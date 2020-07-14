import csv
import sys

# open input csv file from system arguments
reader = csv.reader( open( sys.argv[ 1 ], newline='' ) )

# set output file name
try : outputname = sys.argv[ 2 ]
except : outputname = 'output_tables.csv'

output = csv.writer( open( outputname, 'w', newline='' ) )

for line in reader :
        tableset = set() # initialize empty set
        
        wordlist = line[ 0 ].split()

        # if a 'FROM' or 'JOIN' is found, save next word to the set
        for index, word in enumerate( wordlist ) :
                nextword = word.replace( '[', '' ).replace( ']', '' ).lower() # remove '[',']' from strings
                if wordlist[ index-1 ].upper() == 'FROM'     and 'sys.' not in nextword : tableset.add( nextword )
                if wordlist[ index-1 ].upper() == 'JOIN'     and 'sys.' not in nextword : tableset.add( nextword )
                if wordlist[ index-1 ].upper() == 'APPLY'    and 'sys.' not in nextword : tableset.add( nextword )
                if wordlist[ index-1 ].upper() == 'EXEC'     and 'sys.' not in nextword : tableset.add( nextword )
                if wordlist[ index-1 ].upper() == 'EXECUTE'  and 'sys.' not in nextword : tableset.add( nextword )

        # for every table found, output to csv file
        for table in list( tableset ) : output.writerow( [ line[0], line[1], line[2], table ] )
