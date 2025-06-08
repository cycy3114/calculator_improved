"""Test module for calculator basic operations."""

from calculator import add

def test_add():
    """Test that addition function works correctly."""
    assert add(2, 3) == 5
