#!/usr/bin/python3

import pandas as pd

def main():
    # define the name of our xls file
    excel_file = 'switches.xlsx'

    # create a DataFrame (DF) object
    switches = pd.read_excel(excel_file)

    # show the first ten rows of our DF
    print(switches.head(10))

    # Choose the first column "Title" as
    # index (index=0)
    # movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    # print(movies_sheet1.head())

    # grab the next 2 sheets as well
    # movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    #print(movies_sheet2.head())

    # movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    # print(movies_sheet3.head())

    # combine all DFs into a single DF called movies
    # movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

    # number of rows and columns (r, c)
    print(switches.shape)

    # sort DataFrame based on Gross Earnings
    sorted_by_driver = switches.sort_values(["driver"], ascending=False)

    # Data is sorted by values in a column
    # passing the 10 values to head returns the top 10 not the default 5
    print(sorted_by_driver.head(10))
    
    ## create a python dictionary
    driverdict = switches.to_dict(orient='records')
    print(driverdict)

    # simple loop for each line in dictionary
    for switch in driverdict:
       print(f"The driver of switch {switch['ip']} is {switch['driver']}.")

if __name__ == "__main__":
    main()

