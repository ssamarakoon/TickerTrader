FROM python:3.7
COPY . /app
RUN pip install ta urllib pandas matplotlib
CMD ["python", "TickerTrader.py"]
