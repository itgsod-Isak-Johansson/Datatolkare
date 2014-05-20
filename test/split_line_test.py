#encoding: utf-8

from nose.tools import *
import sys
#sys.path.append('..')
from lib.parser import split_line

#Split line

def setup():
    global example_input, example_output
    example_input = "   1  88    59    74          53.8       0.00 F       280  9.6 270  17  1.6  93 23 1004.5\n"
    example_output = ["1", "88", "59", "74", "53.8", "0.00", "F", "280", "9.6", "270", "17", "1.6", "93", "23", "1004.5"]


def test_split_line_takes_a_string_as_argument():
    assert_raises(TypeError, split_line)


#Detta test kan kommenteras bort om man inte vill test 'Undantagshantering' på C- eller A-nivå
def test_split_line_raises_ValueError_with_correct_error_message_if_fed_a_blank_line():
    with assert_raises(ValueError) as e:
        split_line('')
    assert_equal(e.exception.message, 'can not parse empty line')

@with_setup(setup())
def test_split_line_returns_a_list():
    assert_is_instance(split_line(example_input), list)


@with_setup(setup())
def test_split_line_returns_a_list_with_each_value_in_its_own_field():
    assert_equal(split_line(example_input), example_output)