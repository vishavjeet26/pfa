# importing required modules
from zipfile import ZipFile
import os
import logging 
#import csv

# instance of logging class
logger = logging.getLogger(__name__)
# logging format
format='%(asctime)s : %(levelname)-4s:%(pathname)-4s : %(lineno)d : %(funcName)-4s: %(message)s'
# Basic Logging Configuration without settings.py file
logging.basicConfig(filename = 'logs/compress_zip_error.log', level=logging.DEBUG, format=format)

def get_all_file_paths(directory):

 # initializing empty file paths list
 file_paths = []
 # crawling through directory and subdirectories
 for root, directories, files in os.walk(directory):
  for filename in files:
   # join the two strings in order to form the full filepath.
   filepath = os.path.join(root, filename)
   file_name, ext = os.path.splitext(filepath)
   if ext== '.jpg' or ext== '.txt':
   	file_paths.append(filepath)

 # returning all file paths
 return file_paths

def zip_files(search_directory, selected_extensions, output_path):
 # calling function to get all file paths in the directory
 file_paths = get_all_file_paths(search_directory)

 ext1, ext2 = selected_extensions
 if selected_extensions != ['.jpg','.txt']:
 	print("Only acceptable .jpg and .txt")
 	logging.critical('Only acceptable .jpg and .txt')
 	return False

 # printing the list of all files to be zipped
 print('Following files will be zipped in this program:')
 for file_name in file_paths:
  print(file_name)

 # writing files to a zipfile
 with ZipFile(output_path,'w') as zip:
  # writing each file one by one
  for file in file_paths:
   zip.write(file)

 print('All files zipped successfully!')


if __name__ == "__main__":
    zip_files('.\\my_stuff', ['.jpg','.txt'], 'my_stuff.zip')

