
#!/usr/bin/python
import sys

reverted_index = set()
total = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
        
    thisKey, thisValue = data_mapped
    thisValue = int(thisValue)

    if oldKey and oldKey != thisKey:
        if oldKey == 'fantastic' or oldKey == 'fantastically':
            indexes = list(reverted_index)
            indexes.sort()
            print("{0}\t{1}\t{2}".format(oldKey, total, indexes))
        oldKey = thisKey
        total = 1
        reverted_index = set([thisValue])

    total += 1
    if thisValue not in reverted_index:
        reverted_index.add(thisValue)

    oldKey = thisKey
