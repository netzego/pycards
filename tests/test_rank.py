import pytest

from pycards.rank import Rank


def test_init():
    """This is the happy path"""
    rank = Rank("2")
    assert isinstance(rank, Rank)


def test_type_error():
    """Test Rank with a wrong type"""
    with pytest.raises(TypeError):
        _ = Rank(2)  # type: ignore


def test_value_error():
    """Test Rank with an invalid Value"""
    with pytest.raises(ValueError):
        _ = Rank("1")  # type: ignore
