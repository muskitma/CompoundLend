# test_compoundlend.py
"""
Tests for CompoundLend module.
"""

import unittest
from compoundlend import CompoundLend

class TestCompoundLend(unittest.TestCase):
    """Test cases for CompoundLend class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CompoundLend()
        self.assertIsInstance(instance, CompoundLend)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CompoundLend()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
