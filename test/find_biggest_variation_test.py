#encoding: utf-8

from nose.tools import assert_equal
from nose.tools import assert_is_instance
from nose.tools import assert_raises

import sys
sys.path.append('..')

from lib.parser import find_biggest_variation

def test_find_biggest_variation_takes_a_list_of_hashes_as_argument():
    assert_raises(TypeError, find_biggest_variation)

# #Detta test kan kommenteras bort om man inte vill testa 'Undantagshantering' på C- eller A-nivå
# def test_find_biggest_variation_raises_ValueError_with_correct_error_message_if_array_is_empty():
#     with assert_raises(ValueError) as e:
#         find_biggest_variation([])
#     assert_equal(e.exception.message, 'list must not be empty')


def test_find_biggest_variation_returns_the_hash_for_the_day_with_the_biggest_variation():
    example_list = [{'date': 1, 'max': 88, 'min': 59}, {'date': 2, 'max': 88, 'min': 53}, {'date': 3, 'max': 88, 'min': 67}]
    assert_equal(find_biggest_variation(example_list), {'date': 2, 'max': 88, 'min': 53})

