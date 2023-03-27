import unittest
import requests
from unittest.mock import patch
from services import get_show_info

class TestGetShowInfo(unittest.TestCase):

    @patch('services.requests.get')
    def test_get_show_info(self, mock_get):
        """Test get_show_info."""
        mock_get.return_value.json.return_value = {'name': 'The Office'}
        show_info = get_show_info('The Office')
        self.assertEqual(show_info, {'name': 'The Office'})
        
        mock_get.assert_called_once_with('https://api.tvmaze.com/search/shows?q=', params={'q': 'The Office'}, timeout=10)
        mock_get.return_value.json.assert_called_once_with()
