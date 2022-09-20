import win32api
import time
import csv
import  pandas as pd
import argparse



#& d:/coding/Projects/RustAimBot/venv/Scripts/python.exe d:/coding/Projects/RustAimBot/main/RecordRecoil.py 1 ak47

parser = argparse.ArgumentParser(description='Videos to images')

parser.add_argument('reset', type=bool, help='reset record')
parser.add_argument('guntype', type=str, help='type of gun')

args = parser.parse_args()
print(args.reset)

LinkToCSV = "RecoilRecordings\\" + args.guntype + ".csv"

if args.reset == True:
    with open(LinkToCSV, 'w', newline='', encoding='utf-8') as f:

        writer = csv.writer(f)
        writer.writerow("xy")
        


input("go: ")
while True:
    pos = win32api.GetCursorPos()
    print(pos)
        # open the file in the write mode
    with open(LinkToCSV, 'a+', newline='', encoding='utf-8') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(pos)
      

    time.sleep(.1)

# find the differance





