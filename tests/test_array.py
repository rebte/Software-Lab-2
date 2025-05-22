import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from array_list import ArrayList

@pytest.fixture
def sample_array():
    arr = ArrayList()
    for val in ["a", "b", "c"]:
        arr.append(val)
    return arr

def test_append(sample_array):
    sample_array.append("d")
    assert sample_array.get(3) == "d"
    assert sample_array.length() == 4

def test_insert_beginning(sample_array):
    sample_array.insert("start", 0)
    assert sample_array.get(0) == "start"

def test_insert_middle(sample_array):
    sample_array.insert("mid", 1)
    assert sample_array.get(1) == "mid"

def test_insert_end(sample_array):
    sample_array.insert("end", sample_array.length())
    assert sample_array.get(sample_array.length() - 1) == "end"

def test_delete(sample_array):
    removed = sample_array.delete(1)
    assert removed == "b"
    assert sample_array.length() == 2
    assert sample_array.get(1) == "c"

def test_delete_all(sample_array):
    sample_array.append("b")
    sample_array.deleteAll("b")
    assert sample_array.length() == 2
    assert sample_array.get(0) == "a"
    assert sample_array.get(1) == "c"

def test_get(sample_array):
    assert sample_array.get(0) == "a"
    assert sample_array.get(2) == "c"
    with pytest.raises(IndexError):
        sample_array.get(10)

def test_clone(sample_array):
    cloned = sample_array.clone()
    assert cloned.length() == sample_array.length()
    assert all(cloned.get(i) == sample_array.get(i) for i in range(cloned.length()))

def test_reverse(sample_array):
    sample_array.reverse()
    assert sample_array.get(0) == "c"
    assert sample_array.get(2) == "a"

def test_find_first(sample_array):
    sample_array.append("b")
    assert sample_array.findFirst("b") == 1
    assert sample_array.findFirst("z") == -1

def test_find_last(sample_array):
    sample_array.append("b")
    assert sample_array.findLast("b") == sample_array.length() - 1
    assert sample_array.findLast("z") == -1

def test_clear(sample_array):
    sample_array.clear()
    assert sample_array.length() == 0

def test_extend():
    arr1 = ArrayList()
    arr2 = ArrayList()
    for val in ["a", "b"]:
        arr1.append(val)
    for val in ["c", "d"]:
        arr2.append(val)
    arr1.extend(arr2)
    assert arr1.length() == 4
    assert arr1.get(2) == "c"
    assert arr1.get(3) == "d"
