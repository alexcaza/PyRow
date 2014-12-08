#!/usr/bin/env python

import argparse
import csv # Built in module to handle CSV files
from sys import argv # Argv to handle command line arguments
from collections import defaultdict # Robust dictionary handler

def initialLoop(originalFile, formattedFile):
		outputFile = open(formattedFile, 'w') # Prepare output file to write to.
										# Does not need to exist

		columns = defaultdict(list) # Define expandable dictionary

		with open(originalFile) as csvFile: # Open CSV file as csvFile
			reader = csv.DictReader(csvFile) # read rows into a dictionary format
			for row in reader: # read a row as {column1: value1, column2: value2,...}
				for (key,value) in row.items(): # go over each column name and value
					columns[key].append(value) # append the value into the appropriate list

		def formatListLoop(): # Throwing while loop into function to scope variables
				true = True
				i = 0
				while true:
						outputFile.write(columns['Keyword'][i]+" - "+columns[' Monthly Searches'][i]+"\\mo"+" @"+columns[' CPC'][i]+"\n")
						i += 1
						if i == len(columns['Keyword']):
								true = False
		formatListLoop() # Call loop that formats dictionaries into strings

		outputFile.close() # Close file after using it

def main():
		parser = argparse.ArgumentParser(description="Pass the script the original CSV file to format")
		parser.add_argument('-o', '--original-file', dest="originalFile", type=str, required=True, help='The original File you want to format')
		parser.add_argument('-d', '--destination-file', dest="formattedFile", type=str, required=True, help='The name of the formatted output file you want to create or use')
		args = parser.parse_args()

		initialLoop(args.originalFile, args.formattedFile)

if __name__ == '__main__':
		main()
		
