import datetime
from io import TextIOWrapper

import pickle
import os
import types
import pprint

from localdb.base_unit import BaseUnit
from localdb.utils import (
	json
)

class Row(BaseUnit):
	_row_dbFolder: str
	_row_dbName: str
	_row_tableName: str
	_row_key: str
	_row_filename: str
	
	_row_fdReadonly: TextIOWrapper

	def __init__(self, dbFolder: str, dbName: str, tableName: str, key: str, lock_type = None):
		self._row_dbFolder = dbFolder
		self._row_dbName = dbName
		self._row_tableName = tableName
		self._row_key = key
		self._row_filename = os.path.join(self._row_dbFolder, self._row_dbName, self._row_tableName, key)
		self._row_fdReadonly = open(self._row_filename, 'r')

		self._loadContents()

	def _loadContents(self):
		self._row_fdReadonly.seek(0)
		contents = self._row_fdReadonly.read()
		contents = self._desearialize(contents)
		self.__dict__.update(contents)

	def __repr__(self):
		attribs = self._getPublicAttribs()
		return '<LocalDB.Row object - key: %s>\n\n%s' % (self._row_key, pprint.pformat(attribs))

	def _getPublicAttribs(self):
		return dict([(key, value) for key, value in self.__dict__.items() if key[0] != '_'])

	def _desearializeHelper(self, d):
		if type(d) in (list, tuple):
			return map(self._desearializeHelper, d)
		elif type(d) == dict:
			for key in d:
				d[key] = self._desearializeHelper(d[key])
			return d
		else:
				return d

	def _desearialize(self, contents):
		contents = json.loads(contents)
		contents = self._desearializeHelper(contents)
		return contents

	def _writeContents(self):
		attribs = self._serialize()
		with open(self._row_filename, 'w') as fd:
			fd.write(attribs)

	def _serializeHelper(self, d):
		if type(d) in (list, tuple):
			return map(self._serializeHelper, d)
		elif type(d) == dict:
			for key in d:
				d[key] = self._serializeHelper(d[key])
			return d
		# TODO: missing unicode and long types
		elif type(d) in (dict, list, tuple, str, int, float, bool): # json-supported data types
			return d
		else:
			return {}

	def _serialize(self):
		attribs = self._getPublicAttribs()
		attribs = self._serializeHelper(attribs)
		attribs = json.dumps(attribs)
		return attribs
	
	def save(self):
		self._writeContents()

	# Getters & setters
	def __setitem__(self, key: str, value):
		self.__dict__[key] = value
	
	def __getitem__(self, key: str):
		return self.__dict__[key]

	def getCreatedDate(self):
		return datetime.datetime.fromtimestamp(os.path.getctime(self._row_filename))

	def getModifiedDate(self):
		return datetime.datetime.fromtimestamp(os.path.getmtime(self._row_filename))

	def getKey(self):
		return self._row_key
		