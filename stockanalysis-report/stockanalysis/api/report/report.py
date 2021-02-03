from stockanalysis.report.build_yfinance_report import build_yfinance_report, build_yfinance_report_image
from flask import send_file
import io


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

    # Create file object to stream the data to the API caller
    file_object = io.BytesIO()

    # write PNG into the file-object
    fig.write_image(file_object, scale=1, height=1500)

    # move to beginning of file so `send_file()` it will read from start
    file_object.seek(0)

    return send_file(file_object, mimetype='image/png')
