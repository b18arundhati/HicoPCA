# Principal Components Analysis
This website and its associated scripts generate a Principal Components Analysis from hyperspectral imagery from the HICO (Hyperspectral Imager for the Coastal Ocean) imager. This data can be downloaded for free from http://hico.coas.oregonstate.edu. To use with this website, the data must be downloaded in ENVI format. 

### Introduction 
Hyperspectral imagery, which contains data from across the electromagnetic spectrum, is a useful resource with uses across different fields and industries. However, raw hyperspectral data generally contains hundreds of bands of data, which creates tremendously large files. To reduce the dimensionality of this data, we can apply Principal Components Analysis (PCA), which is a technique to calculate the eigenvectors with the greatest variability and reproject the data using them, reducing the data to a few very different bands. 

### HICO 
I decided to use HICO imagery because it is relatively small. HICO data can be downloaded for free from [Oregon State](http://hico.coas.oregonstate.edu/datasearch/data-search-basic.php) University's website in ENVI or HDF5 format; these scripts work with the L1B data in ENVI format.

Hico data characteristics: 
* 87 bands from 400-900 nm
* 5.7 nm spectral resolution
* A high signal-to-noise ratio, 200:1
* Images are 500 * 2000 pixels, for a 50 x 200 km scene

### Technology and File Structure 
This site is programmed with Javascript on the front end and Python 3.4 for the backend, using CherryPy for the server. 