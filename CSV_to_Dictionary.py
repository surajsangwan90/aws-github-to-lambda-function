import csv
import json
def lambda_handler(event,context):
    csvFilePath = r'C:\Users\nitil\Downloads\Eventswedo.csv'
    jsonFilePath = 'CSV_convertedfile.json'

    #Create a Blank Dictionary, later we will save the date into this dictionary
    data={}
    with open(csvFilePath, encoding='utf-8') as csvfile:
        csvreader=csv.DictReader(csvfile) # DictReader will read the CSV File and convert into dictionary object
        print(type(csvreader))
        #iterate each row from the dictionary
        for rows in csvreader:
            # Select category as primary key
            key=rows['Category']
    #         print(key)
        # save the each data of row  in blank dictionary
            data[key]=rows
    #         print(data[key])
    # convert Dictionary file into JSON, and save the file.
    with open(jsonFilePath,"w") as outfile:
        json.dump(data,outfile,indent=4)
        return json.dump(data,outfile,indent=4)
lambda_handler()