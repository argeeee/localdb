def getJsonModule():
	try:
		module = __import__('ujson')
		return module
	except ImportError:
		pass

	try:
		module = __import__('cjson')
		class json(object):
			loads = module.decode
			dumps = module.encode
		return json()
	except ImportError:
		pass

	try:
		module = __import__('json')
		return module
	except ImportError:
		raise ImportError('No acceptable json module found.')

json = getJsonModule()
