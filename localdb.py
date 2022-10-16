"""
LocalDB library 

"""
import os
import shutil

from localdb.database import Database

class LocalDB:
	db_folder: str

	def __init__(self, db_folder: str):
		self.db_folder = db_folder
		self._create_folder_if_not_exist(self.db_folder)

	def load_db(self, database_name: str) -> Database:
		pass
	
	def create_db(self, database_name: str):
		path = os.path.join(self.db_folder, database_name)
		self._create_folder_if_not_exist(path)

	def delete_db(self, database_name: str) -> Database:
		path = os.path.join(self.db_folder, database_name)
		shutil.rmtree(path)
	
	# Private methods
	def _create_folder_if_not_exist(self, directory: str):
		if not os.path.exists(directory):
			os.makedirs(directory)
