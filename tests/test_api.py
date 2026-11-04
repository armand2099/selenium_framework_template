import pytest
from utils.rest import Rest


#API test URL
API_URL = "https://api.duckduckgo.com/"


@pytest.mark.API
def test_api(logger):

    rest_client = Rest(API_URL)
    response = rest_client.rest_get("Playwright")
    assert response.status_code == 200
    logger.log(f"Status Code: {response.status_code}")

    header = (response.json())['Heading'].lower()
    assert header == "playwright"
    logger.log(f"Header: {header}")