__author__ = 'Oliver'

import Quandl
mydata = Quandl.get("WIKI/AAPL", authtoken="9Z2BFAy2xsX71vJqVKXS")

print mydata
