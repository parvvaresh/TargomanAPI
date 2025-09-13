import pytest
import requests
from unittest.mock import patch
import json

from api import Translate, translate


# Mock response data
mock_response_fa_en = {
    "result": {
        "tr": {
            "base": [
                [0, "Hello"]
            ]
        }
    }
}

mock_response_en_fa = {
    "result": {
        "tr": {
            "base": [
                [0, "سلام"]
            ]
        }
    }
}


@patch("requests.post")
def test_translate_fa_to_en(mock_post):
    # Mock the requests.post response
    mock_post.return_value.text = json.dumps(mock_response_fa_en)

    result = Translate("سلام", "fa", "en")
    assert result == "Hello"


@patch("requests.post")
def test_translate_en_to_fa(mock_post):
    mock_post.return_value.text = json.dumps(mock_response_en_fa)

    result = Translate("Hello", "en", "fa")
    assert result == "سلام"
