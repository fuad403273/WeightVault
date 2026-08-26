# test_weightvault.py
"""
Tests for WeightVault module.
"""

import unittest
from weightvault import WeightVault

class TestWeightVault(unittest.TestCase):
    """Test cases for WeightVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WeightVault()
        self.assertIsInstance(instance, WeightVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WeightVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
