import urllib2
import time

stocksToPull ='AAPL','GOOG','MSFT','CMG','AMZN','EBAY','TSLA'

def pullData(stock):
	try:
		fileLine = stock+'.txt'
		urlToVisit = 'http://ichart.finance.yahoo.com/table.csv?s='+stock
		sourceCode = urllib2.urlopen(urlToVisit).read()
		splitSource = sourceCode.split('\n')
		
		for eachLine in splitSource:
			splitLine = eachLine.split(',')
			if len(splitLine)==7:
				if 'value' not in eachLine:
					saveFile = open(fileLine,'a')
					lineToWrite = eachLine+'\n'
					saveFile.write(lineToWrite)
				
		print 'Pulled',stock
		print 'sleeping'
		time.sleep(1)
					
		
	except Exception,e:
		print 'main loop',str(e)
		
for eachStock in stocksToPull:
	pullData(eachStock)
