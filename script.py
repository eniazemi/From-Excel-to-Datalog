
# Created by Eni Azemi

# Before executing please make sure you have pandas and openpyxl libraries installed.
# If you don't you can install them from terminal (pip install pandas)(pip install openpyxl))
# Make sure that excel files are in the same directory as this script when you execute it
# Make sure that one excel file contains only one table
# Note that the name of the excel file represents the table name in the datalog file
# To avoid any misconceptions please create excel tables in the format that is shown in TestSample folder

import pandas as pd
import csv

namesOfExcelFiles = ["excelTable1", "excelTable2", "excelTable3"]    # Here add all names of excel files that are in the same folder as this script (without prefix .xlsx)

empty = pd.DataFrame()
open("database.dl", "w+")

for i in namesOfExcelFiles:

    df = pd.read_excel(i + ".xlsx")

    df.insert(0, 'start', i + "(")
    df['end'] = ")."

    columns = list(df.columns)
    df = df.astype(str)

    df.insert(0, 'startWith', df['start'] + df[columns[1]])
    df.insert(len(columns) + 1, 'endWith', df[columns[-2]] + df[columns[-1]])

    df.drop(columns=[columns[0], columns[1], columns[-2], columns[-1]], inplace=True)

    df.to_csv("temp.txt", index=False)

    lines = list()
    with open("temp.txt", 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
    lines.pop(0)

    with open("database.dl", 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

