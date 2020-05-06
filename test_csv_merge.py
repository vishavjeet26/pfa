import pytest
from csv_merge import csv_merge

def test_csv_merge_1():
	res = csv_merge(['class1.csv', 'class2.csv'], 'all_students.csv')
	assert res

def test_csv_merge_2():
	res = csv_merge(['class1', 'class2.csv'], 'all_students.csv')
	assert res

def test__csv_merge_3():
	res = csv_merge(['class1.csv', 'class2.csv','class3.csv'], 'all_students.csv')
	assert res		

