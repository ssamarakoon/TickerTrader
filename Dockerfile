FROM python:3.7
RUN pip install -r requirements.txt
RUN TickerTrader.py
