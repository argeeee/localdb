
import os
import errno
import random
import string

from localdb.base_unit import BaseUnit
from localdb.row import Row
from localdb.errors import (
	RowAlreadyExists,
	RowDoesNotExist,
)

class Table(BaseUnit):
	path: str
	dbName: str
	tableName: str
	
	def __init__(self, path: str, dbName: str, tableName: str):
		self.path = path
		self.dbName = dbName
		self.tableName = tableName

	def getRow(self, key: str):
		row = Row(self.path, self.dbName, self.tableName, key)
		return row
	
	def createRow(self, key: str): 
		filename = os.path.join(self.path, self.dbName, self.tableName, key)
		if os.path.exists(filename):
			raise RowAlreadyExists(key)
		with open(filename, 'w') as fd:
			fd.write('{}')
			row = Row(self.path, self.dbName, self.tableName, key)

		return row

	def createRowWithUniqueKey(self, key_len = 5):
		# TODO: to optimize generation
		while True:
			try:
				key = self._generateRandomString(key_len)
				row = self.createRow(key)
				break
			except RowAlreadyExists:
				continue

		return row

	def remove(self, key):
		try:
			os.remove(os.path.join(self.path, self.dbName, self.tableName, key))
		except IOError as e:
			if e.errno == errno.ENOENT: # if the file doesn't exist
				raise RowDoesNotExist(key)
			else:
				raise

	def _generateRandomString(self, length=5):
		return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])
