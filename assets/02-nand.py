# %%
# prelude

from random import seed
from random import randint

seed(42)


# %%
def NAND(b0: bool, b1: bool) -> bool:
    """return b0 NAND b1

    Args:
        b0 (bool): first bit
        b1 (bool): second bit

    Returns:
        bool: b0 nand b1
        False if both inputs are True. True otherwise
    """
    return not (b1 and b0)


# %%
def NOT(b: bool) -> bool:
    return NAND(b, b)


# testing
print(NOT(0))
print(NOT(1))


# %%
def AND(b1: bool, b0: bool) -> bool:
    b2 = NAND(b1, b0)
    return NAND(b2, b2)


# testing
print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))


# %%
def XOR(b1: bool, b0: bool) -> bool:
    b2 = NAND(b0, b1)

    b3 = NAND(b0, b2)
    b4 = NAND(b1, b2)

    return NAND(b3, b4)


# testing
print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))


# %%
def ADD_32(b2: bool, b1: bool, b0: bool) -> tuple[bool, bool]:
    i1 = NAND(b2, b1)
    i2 = XOR(b1, b2)
    i3 = NAND(i2, b0)
    i4 = XOR(b0, i2)
    i5 = NAND(i1, i3)

    return i5, i4


# testing
print(ADD_32(0, 0, 0))
print(ADD_32(0, 0, 1))
print(ADD_32(0, 1, 0))
print(ADD_32(0, 1, 1))
print(ADD_32(1, 0, 0))
print(ADD_32(1, 0, 1))
print(ADD_32(1, 1, 0))
print(ADD_32(1, 1, 1))


# %%
def ADD_4bits(
    op1b3, op1b2, op1b1, op1b0, op2b3, op2b2, op2b1, op2b0
) -> tuple[bool, bool, bool, bool, bool]:

    i1, i0 = ADD_32(op1b0, op2b0, 0)
    i3, i2 = ADD_32(op1b1, op2b1, i1)
    i5, i4 = ADD_32(op1b2, op2b2, i3)
    i7, i6 = ADD_32(op1b3, op2b3, i5)

    return i7, i6, i4, i2, i0


# %%
def DecTo4bits(i: int) -> tuple[bool, bool, bool, bool]:
    """Convert an int <= 15 to 4 distinct bits

    Args:
        i (int): the int to be converted

    Returns:
        tuple [bool, bool, bool, bool]: the corresponding bits. MSB on the left, LSB on the right.
    """
    b0 = i % 2
    i = i // 2

    b1 = i % 2
    i = i // 2

    b2 = i % 2
    i = i // 2

    b3 = i % 2
    # i = i//2

    return b3, b2, b1, b0


# %%
# test for ADD_4bits()
for i in range(5):
    op1 = randint(0, 15)
    op2 = randint(0, 15)

    i3, i2, i1, i0 = DecTo4bits(op1)
    j3, j2, j1, j0 = DecTo4bits(op2)
    o4, o3, o2, o1, o0 = ADD_4bits(i3, i2, i1, i0, j3, j2, j1, j0)
    result = o4 * 2**4 + o3 * 2**3 + o2 * 2**2 + o1 * 2**1 + o0 * 2**0
    print(f"i = {op1:2}   j = {op2:2}   i+j = {result:2}")


# %%
def MUL_4bits(op1b3, op1b2, op1b1, op1b0, op2b3, op2b2, op2b1, op2b0):

    i0 = AND(op1b0, op2b0)
    i1 = AND(op1b1, op2b0)
    i2 = AND(op1b2, op2b0)
    i3 = AND(op1b3, op2b0)

    i4 = AND(op1b0, op2b1)
    i5 = AND(op1b1, op2b1)
    i6 = AND(op1b2, op2b1)
    i7 = AND(op1b3, op2b1)

    i9, i8 = ADD_32(i4, i1, 0)
    i11, i10 = ADD_32(i5, i2, i9)
    i13, i12 = ADD_32(i6, i3, i11)
    i15, i14 = ADD_32(i7, 0, i13)

    i16 = AND(op1b0, op2b2)
    i17 = AND(op1b1, op2b2)
    i18 = AND(op1b2, op2b2)
    i19 = AND(op1b3, op2b2)

    i21, i20 = ADD_32(i16, i10, 0)
    i23, i22 = ADD_32(i17, i12, i21)
    i25, i24 = ADD_32(i18, i14, i23)
    i27, i26 = ADD_32(i19, i15, i25)

    i28 = AND(op1b0, op2b3)
    i29 = AND(op1b1, op2b3)
    i30 = AND(op1b2, op2b3)
    i31 = AND(op1b3, op2b3)

    i33, i32 = ADD_32(i28, i22, 0)
    i35, i34 = ADD_32(i29, i24, i33)
    i37, i36 = ADD_32(i30, i26, i35)
    i39, i38 = ADD_32(i31, i27, i37)

    return i39, i38, i36, i34, i32, i20, i8, i0


# %%
# test for MUL_4bits()
for i in range(5):
    op1 = randint(0, 15)
    op2 = randint(0, 15)

    i3, i2, i1, i0 = DecTo4bits(op1)
    j3, j2, j1, j0 = DecTo4bits(op2)
    o7, o6, o5, o4, o3, o2, o1, o0 = MUL_4bits(i3, i2, i1, i0, j3, j2, j1, j0)
    result = (
        o7 * 2**7
        + o6 * 2**6
        + o5 * 2**5
        + o4 * 2**4
        + o3 * 2**3
        + o2 * 2**2
        + o1 * 2**1
        + o0 * 2**0
    )
    print(f"i = {op1:2}   j = {op2:2}   i*j = {result:3}")
