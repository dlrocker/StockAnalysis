import json
from stockanalysis.report.build_yfinance_report import build_yfinance_report


def get_yfinance_report(ticker):
    try:
        ticker_obj, data = build_yfinance_report(ticker.upper())
    except ValueError:
        msg = {
            "details": "Invalid stock ticker: {}".format(ticker),
            "status": 400,
            "title": "Invalid ticker provide"
        }
        return msg, 400
    except KeyError:
        msg = {
            "details": "Invalid stock ticker: {}".format(ticker),
            "status": 400,
            "title": "Invalid ticker provide"
        }
        return msg, 400
    return json.dumps(data), 200

