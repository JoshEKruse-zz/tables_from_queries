import csv
import sys

# open input csv file from system arguments
queries = list( csv.reader( open( sys.argv[ 1 ], newline='' ) ) )
tableset = set() # initialize empty set

# split list of queries into a list of single words
wordlist = [ word for line in [ line for row in queries for line in row ] for word in line.split() ]

# if a 'FROM' or 'JOIN' is found, save next word to the set
for index, word in enumerate( wordlist ) :
	if word == 'FROM' : tableset.add( wordlist[ index+1 ] )
	if word == 'JOIN' : tableset.add( wordlist[ index+1 ] )

# for every table found, output to csv file
output = csv.writer( open( 'output_tables.csv', 'w', newline='' ) )
for table in list( tableset ) : output.writerow( [ table ] )
