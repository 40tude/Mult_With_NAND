from random import seed
from random import randint

from nand.nand_fn import ADD_4bits
from nand.nand_fn import MUL_4bits


def DecTo4bits(i: int) -> tuple[bool, bool, bool, bool]:
    """
    Convert an int (<= 15) in 4 distinct bits

    Args:
        i (int): the int to be converted

    Returns:
        tuple [bool, bool, bool, bool]: the corresponding bits. MSB on the left, LSB on the right.
    """
    assert i <= 15

    b0 = i % 2
    i = i // 2

    b1 = i % 2
    i = i // 2

    b2 = i % 2
    i = i // 2

    b3 = i % 2
    # i = i//2

    return b3, b2, b1, b0


if __name__ == "__main__":

    # seed(42)

    # shows how to call ADD_4bits()
    for i in range(5):
        op1 = randint(0, 15)  # 4 bits max => 15
        op2 = randint(0, 15)

        i3, i2, i1, i0 = DecTo4bits(op1)
        j3, j2, j1, j0 = DecTo4bits(op2)
        o4, o3, o2, o1, o0 = ADD_4bits(i3, i2, i1, i0, j3, j2, j1, j0)
        result = o4 * 2**4 + o3 * 2**3 + o2 * 2**2 + o1 * 2**1 + o0 * 2**0
        print(f"i = {op1:2}   j = {op2:2}   i+j = {result:2}")

    print()

    # shows how to call MUL_4bits()
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
