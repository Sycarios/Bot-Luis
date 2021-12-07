import unittest
import config

from unittest.mock import patch 
from request_T import response


class FetchTests(unittest.TestCase):
    def test_returns_true_if_url_found(self):
        with patch('requests.get') as mock_request:
            key=config.DefaultConfig.LUIS_API_KEY
            headers = {
                    } 
            params ={
        'query': 'utterance',
        
        'subscription-key': key
    }

            # set a `status_code` attribute on the mock object
            # with value 200
            mock_request.return_value.status_code = 200 # Was the request made succefully ?

            self.assertTrue(response(headers,params))
