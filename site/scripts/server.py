""" 

Init CherryPy server for site 

"""

import os.path
import cherrypy
from cherrypy.lib import file_generator

PATH = os.path.abspath(os.path.dirname(__file__))

class Root(object): 
	@cherrypy.expose
	def test(self):
		return "Hello world!"

	@cherrypy.expose
	def setHicoFile(self, filename):
		filename = filename.split('.')
		basename = '.'.join(filename[:-2])
		cherrypy.session['hicoFile'] = basename

	@cherrypy.expose
	def getHicoFile(self):
		return cherrypy.session['hicoFile']

	@cherrypy.expose
	def getPCA(self):
		# not working
		# pca('../hico_sample_files/Egypt/iss.2014169.0618.122053.L1B.Lake_Manzalah.v04.16437.20140618190545.100m.hico.bil')
		# cherrypy.response.headers['Content-Type'] = "image/png"
		# path = os.path.dirname(os.path.realpath(__file__)) + '/results/PCA 1.png'
		# return serve_file('results/PCA 1.png') 

cherrypy.tree.mount(Root(), '/', config={
	'/': {
	'tools.staticdir.on': True,
	'tools.staticdir.dir': PATH,
	'tools.staticdir.index': 'index.html',
	'tools.sessions.on': True,
	'tools.sessions.storage_type': "File",
	'tools.sessions.storage_path': 'sessions',
	'tools.sessions.timeout': 10
	}
})

cherrypy.engine.start()
