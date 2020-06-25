import csv
import sys

# open input csv file from system arguments
queries = list( csv.reader( open( sys.argv[ 1 ], newline='' ) ) )

# set output file name
try : outputname = sys.argv[ 2 ]
except : outputname = 'output_tables.csv'

tableset = set() # initialize empty set

# split list of queries into a list of single line
linelist = [ line for row in queries for line in row ]
# split list of lines into a list of single words
wordlist = [ word for line in linelist for word in line.split() ]

# if a 'FROM' or 'JOIN' is found, save next word to the set
for index, word in enumerate( wordlist ) :
	nextword = word.replace( '[', '' ).replace( ']', '' ) # remove '[',']' from strings
	if wordlist[ index-1 ].upper() == 'FROM'     and 'sys.' not in nextword : tableset.add( nextword )
	if wordlist[ index-1 ].upper() == 'JOIN'     and 'sys.' not in nextword : tableset.add( nextword )
	if wordlist[ index-1 ].upper() == 'APPLY'    and 'sys.' not in nextword : tableset.add( nextword )
	if wordlist[ index-1 ].upper() == 'EXEC'     and 'sys.' not in nextword : tableset.add( nextword )
	if wordlist[ index-1 ].upper() == 'EXECUTE'  and 'sys.' not in nextword : tableset.add( nextword )

# for every table found, output to csv file
output = csv.writer( open( outputname, 'w', newline='' ) )
for table in list( tableset ) : output.writerow( [ table ] )

print(len(tableset))
