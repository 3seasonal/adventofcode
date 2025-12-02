import pytest
from classes01 import Safe_Position_Tracker, Safe_Instruction_Handler


def test_move_right_simple():
    t = Safe_Position_Tracker(starting_position=0, modulus=10)
    assert t.get_current_position() == 0
    t.move("R3")
    assert t.get_current_position() == 3
    assert t.get_zero_count() == 0
    assert t.get_traverse_zero_count() == 0
    assert t.get_instruction_count() == 1


def test_move_right_wrap_and_zero():
    t = Safe_Position_Tracker(starting_position=8, modulus=10)
    t.move("R4")  # 8+4=12 -> pos 2, crossed zero once
    assert t.get_current_position() == 2
    assert t.get_traverse_zero_count() == 1
    assert t.get_zero_count() == 0


def test_move_land_on_zero_counts_traverse_and_zero():
    t = Safe_Position_Tracker(starting_position=7, modulus=10)
    t.move("R3")  # 7+3=10 -> pos 0
    assert t.get_current_position() == 0
    assert t.get_zero_count() == 1
    # landing exactly on zero should NOT count as a traversal (only a rest)
    assert t.get_traverse_zero_count() == 0


def test_move_left_wrap():
    t = Safe_Position_Tracker(starting_position=2, modulus=10)
    t.move("L5")  # 2-5 = -3 -> pos 7, should have crossed zero once
    assert t.get_current_position() == 7
    assert t.get_traverse_zero_count() == 1


def test_large_steps():
    t = Safe_Position_Tracker(starting_position=0, modulus=100)
    t.move("R250")  # 250 -> wraps 2 full times, end at 50
    assert t.get_current_position() == 50
    assert t.get_traverse_zero_count() == 2


def test_invalid_instruction_raises():
    t = Safe_Position_Tracker()
    with pytest.raises(ValueError):
        t.move("X10")


def test_instruction_handler():
    # create a temporary input file with a couple of instructions
    import tempfile
    import os

    fd, path = tempfile.mkstemp(text=True)
    try:
        with os.fdopen(fd, "w") as f:
            f.write("R3\nL2\n")

        h = Safe_Instruction_Handler(path)
        assert h.has_instructions()
        assert h.get_next_instruction() == "R3"
        assert h.get_next_instruction() == "L2"
        assert h.get_next_instruction() is None
        assert not h.has_instructions()
    finally:
        os.remove(path)


def test_multiple_wraps_and_land_on_zero():
    # start at 1, modulus 10, move R29: 1+29=30 -> lands at 0
    # traversed_zeros = (1+29)//10 = 3, but final landing should not count, so traverse==2
    t = Safe_Position_Tracker(starting_position=1, modulus=10)
    t.move("R29")
    assert t.get_current_position() == 0
    assert t.get_zero_count() == 1
    assert t.get_traverse_zero_count() == 2
