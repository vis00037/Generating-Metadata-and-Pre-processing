# @Author: AUTHOR NAME <GITHUB_USERNAME>
# @Date:   2017-10-19
# @Filename: process.py

import sys
# import libraries

def readConfig(): # add appropriate args
    # code to read the config.json
    return
def readData(): # add appropriate args
    # code to read the input data file
    return 
def generateMetadata(): # add appropriate args
    # code to generate metadata about a data
    return
def dropnull(): # add appropriate args
    # code to drop all the rows having null or NaN in a specific column
    return
def fillnull(): # add appropriate args
    # code to replace null or NaN in a specific column with default values
    return
def normalise(): # add appropriate args
    # code to normalise given column
    return
def sortData(): # add appropriate args
    # code to sort data with respect to given column
    return
def validateDebitCard():  # add appropriate args
    # code to check if a given number is valid debit card number or not
    return 
def removeInvalidDebitCardEntries():  # add appropriate args
    # code to remove all the rows having invalid debit card numbers
    return 
def preprocessData():  # add appropriate args
    # code to call corresponding preprocessing fuctions
    return 
def main(configFile):
    # readConfig
    # readData
    # generateMetadata
    # preprocessData
    # write preprocessed data
    return

###########################################
# DO NOT CHANGE THE CODE WRITTEN BELOW    #
###########################################
if __name__ == '__main__':
    if(len(sys.argv)>1):
        configFile = sys.argv[1]
    else:
        configFile = "config.json"
    main(configFile)
