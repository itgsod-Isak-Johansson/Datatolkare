#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('..')

from datatolkare import *

def test_split_line_takes_list_as_argument():
    assert_raises(TypeError, split_line)

#
# def test_split_line_returns_list():
#     assert_is_instance(split_line('   1  88    59    74          53.8       0.00 F       280  9.6 270  17  1.6  93 231004.5\n'), list)
<<<<<<< HEAD
# def
=======
#
>>>>>>> FETCH_HEAD


