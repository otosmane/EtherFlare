# test_etherflare.py
"""
Tests for EtherFlare module.
"""

import unittest
from etherflare import EtherFlare

class TestEtherFlare(unittest.TestCase):
    """Test cases for EtherFlare class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherFlare()
        self.assertIsInstance(instance, EtherFlare)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherFlare()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
