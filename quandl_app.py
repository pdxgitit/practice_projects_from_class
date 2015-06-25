__author__ = 'Oliver'

import Quandl
mydata = Quandl.get("FRED/GDP.csv", authtoken="9Z2BFAy2xsX71vJqVKXS")


print mydata
