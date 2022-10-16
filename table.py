
from typing import Any
from localdb.condition import Condition


class Table:

	def __init__(self):
		pass

	def select(self, condition: Condition):
		pass

	def insert(self, element: Any):
		pass
	
	def update(self, condition: Condition):
		pass

	def delete(self, condition: Condition):
		pass
