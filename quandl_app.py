__author__ = 'Oliver'

import Quandl
mydata = Quandl.get("WIKI/AAPL", authtoken="9Z2BFAy2xsX71vJqVKXS")

# search will return 10 items
# search = https://www.quandl.com/api/v1/datasets.json?query=crude+oil

# return data from API
# url = 'https://www.quandl.com/api/v1/datasets/WIKI/AAPL.csv'

# authorization token

# token = '&auth_token=9Z2BFAy2xsX71vJqVKXS'

print mydata
