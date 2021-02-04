import yfinance as yf
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import locale
import json
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

info_fields = {
    "longName": "Company Name",
    "sector": "Sector",
    "open": "Open",
    "close": "Close",
    "previousClose": "Previous Close",
    "dayLow": "Day Low",
    "dayHigh": "Day High",
    "fiftyTwoWeekHigh": "52 Week High",
    "marketCap": "Market Capitalization",
    "dividendRate": "Divident Rate",
    "volume": "Daily Volume",
    "averageVolume": "Average Daily Volume",
    "averageDailyVolume10Day": "Average 10 Day Daily Volume",
    "forwardPE": "Forward P/E",
    "sharesOutstanding": "Shares Outstanding",
    "floatShares": "Float Shares",
    "sharesShort": "Shares Shorted",
    "shortPercentOfFloat": "Short Percentage of Float"
}

generated_fields = {
    "dailyVolumePercent": "Daily Volume Percentage of Avg. Volume"
}

info_field_type = {
    "longName": "string",
    "sector": "string",
    "open": "currency",
    "close": "currency",
    "previousClose": "currency",
    "dayLow": "currency",
    "dayHigh": "currency",
    "fiftyTwoWeekHigh": "currency",
    "marketCap": "currency",
    "volume": "numeric",
    "averageVolume": "numeric",
    "averageDailyVolume10Day": "",
    "forwardPE": "numeric",
    "sharesOutstanding": "numeric",
    "floatShares": "numeric",
    "sharesShort": "numeric",
    "shortPercentOfFloat": "percent",
    "dailyVolumePercent": "percent"
}


def build_additional_features(ticker_data):
    # Calculate difference in daily volume vs average volume
    if ticker_data.get("volume") is not None and ticker_data.get("averageVolume") is not None:
        ticker_data["dailyVolumePercent"] = 1 + float(ticker_data.get("volume") - ticker_data.get("averageVolume")) / float(ticker_data.get("averageVolume"))
    return ticker_data


def build_yfinance_report(stock):
    ticker = yf.Ticker(stock)

    filtered_info_features = dict((key, ticker.info[key]) for key in ticker.info if key in info_fields)
    data = build_additional_features(filtered_info_features)

    report_dict = dict()
    for field in list(data.keys()):
        value = data.get(field)
        if info_field_type.get(field) == "string":
            report_dict[field] = value
        elif info_field_type.get(field) == "currency":
            report_dict[field] = locale.currency(value, grouping=True)
        elif info_field_type.get(field) == "percent":
            report_dict[field] = "{:.3f} %".format(float(value)*100)
        elif info_field_type.get(field) == "numeric":
            report_dict[field] = "{:,.3f}".format(value)
        else:
            report_dict[field] = str(value)

    return ticker, report_dict




def build_yfinance_report_image(ticker, data):
    field_names_superset = {**info_fields, **generated_fields}
    field_names_subset = dict(
        (key, field_names_superset[key]) for key in field_names_superset if key in data.keys())

    fig = make_subplots(
        rows=3,
        cols=1,
        vertical_spacing=0.03,
        specs=[
            [{"type": "table"}],
            [{"type": "table"}],
            [{"type": "table"}]
        ]
    )
    fig.add_trace(
        go.Table(
            header=dict(
                values=['Information Field', 'Information Value'],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'
            ),
            cells=dict(
                values=[
                    [field_names_subset[field_name] for field_name in field_names_subset],  # 1st column
                    [data[field] for field in field_names_subset]  # 2nd column
                ],
                line_color='darkslategray',
                fill_color='lightcyan',
                align='left'
            )
        ), row=1, col=1)

    institutional_holders = ticker.institutional_holders
    fig.add_trace(
        go.Table(
            header=dict(
                values=["Holder", "Shares", "Value"],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'
            ),
            cells=dict(
                values=[institutional_holders.Holder, institutional_holders.Shares, institutional_holders.Value],
                line_color='darkslategray',
                fill_color='lightcyan',
                align='left'
            )
        ), row=2, col=1)

    recommendations = ticker.recommendations
    recommendations.reset_index(level=0, inplace=True)
    recommendations = recommendations[(recommendations['Date'] > '2021-01-01')]
    fig.add_trace(
        go.Table(
            header=dict(
                values=['Date', 'Firm', 'To Grade', 'From Grade', 'Action'],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'
            ),
            cells=dict(
                values=[recommendations.Date, recommendations.Firm, recommendations['To Grade'],
                        recommendations['From Grade'], recommendations['Action']],
                line_color='darkslategray',
                fill_color='lightcyan',
                align='left'
            )
        ), row=3, col=1)

    fig.update_layout(width=1000)
    return fig


if __name__ == "__main__":
    ticker, report_data = build_yfinance_report("GME")
    fig = build_yfinance_report_image(ticker, report_data)
    fig.show()
