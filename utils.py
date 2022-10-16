import os

def create_folder_if_not_exist(directory: str):
		if not os.path.exists(directory):
			os.makedirs(directory)