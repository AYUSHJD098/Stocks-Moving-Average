#echo "# Stocks-Moving-Average" >> README.md
#git init
#git add README.md
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/AYUSHJD098/Stocks-Moving-Average.git
#git push -u origin mai



# #GOCMB79XBM92IZT7
# from alpha_vantage.timeseries import TimeSeries
# ts = TimeSeries(key='YOUR_API_KEY')
# # Get json object with the intraday data and another with  the call's metadata
# data, meta_data = ts.get_intraday('GOOGL')

import time,requests, json

closed = []
api_key = 'GOCMB79XBM92IZT7'
intervel = '1'+'min'
symbol = 'TSLA' #tesla
function = 'TIME_SERIES_INTRADAY'

headers = f'query?function={function}&symbol={symbol}&interval={intervel}&apikey={api_key}'

response = requests.get(f'https://www.alphavantage.co/' + headers)

json_data = json.loads(response.text)
json_data = json_data['Time Series (1min)']


for data in json_data:
    closed.append(json_data[data]['4. close'])



n =  len(data)
ma = 0

for c in closed:
    ma += float(c)
    print(ma)

moving_average =  ma/n
