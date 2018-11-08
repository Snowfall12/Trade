'''
Created on 8 nov. 2018

@author: loicb
'''

import quandl as ql
import sys

def GetData(Ticker,StartDate=None,EndDate=None):
    '''
    This functions retrieves the data of the desired ticker, start and enddate are in option
    
    '''
    # Setting up the API key
    ql.ApiConfig.api_key="Ysf-yLKC5NB1CMgcSUf6"
    
    # Try to retrieve the data
    try:
        Data=ql.get(Ticker,start_date=StartDate,end_date=EndDate)
    
    # If there is an error, leave a message and end the process
    except:
        return "There was an error with the ticker " + str(Ticker) + "/n make sure you entered a valid ticker"
        sys.exit()
        
    # Returns the data unless there was an error
    return Data