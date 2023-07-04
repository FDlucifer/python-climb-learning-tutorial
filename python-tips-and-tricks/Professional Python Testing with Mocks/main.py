import requests
import unittest
from unittest.mock import patch, Mock


def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()


class TestUserData(unittest.TestCase):
    @patch("requests.get")
    def test_get_user_data(self, mock_get):
        mock_response = Mock()
        response_dist = {"name": "john", "email": "john@example.com"}
        mock_response.json.return_value = response_dist

        mock_get.return_value = mock_response

        user_data = get_user_data(1)
        mock_get.assert_called_wiith("https://api.example.com/users/1")
        self.assertEqual(user_data, response_dist)


if __name__ == "__main__":
    unittest.main()
