import urllib2
import time

stockToPull = "AAPL"

def pullData(stock):
	try:
		fileLine = stock+'.txt'
		urlToVisit = 'http://ichart.finance.yahoo.com/table.csv?s='+stock+''
		sourceCode = urllib2.urlopen(urlToVisit).read()
		splitSource = sourceCode.split('\n')
		
		for eachLine in SplitSource:
			splitLine = eachLine.split(',')
			if len(splitLine)==6:
				if 'value' not in eachLine:
					saveFile = open(fileLine,'a')
					lineToWrite = eachLine+'\n'
					saveFlie.write(lineToWrite)
				
		print 'Pulled',stockToPull
		print 'sleeping'
		time.sleep(5)
					
		
	except Exception,e:
		print 'main loop',str(e)
		
pullData('stockToPulll')
