# -*- coding: utf-8 -*-
"""\
Tests against <https://github.com/mnooner256/pyqrcode/issues/29>

Negative numbers aren't supported by "numeric" mode.
"""
from __future__ import unicode_literals
import pyqrcodeng as pyqrcode


def test_negative_int():
    qr = pyqrcode.create(-7)
    assert b'-7' == qr.data
    assert 'alphanumeric' == qr.mode


def test_negative_int_str():
    qr = pyqrcode.create('-123')
    assert b'-123' == qr.data
    assert 'alphanumeric' == qr.mode


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
