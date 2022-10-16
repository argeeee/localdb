"""
LocalDB library 

"""
import errno
import imp
import os
import shutil

from localdb.database import Database
from localdb.errors import (
	DatabaseAlreadyExists,
	DatabaseDoesNotExist,
)


class LocalDB:
	dbFolder: str

	def __init__(self, dbFolder: str):
		self.dbFolder = dbFolder
		if not os.path.exists(dbFolder):
			os.makedirs(dbFolder)

	def getDatabase(self, dbName: str):
		return Database(self.dbFolder, dbName)

	def createDatabase(self, dbName: str):
		try:
			os.mkdir(os.path.join(self.dbFolder, dbName))
		except OSError as e:
			if e.errno == errno.EEXIST:
				raise DatabaseAlreadyExists(dbName)
			else:
				raise

	def removeDatabase(self, dbName: str):
		try:
			shutil.rmtree(os.path.join(self.dbFolder, dbName))
		except OSError as e:
			if e.errno == errno.ENOENT: # if the table doesn't exist
				raise DatabaseDoesNotExist(dbName)
			else:
				raise
	
