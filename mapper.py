%%writefile mapper.py
import sys
import csv

reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        line_id = int(row['LineId'])
        event = row['EventId']

        window_id = line_id // 50

        print(f"{window_id}\t{event}\t1")

    except:
        continue
