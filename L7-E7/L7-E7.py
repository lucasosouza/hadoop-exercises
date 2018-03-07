
# coding: utf-8

# In[134]:

get_ipython().system('ls forum_data/')


# In[143]:

#!/usr/bin/python
import sys
import re
import csv

i = 0
first = True
mapper_out = []
with open('forum_data/forum_node.tsv', 'r') as csvfile:
    for data in csv.reader(csvfile, delimiter='\t'):
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
            mapper_out.append("{0}\t{1}".format(word, node))


# In[144]:

mapper_out[:10]


# In[145]:

# sorter
def sorter(data):
    data = [line.split("\t") for line in data]
    sorted_data = sorted(data, key=lambda x: x[0])
    return [('\t').join(line) for line in sorted_data]

sorter_out = sorter(mapper_out)


# In[146]:

r = random.randint(0, len(sorter_out))
sorter_out[r-10:r+10]


# In[147]:

reducer_out = []
reverted_index = set()
total = 0
oldKey = None

for line in sorter_out:
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
            reducer_out.append("{0}\t{1}\t{2}".format(oldKey, total, indexes))
        oldKey = thisKey
        total = 1
        reverted_index = set([thisValue])

    total += 1
    if thisValue not in reverted_index:
        reverted_index.add(thisValue)

    oldKey = thisKey


# In[148]:

reducer_out


# In[ ]:



