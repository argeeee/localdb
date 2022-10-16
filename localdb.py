"""
LocalDB library 

"""
import os
import shutil

from localdb.database import Database
from localdb.utils import create_folder_if_not_exist

class LocalDB:
	db_folder: str

	def __init__(self, db_folder: str):
		self.db_folder = db_folder
		create_folder_if_not_exist(self.db_folder)

	def load_db(self, database_name: str) -> Database:
		path = os.path.join(self.db_folder, database_name)
		return Database(database_name, path)
	
	def create_db(self, database_name: str):
		path = os.path.join(self.db_folder, database_name)
		create_folder_if_not_exist(path)

	def delete_db(self, database_name: str) -> Database:
		path = os.path.join(self.db_folder, database_name)
		shutil.rmtree(path)
	
