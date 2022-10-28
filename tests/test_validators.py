"""Tests of fordev.validators module."""

import unittest

from fordev.validators import raise_for_invalid_uf


class TestValidators(unittest.TestCase):
    """Test Class of fordev.validators module."""
    
    def test_raise_for_invalid_uf(self):
        raise_for_invalid_uf('SP')
        raise_for_invalid_uf('', include_blank=True)
        with self.assertRaises(ValueError):
            raise_for_invalid_uf('HUE')
            raise_for_invalid_uf('', include_blank=False)


if __name__ == '__main__':
    unittest.main()
