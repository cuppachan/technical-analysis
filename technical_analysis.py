import urllib2
import time
import datetime

stocksToPull ='AAPL','GOOG','MSFT','CMG','AMZN','EBAY','TSLA'

def pullData(stock):
	try:
  
		print 'Currently Pullingstock',stock
		print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d' %H:%M:%S'))
		urlToVisit = 'http://ichart.finance.yahoo.com/table.csv?s='+stock
		saveFileLine = stock+'.txt'
                
		try:
			readExistingData = open(saveFileLIne,'r').read()
			splitExisting = readExistingData.split('\n')
			mostRecentLine = splitExisting(-2)
			lastUnix = int(mostRecentLine.split(',')[0])
		except: 
			lastUnix = 0 

	
	
	except Exception,e:
		print 'main loop',str(e)

	for eachStock in stocksToPull:
		pullData(eachStock)
