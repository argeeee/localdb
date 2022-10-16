import errno
import os
from pathlib import Path
import shutil
from typing import Dict, List
from localdb.base_unit import BaseUnit
from localdb.table import Table

from localdb.errors import (
	TableAlreadyExists,
	TableDoesNotExist,
)

class Database(BaseUnit):
	path: str
	dbName: str

	def __init__(self, path: str, dbName: str):
		self.path = path
		self.dbName = dbName

	def getTable(self, tableName: str):
		return Table(self.path, self.dbName, tableName)

	def createTable(self, tableName: str):
		try:
			os.mkdir(os.path.join(self.path, self.dbName, tableName))
		except OSError as e:
			if e.errno == errno.EEXIST:
				raise TableAlreadyExists(tableName)
			else:
				raise

	def removeTable(self, tableName: str):
		try:
			shutil.rmtree(os.path.join(self.path, self.dbName, tableName))
		except OSError as e:
			if e.errno == errno.ENOENT: # if the table doesn't exist
				raise TableDoesNotExist(tableName)
			else:
				raise

