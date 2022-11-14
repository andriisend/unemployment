
from app.unemployment_json import parsed_response

def test_unemployment_data_fetching():
    assert isinstance(parsed_response, dict)

    assert "name" in parsed_response
    assert "interval" in parsed_response
    assert "unit" in parsed_response
    assert "data" in parsed_response