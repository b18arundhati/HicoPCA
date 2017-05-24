def pca(filename):
	import numpy as np
	from osgeo import gdal, osr, ogr
	from PIL import Image
	import matplotlib
	matplotlib.use('TkAgg')
	import matplotlib.pyplot as plt
	from pathlib import Path
	import os 

	cmap = plt.cm.jet
	_file = Path(filename)

	# create "results" folder if none exists
	if not os.path.exists("results"):
	    os.makedirs("results")

	def createResultFile(file):
		return (os.path.dirname(os.path.abspath(__file__)) + '/' + 'results' + '/' + file)

	# check if file is valid 
	if _file.is_file():
		ds = gdal.Open(filename)  
	else:
		raise ValueError('No file with name ' + filename)

	## all Hico data is 200 * 500 - hardcoded 
	xRes     = 500;
	yRes     = 2000;
	numBands = ds.RasterCount
	npBands = np.empty((numBands, yRes, xRes))

	# Fill each band and calculate means
	print("Loading to numpy")
	means = []
	for band in range( ds.RasterCount ):
	    nparray = ds.GetRasterBand(band + 1).ReadAsArray()
	    npBands[band] = nparray
	    means.append(np.mean(nparray))

	# Calculate covariance (result is 87 x 87 matrix expressing pixel covariance per band)
	print("Calculating covariance matrix")
	cv = np.zeros((numBands, numBands))
	for i in range(numBands):
	    for j in range(numBands):
	        x = npBands[i]
	        y = npBands[j]
	        meanx = means[i]
	        meany = means[j]
	        cv[i, j] = ((x - meanx) * (y - meany)).sum() / (numBands - 1)

	plt.plot(cv)
	plt.savefig(createResultFile("convariance matrix.png"))

	# Get the eigenvalues and eigenvectors from the covariance matrix
	print("Calculating eigenvalues/vectors")
	eig_val, eig_vec = np.linalg.eig(cv)
	plt.plot(eig_vec)
	plt.savefig(createResultFile("eigenvectors.png"))
	plt.plot(eig_val)
	plt.savefig(createResultFile("eigenvalues.png"))

	# Get the top 3
	print("Getting the top 3")
	eig_pairs = [(np.abs(eig_val[i]), eig_vec[:,i]) for i in range(len(eig_val))]
	eig_pairs.sort(key=lambda x: x[0], reverse=True)
	top3_pc = np.zeros((3, numBands))

	# Pull out the eigenvectors
	top3_pc[0] = np.asarray(eig_pairs[0][1])
	top3_pc[1] = np.asarray(eig_pairs[1][1])
	top3_pc[2] = np.asarray(eig_pairs[2][1])
	print(top3_pc)

	# Reshape for understandability - we have numBands dimensions, the rows and columns are the data 
	print("Transforming data")
	npBandsReshaped = npBands.reshape(numBands, npBands.shape[1] * npBands.shape[2])
	matrix_w = np.hstack((top3_pc[0].reshape(numBands, 1), top3_pc[1].reshape(numBands, 1), top3_pc[2].reshape(numBands, 1)))

	# Transformation is dot product - sum of product of each value in three dimensions times data
	transformed = matrix_w.T.dot(npBandsReshaped)
	output = transformed.reshape(3, npBands.shape[1], npBands.shape[2])

	# Show top three components
	plt.imsave(createResultFile("PCA 1.png"), output[0,:, :], cmap=cmap)
	plt.imsave(createResultFile("PCA 2.png"), output[1,:, :], cmap=cmap)
	plt.imsave(createResultFile("PCA 3.png"), output[2,:, :], cmap=cmap)

pca('../hico_sample_files/Egypt/iss.2014169.0618.122053.L1B.Lake_Manzalah.v04.16437.20140618190545.100m.hico.bil')