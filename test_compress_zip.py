import pytest
from zip_files import zip_files

def test_zip_files_1():
	res = zip_files('.\\my_stuff', ['.png','.txt'], 'my_stuff.zip')
	assert res

def test_zip_files_2():
	res = zip_files('.\\my_stuff', ['.jpg','.txt'], 'my_stuff.zip')
	assert res
		

