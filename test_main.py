"""Tests for main.py"""
import pytest
from calculator.calculator import Calculator

def test_main_import():
    """Test that Calculator can be imported from main"""
    from main import Calculator as MainCalculator
    assert MainCalculator == Calculator
