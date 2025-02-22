import unittest
import sys

class TestCompatibility(unittest.TestCase):
    def test_python_version(self):
        # Check if the current Python version is the latest
        self.assertGreaterEqual(sys.version_info, (3, 9))

    def test_ursina_import(self):
        # Check if ursina can be imported
        try:
            import ursina
        except ImportError:
            self.fail("ursina module could not be imported")

    def test_ursinanetworking_import(self):
        # Check if ursinanetworking can be imported
        try:
            import ursinanetworking
        except ImportError:
            self.fail("ursinanetworking module could not be imported")

if __name__ == '__main__':
    unittest.main()
