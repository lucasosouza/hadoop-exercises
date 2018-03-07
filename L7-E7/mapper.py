
#!/usr/bin/python
import sys
import re
import csv

first = True
for data in csv.reader(sys.stdin, delimiter='\t'):
    if len(data) != 19:
        continue
    if first:
        first = False
        continue

    # get relevant fields
    node = data[0].strip('"') # remove extra " on node
    body = data[4]    

    # split words on given pattern (all characters escaped)
    # words = re.split('[ \.\,\!\?\:\;\"\(\)\<\>\[\]\#\$\=\-\/]', body)
    words = re.findall('\w+', body)
    words = [w.lower() for w in words if w != '']

    for word in words:
        print("{0}\t{1}".format(word, node))


