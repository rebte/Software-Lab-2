import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from linked_list import LinkedList

@pytest.fixture
def sample_list():
    ll = LinkedList()
    for val in [1, 2, 3]:
        ll.append(val)
    return ll

def test_append(sample_list):
    sample_list.append(4)
    assert sample_list.get(3) == 4
    assert sample_list.length() == 4

def test_insert_beginning(sample_list):
    sample_list.insert(0, 0)
    assert sample_list.get(0) == 0

def test_insert_middle(sample_list):
    sample_list.insert(5, 1)
    assert sample_list.get(1) == 5

def test_insert_end(sample_list):
    sample_list.insert(6, sample_list.length())
    assert sample_list.get(sample_list.length() - 1) == 6

def test_delete(sample_list):
    removed = sample_list.delete(1)
    assert removed == 2
    assert sample_list.length() == 2
    assert sample_list.get(1) == 3

def test_delete_all(sample_list):
    sample_list.append(2)
    sample_list.deleteAll(2)
    assert sample_list.length() == 2
    assert sample_list.get(0) == 1
    assert sample_list.get(1) == 3

def test_get(sample_list):
    assert sample_list.get(0) == 1
    assert sample_list.get(2) == 3
    with pytest.raises(IndexError):
        sample_list.get(10)

def test_clone(sample_list):
    cloned = sample_list.clone()
    assert cloned.length() == sample_list.length()
    assert all(cloned.get(i) == sample_list.get(i) for i in range(cloned.length()))

def test_reverse(sample_list):
    sample_list.reverse()
    assert sample_list.get(0) == 3
    assert sample_list.get(2) == 1

def test_find_first(sample_list):
    sample_list.append(2)
    assert sample_list.findFirst(2) == 1
    assert sample_list.findFirst(10) == -1

def test_find_last(sample_list):
    sample_list.append(2)
    assert sample_list.findLast(2) == 3
    assert sample_list.findLast(10) == -1

def test_clear(sample_list):
    sample_list.clear()
    assert sample_list.length() == 0

def test_extend():
    l1 = LinkedList()
    l2 = LinkedList()
    for val in [1, 2]:
        l1.append(val)
    for val in [3, 4]:
        l2.append(val)
    l1.extend(l2)
    assert l1.length() == 4
    assert l1.get(2) == 3
    assert l1.get(3) == 4
