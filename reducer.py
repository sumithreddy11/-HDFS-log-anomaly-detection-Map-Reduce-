%%writefile reducer.py
import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    try:
        window, event, count = line.strip().split('\t')
        counts[(window, event)] += int(count)
    except:
        continue

for (window, event), value in counts.items():
    print(f"{window},{event},{value}")
