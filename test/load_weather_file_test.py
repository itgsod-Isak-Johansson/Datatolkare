#encoding: utf-8

from nose.tools import assert_equal
from nose.tools import assert_is_instance
from nose.tools import assert_raises

import sys
sys.path.append('..')

from lib.parser import load_weather_file

def test_load_weather_file_takes_a_path_as_argument():
    assert_raises(TypeError, load_weather_file)


def test_load_weather_file_raises_ValueError_with_correct_error_message_if_path_is_empty():
    with assert_raises(ValueError) as e:
        load_weather_file('')
    assert_equal(e.exception.message, 'path must not be empty')

#Detta test kan kommenteras bort om man inte vill testa 'Undantagshantering' på C- eller A-nivå
def test_load_weather_file_raises_IOError_with_correct_message_if_file_does_not_exist():
    with assert_raises(IOError) as e:
        load_weather_file('nonexisting.file')
    assert_equal(e.exception.message, 'file does not exist')

def test_load_weather_file_reads_the_file_and_returns_an_array_of_all_rows_EXCEPT_the_first_two():
    assert_equal(load_weather_file('test/test.dat'), ["   1  88    67    74          53.8       0.00 F       280  9.6 270  17  1.6  93 23 1004.5\n", "   2  87    61    71          46.5       0.00         330  8.7 340  23  3.3  70 28 1004.5\n", "   3  83    72    66          39.6       0.00         350  5.0 350   9  2.8  59 24 1016.8"])

