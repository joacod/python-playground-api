import unittest
from flask import Flask
from unittest.mock import patch
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_hello_world(self):
        """Test the hello_world route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), 'Hello, World!')

    def test_lyrics(self):
        """Test the lyrics route."""
        response = self.client.get('/lyrics/Queen/Bohemian Rhapsody')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), 'Lyrics for Bohemian Rhapsody by Queen')

    @patch('app.get_show_info')
    def test_show(self, mock_get_show_info):
        """Test the show route."""
        mock_get_show_info.return_value = {'name': 'The Office'}
        response = self.client.get('/show/The Office')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True).strip(), '{"name":"The Office"}')
        mock_get_show_info.assert_called_once_with('The Office')
