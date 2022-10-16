from enum import Enum

class ComparationOperator(Enum):
	Equals = 1
	Greater = 2
	GreaterEquals = 3
	Less = 4
	LessEquals = 5
	NotEquals = 6

class Condition:
	table_field: str
	comp: ComparationOperator
	to_find: str

