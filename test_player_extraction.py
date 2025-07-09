# filepath: /Users/leahwest/Desktop/D3Athletics/test_player_extraction.py
import unittest
from unittest.mock import patch
from bs4 import BeautifulSoup
from playerExtraction import requests

class TestPlayerExtraction(unittest.TestCase):
    @patch('requests.get')


    def test_player_extraction(self, mock_get):
        # Mock the HTTP response
        mock_html = '''
        <html>
            <h3 class="sidearm-roster-player-details">John Doe</h3>
        </html>
        '''
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = mock_html

        # Import your function or code here
        from playerExtraction import requests, BeautifulSoup

        url = "https://cmsathletics.org/sports/softball/roster"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            name_tag = soup.find('h3', class_='sidearm-roster-player-details')

            self.assertIsNotNone(name_tag)
            self.assertEqual(name_tag.get_text(strip=True), "John Doe")
        else:
            self.fail("Failed to retrieve the page.")

if __name__ == "__main__":
    unittest.main()