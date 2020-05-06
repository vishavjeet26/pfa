# pfa
### USAGE, REQUIREMENTS and DEPLOYMENT

#1: Clone 
> git clone https://github.com/vishavjeet26/pfa.git

#2: Change into project directory
>cd pfa

#3: Make virtual environment
>virtualenv env

#4: Activate virtual environment
>env\Scripts\Activate

#5: Install requirements
>pip install -r requirements.txt

#6: Setup (if necessary)

### Run Problem 1: Write method to merge 2 csv files with different column header and write the output to another csv with headers from all the csv's files.
>python csv_merge.py

### Run Problem 2: Write a method to compress all file in a folder with specified extensions and save to output
>python zip_files.py

### Unit test cases using pytest for problem 1 and probem 2 (test_csv_merge.py , test_compress_zip.py)
>pytest

