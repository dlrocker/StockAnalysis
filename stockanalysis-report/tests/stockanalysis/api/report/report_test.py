import pytest
import json
import os

def filter_response(expected_data: dict, actual_data: dict):
    """
    Helper function that filters the actual data based on the keys of the expected data
    :param expected_data: Dictionary containing the expected key-value pairs of a API response
    :param actual_data: Dictionary containing the actual key-value pairs of a API response that need to be reduced
    :return: Updated dictionary of the actual response
    """
    expected_data_keys = list(expected_data.keys())
    return dict((key, actual_data.get(key)) for key in expected_data_keys)


@pytest.mark.usefixtures("client")
def test_get_report_valid_ticker(client):
    """
    Will use GME (GameStop) as a valid ticker. Sample return:
    {
      "sector": "Consumer Cyclical",
      "previousClose": "$193.60",
      "averageDailyVolume10Day": "116167342",
      "open": "$379.71",
      "dividendRate": "None",
      "marketCap": "$22,667,776,000.00",
      "averageVolume": "27,457,036.000",
      "dayLow": "$250.00",
      "volume": "50,397,132.000",
      "fiftyTwoWeekHigh": "$483.00",
      "forwardPE": "-1,911.765",
      "dayHigh": "$413.98",
      "longName": "GameStop Corp.",
      "sharesOutstanding": "69,747,000.000",
      "sharesShort": "61,782,730.000",
      "floatShares": "46,888,789.000",
      "shortPercentOfFloat": "226.420 %",
      "dailyVolumePercent": "183.549 %"
    }

    Note: Due to many values changing over time, we will only validate that a few fields are what we expect.
    """
    response = client.get("/api/v1/report/?ticker=GME")
    actual_data = json.loads(response.get_data(as_text=True))
    expected_data = {
        "longName": "GameStop Corp.",
        "sector": "Consumer Cyclical",
        "dividendRate": "None",
        "sharesOutstanding": "69,747,000.000"
    }
    actual_data_filtered = filter_response(expected_data, actual_data)
    assert response.status_code == 200
    assert expected_data == actual_data_filtered


@pytest.mark.usefixtures("client")
def test_get_report_default_ticker(client):
    """
    Validate that by default the API returns information for GME (GameStop)
    """
    response = client.get("/api/v1/report/")
    actual_data = json.loads(response.get_data(as_text=True))
    expected_data = {
        "longName": "GameStop Corp.",
        "sector": "Consumer Cyclical"
    }
    actual_data_filtered = filter_response(expected_data, actual_data)
    assert response.status_code == 200
    assert expected_data == actual_data_filtered


@pytest.mark.usefixtures("client")
def test_get_report_invalid_ticker(client):
    response = client.get("/api/v1/report/?ticker=FAKETICKER")
    actual_data = json.loads(response.get_data(as_text=True))
    expected_data = {
        "details": "Invalid stock ticker: FAKETICKER",
        "status": 400,
        "title": "Invalid ticker provided"
    }
    assert response.status_code == 400
    assert expected_data == actual_data


@pytest.mark.usefixtures("client")
def test_get_report_invalid_query_option(client):
    response = client.get("/api/v1/report/?option=test")
    actual_data = json.loads(response.get_data(as_text=True))
    expected_data = {
        "detail": "Missing query parameter 'ticker'",
        "status": 400,
        "title": "Bad Request",
        "type": "about:blank"
    }
    assert response.status_code == 400
    assert expected_data == actual_data


@pytest.mark.usefixtures("client")
def test_get_report_ticker_as_number(client):
    response = client.get("/api/v1/report/?ticker=1")
    actual_data = json.loads(response.get_data(as_text=True))
    expected_data = {
        "details": "Invalid stock ticker: 1",
        "status": 400,
        "title": "Invalid ticker provided"
    }
    assert response.status_code == 400
    assert expected_data == actual_data


@pytest.mark.usefixtures("client")
def test_get_yfinance_report_image(client):
    response = client.get("/api/v1/report/image/?ticker=GME")
    with open("report.png", "wb") as f:
        f.write(response.data)
    assert response.status_code == 200

    # Verify it is actually a png by checking first line of file for \x89PNG
    with open("report.png", "rb") as f:
        content = f.readline()
    assert content.startswith(b'\x89PNG')

    # Cleanup
    os.remove("report.png")
