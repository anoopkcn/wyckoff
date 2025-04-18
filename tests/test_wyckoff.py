import unittest
from wyckoff import get_wyckoff_dict_from_sgn, get_wyckoff_database


class TestWyckoff(unittest.TestCase):
    def test_get_wyckoff_database(self):
        """Test that we can load the database."""
        database = get_wyckoff_database()
        self.assertIsInstance(database, dict)
        # Check that we have at least the space groups from our sample data
        self.assertIn('1', database)
        self.assertIn('2', database)
        
    def test_get_wyckoff_dict_from_sgn(self):
        """Test that we can get Wyckoff positions for a specific space group."""
        # Space group 1 should have position 1a
        sg1 = get_wyckoff_dict_from_sgn(1)
        self.assertIsInstance(sg1, dict)
        self.assertIn('1a', sg1)
        
        # Space group 2 should have positions 1a through 1h and 2i
        sg2 = get_wyckoff_dict_from_sgn(2)
        self.assertIsInstance(sg2, dict)
        for label in ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h', '2i']:
            self.assertIn(label, sg2)
        
        # Non-existent space group should return empty dict
        sg999 = get_wyckoff_dict_from_sgn(999)
        self.assertEqual(sg999, {})


if __name__ == '__main__':
    unittest.main()