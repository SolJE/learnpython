try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description' : 'My way of Python'
	'author' : 'SOL JE'
	'url' : 'http://deih.cn'
	'download_url' : 'http://deih.cn'
	'author_email' : 'deih@deih.cn'
	'version' : '0.1'
	'install_requires' : ['nose']
	'packages' : ['NAME']
	'scripts' : []
	'name' : 'mwop'
}

setup(**config)