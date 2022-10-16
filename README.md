# LocalDB library

A simple json database 

## Installation

To install correctly the library run:

On macos & linux
```bash
pip3 install -r requirements.txt
```

On windows
```bat
pip install -r requirements.txt
```

## Usage
```python
from localdb.LocalDB import LocalDB
from localdb.errors import (
	DatabaseAlreadyExists,
	RowAlreadyExists,
	TableAlreadyExists,
)

STORE_FOLDER = 'db_store'
DB_NAME = 'db'
TABLE_NAME = 'table'
ROW_KEY = 'ROW_1234'

store = LocalDB(STORE_FOLDER)

try:
	store.createDatabase(DB_NAME)
except DatabaseAlreadyExists as e:
	pass
except Exception as e:
	print('error: cannot create database | unknown exception')
	exit(-1)

db = store.getDatabase(DB_NAME)

try:
	db.createTable(TABLE_NAME)
except TableAlreadyExists as e:
	pass
except Exception as e:
	print('error: cannot create table | unknown exception')
	exit(-1)

table = db.getTable(TABLE_NAME)

try:
	table.createRow(ROW_KEY)
except RowAlreadyExists as e:
	pass
except Exception as e:
	print('error: cannot create row | unknown exception')
	exit(-1)

row = table.getRow(ROW_KEY)

row['id'] = ROW_KEY
row.save()
```
