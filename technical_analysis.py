import urllib2
import time

stockToPull = "AAPL"

def pullData(stock):
	try:
		fileLine = stock+'.txt'
		urlToVisit = 'http://ichart.finance.yahoo.com/table.csv?s='+stockToPull
		sourceCode = urllib2.urlopen(urlToVisit).read()
		splitSource = sourceCode.split('\n')
		
		for eachLine in splitSource:
			splitLine = eachLine.split(',')
			if len(splitLine)==7:
				if 'value' not in eachLine:
					saveFile = open(fileLine,'a')
					lineToWrite = eachLine+'\n'
					saveFile.write(lineToWrite)
				
		print 'Pulled',stockToPull
		print 'sleeping'
		time.sleep(5)
					
		
	except Exception,e:
		print 'main loop',str(e)
		
pullData('stockToPulll')
