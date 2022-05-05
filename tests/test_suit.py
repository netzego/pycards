import pytest

from pycards.suit import Suit


def test_init():
    """This is the happy path"""
    rank = Suit("clubs")
    assert isinstance(rank, Suit)


def test_type_error():
    """Test Suit with a wrong type"""
    with pytest.raises(TypeError):
        _ = Suit(42)  # type: ignore


def test_value_error():
    """Test Suit with an invalid Value"""
    with pytest.raises(ValueError):
        _ = Suit("wrong")  # type: ignore
