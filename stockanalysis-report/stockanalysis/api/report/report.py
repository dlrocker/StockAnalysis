import json
import io
import plotly
from stockanalysis.report.build_yfinance_report import build_yfinance_report, build_yfinance_report_image
from flask import send_file

def get_yfinance_report(ticker):
    try:
        ticker_obj, data = build_yfinance_report(ticker.upper())
    except ValueError:
        msg = {
            "details": "Invalid stock ticker: {}".format(ticker),
            "status": 400,
            "title": "Invalid ticker provided"
        }
        return msg, 400
    except KeyError:
        msg = {
            "details": "Invalid stock ticker: {}".format(ticker),
            "status": 400,
            "title": "Invalid ticker provided"
        }
        return msg, 400
    return data, 200


def get_yfinance_report_image(ticker):
    try:
        ticker_obj, data = build_yfinance_report(ticker.upper())
    except ValueError:
        msg = {
            "details": "Invalid stock ticker: {}".format(ticker),
            "status": 400,
            "title": "Invalid ticker provided"
        }
        return msg, 400
    except KeyError:
        msg = {
            "details": "Invalid stock ticker: {}".format(ticker),
            "status": 400,
            "title": "Invalid ticker provided"
        }
        return msg, 400

    fig = build_yfinance_report_image(ticker_obj, data)
    fig.write_image("report.png", scale=1.0, width=5000, height=10000)
    return send_file("report.png", mimetype='image/png'), 200
