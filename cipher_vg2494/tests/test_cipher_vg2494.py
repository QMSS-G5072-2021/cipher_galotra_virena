from cipher_vg2494 import cipher_vg2494

import pytest

def test_cipher_with_single_word():
    example = "Potato"
    expected = "Srwdwr"
    result = cipher(example, 3, encrypt = True)
    assert result == expected