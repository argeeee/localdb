import os
from typing import List
from localdb.table import Table

class Database:
	db_name: str
	path: str
	tables: List[Table]

	def __init__(self, db_name: str, path: str):
		self.db_name = db_name
		self.path = path
		self.tables = List[Table]()
	
	def create_table(self, table: Table):
		pass
	
	def delete_table(self, table: Table):
		pass

