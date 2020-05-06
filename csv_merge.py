# importing pandas module
import pandas as pd
import os
import logging 
#import csv

# instance of logging class
logger = logging.getLogger(__name__)
# logging format
format='%(asctime)s : %(levelname)-4s:%(pathname)-4s : %(lineno)d : %(funcName)-4s: %(message)s'
# Basic Logging Configuration without settings.py file
logging.basicConfig(filename = 'logs/csv_merge_error.log', level=logging.DEBUG, format=format)

def csv_merge(list_of_csv_file, output_path):   
    # build list with all fieldnames
    if len(list_of_csv_file)!=2:
    	print("List of CSV files should be two")
    	logging.critical('List of CSV files should be two')
    	return False

    file_name1, ext1 = os.path.splitext(list_of_csv_file[0])
    file_name2, ext2 = os.path.splitext(list_of_csv_file[1])
    if ext1 !='.csv' or ext2 !='.csv':
    	print("File extension is wrong, only csv file acceptable")
    	logging.critical('File extension is wrong')
    	return False
    # Read CSV file	
    csv_file1 = pd.read_csv(list_of_csv_file[0])
    csv_file2 = pd.read_csv(list_of_csv_file[1])
    # write data to output file based on field names        
    # Convert the csv_file1's Data into DataFrame  
    df1 = pd.DataFrame(csv_file1)
    # Convert the csv_file2's Data into DataFrame   
    df2 = pd.DataFrame(csv_file2)
    # using keys for identify csv data
    frames = [df1, df2 ]
    res = pd.concat(frames, keys=[file_name1, file_name2])
    # Merge the dataframe into output_path
    res.to_csv(output_path)
    print(f"Merge CSV file {file_name1}{ext1} and {file_name2}{ext2} into {output_path}")
    return True    

if __name__ == '__main__':
    csv_merge(['class1.csv', 'class2.csv'], 'all_students.csv')    

