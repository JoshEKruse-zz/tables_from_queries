import csv
import sys

with open(sys.argv[1], newline='') as csvfile:
	reader = list(csv.reader(csvfile))
	tableset = set()

	index = 0
	for row in reader :
		for line in row :
			line = line.split()
			for index, word in enumerate(line) :
				if word == 'FROM' :
					tableset.add( line[ index+1 ] )
				if word == 'JOIN' :
					tableset.add( line[ index+1 ] )
		
	#print( tableset )

	with open('output_tables.csv', 'w', newline='')  as csvfile :
		cw = csv.writer(csvfile)
		for table in list(tableset) :
			cw.writerow( [table] )
