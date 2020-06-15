import csv
import sys

# open input csv file from system arguments
queries = list( csv.reader( open( sys.argv[ 1 ], newline='' ) ) )
tableset = set() # initialize empty set

# split list of queries into a list of single line
linelist = [ line for row in queries for line in row ]
# split list of lines into a list of single words
wordlist = [ word for line in linelist for word in line.split() ]

# if a 'FROM' or 'JOIN' is found, save next word to the set
for index, word in enumerate( wordlist ) :
	nextword = word.replace( '[', '' ).replace( ']', '' ) # remove '[',']' from strings
	if wordlist[ index-1 ].upper() == 'FROM'  and 'sys.' not in nextword : tableset.add( nextword )
	if wordlist[ index-1 ].upper() == 'JOIN'  and 'sys.' not in nextword : tableset.add( nextword )
	if wordlist[ index-1 ].upper() == 'APPLY' and 'sys.' not in nextword : tableset.add( nextword )

# for every table found, output to csv file
output = csv.writer( open( 'output_tables.csv', 'w', newline='' ) )
for table in list( tableset ) : output.writerow( [ table ] )
