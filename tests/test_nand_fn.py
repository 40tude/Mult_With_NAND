import pytest
from src.nand.nand_fn import NAND
from src.nand.nand_fn import AND
from src.nand.nand_fn import XOR
from src.nand.nand_fn import ADD_32


# test_xxxxx
def test_NAND():
    b = NAND(0, 0)
    assert b == True

    b = NAND(0, 1)
    assert b == True

    b = NAND(1, 0)
    assert b == True

    b = NAND(1, 1)
    assert b == False

    # b = NAND(1, 1)
    # assert b == True


def test_AND():
    b = AND(0, 0)
    assert b == False

    b = AND(0, 1)
    assert b == False

    b = AND(1, 0)
    assert b == False

    b = AND(1, 1)
    assert b == True


def test_XOR():
    b = XOR(0, 0)
    assert b == False

    b = XOR(0, 1)
    assert b == True

    b = XOR(1, 0)
    assert b == True

    b = XOR(1, 1)
    assert b == False


def test_ADD_32():
    b1, b0 = ADD_32(0, 0, 0)
    result = b1 * 2**1 + b0 * 2**0
    assert result == 0

    b1, b0 = ADD_32(0, 0, 1)
    result = b1 * 2**1 + b0 * 2**0
    assert result == 1

    b1, b0 = ADD_32(0, 1, 0)
    result = b1 * 2**1 + b0 * 2**0
    assert result == 1

    b1, b0 = ADD_32(0, 1, 1)
    result = b1 * 2**1 + b0 * 2**0
    assert result == 2

    b1, b0 = ADD_32(1, 0, 0)
    result = b1 * 2**1 + b0 * 2**0
    assert result == 1

    b1, b0 = ADD_32(1, 0, 1)
    result = b1 * 2**1 + b0 * 2**0
    assert result == 2

    b1, b0 = ADD_32(1, 1, 0)
    result = b1 * 2**1 + b0 * 2**0
    assert result == 2

    b1, b0 = ADD_32(1, 1, 1)
    result = b1 * 2**1 + b0 * 2**0
    assert result == 3
