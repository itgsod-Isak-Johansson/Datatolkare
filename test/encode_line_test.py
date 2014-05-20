#encoding: utf-8

from nose.tools import *

import sys
sys.path.append('..')

from lib.parser import encode_line


def setup():
    global example_list, example_dict
    example_list = ["1", "88", "59", "74", "53.8", "0.00", "F", "280", "9.6", "270", "17", "1.6", "93", "23", "1004.5"]
    example_dict = {'date': 1, 'max': 88, 'min': 59 }


def test_encode_line_takes_a_list_as_argument():
    assert_raises(TypeError, encode_line)

#Detta test kan kommenteras bort om man inte vill testa 'Undantagshantering' på C- eller A-nivå
def test_encode_line_raises_ValueError_with_correct_error_message_if_list_is_too_short():
    with assert_raises(ValueError) as e:
        encode_line([1,2])
    assert_equal(e.exception.message, 'incomplete list')


@with_setup(setup())
def test_encode_returns_a_dict_with_correct_keys():
    assert_equal(encode_line(example_list).keys(), ['date', 'max', 'min'])


@with_setup(setup())
def test_encode_line_returns_the_list_correctly_encoded_as_a_hash():
    assert_equal(encode_line(example_list), example_dict)
