import unittest
from src.data.loader import load_data  # Adjust the import based on your actual function names

class TestDataLoader(unittest.TestCase):

    def test_load_data(self):
        # Test loading data from a sample source
        data = load_data('data/raw/sample_data.csv')  # Replace with actual path and filename
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_data_format(self):
        # Test if the loaded data has the expected format
        data = load_data('data/raw/sample_data.csv')  # Replace with actual path and filename
        self.assertIn('column_name', data.columns)  # Replace 'column_name' with an actual column name

if __name__ == '__main__':
    unittest.main()