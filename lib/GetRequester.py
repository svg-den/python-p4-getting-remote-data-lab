import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to the URL and returns the response body as text.
        If the request is unsuccessful or raises an error, None is returned.
        """
        response = requests.get(self.url)
        return response.content
   
    def load_json(self):
        """
        Uses get_response_body to get the response in text format,
        then attempts to convert and return it as a Python dictionary or list.
        Returns None if conversion fails or response is invalid.
        """
        response_body = self.get_response_body()
        if response_body:
            try:
                return json.loads(response_body)
            except json.JSONDecodeError as e:
                print(f"JSON decoding error: {e}")
        return None
