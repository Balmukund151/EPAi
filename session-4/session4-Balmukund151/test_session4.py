import pytest
import random
import string
import session4
import os
import inspect
import re
import math
from session4 import Qualean

README_CONTENT_CHECK_FOR = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]

def test_readme_exists():
    assert os.path.isfile("session-4/session4-Balmukund151/README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_and():
    q1=Qualean(1)
    q2=Qualean(0)
    assert((q1 & q2)==False)

def test_or():
    q1=Qualean(1)
    q2=Qualean(0)
    assert((q1 | q2)==True)

def test_repr():
    q1=Qualean(1)
    assert(repr(q1)==('Qualean('+str(round(q1))+')'))

def test_str():
    q1=Qualean(-1)
    assert(str(q1)==('Qualean('+str(round(q1))+')'))

def test_add():
    q1=Qualean(1)
    q2=Qualean(0)
    assert((q1+q2)==(round(q1)+round(q2)))

def test_eq():
    q1=Qualean(1)
    q2=q1
    assert((q1==q2)==True)

def test_float():
    q1=Qualean(1)
    assert(float(q1)==float(round(q1)))

def test_ge():
    q1=Qualean(1)
    q2=Qualean(0)
    assert((q1>=q2)==(round(q1)>=round(q2)))

def test_gt():
    q1=Qualean(1)
    q2=Qualean(0)
    assert((q1>q2)==(round(q1)>round(q2)))

def test_invertsign():
    q1=Qualean(1)
    assert(float(q1.__invertsign__())==(float(q1.computed_val)*-1))

def test_le():
    q1=Qualean(1)
    q2=Qualean(0)
    assert((q1<=q2)==(round(q1)<=round(q2)))

def test_lt():
    q1=Qualean(1)
    q2=Qualean(0)
    assert((q1<q2)==(round(q1)<round(q2)))


def test_mul():
    q1=Qualean(1)
    q2=Qualean(0)
    assert((q1*q2)==(round(round(q1)*round(q2))))
    
def test_sqrt():
    q1=Qualean(1)
    if q1.computed_val<0:
        assert(float(q1.__sqrt__())==round(float(math.sqrt(-1*q1.computed_val)),10))
    else:
        assert(float(q1.__sqrt__())==round(float(math.sqrt(q1.computed_val)),10))
    
def test_bool():
    q1=Qualean(1)
    assert(bool(q1)==True)
    
def test_check_for_100_sums():
    q1=Qualean(1)
    assert(q1.check_for_100_sums()==True)
    
def test_sum_1_milliontimes():
    q1=Qualean(1)
    assert(q1.sum_1_milliontimes(1000000)==True)
    
def test_q1_q2_false():
    q1=Qualean(0)
    q2=Qualean(1)
    assert((q1 & q2) == False)
    
def test_q1_q2_true():
    pass
    


