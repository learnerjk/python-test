from app import index,throw
import pytest

def test_index():
	temp = index()
	assert temp["1"]== "2"

def test_throw():
	with pytest.raises(Exception):
		throw()
