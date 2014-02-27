# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#!/usr/bin/python
from __future__ import division
"""Script can be used to calculate the Gini Index of a column in a CSV file.
Classes are strings."""

import fileinput
import csv
from collections import Counter, defaultdict

# <codecell>

(
    CMTE_ID, AMNDT_IND, RPT_TP, TRANSACTION_PGI, IMAGE_NUM, TRANSACTION_TP,
    ENTITY_TP, NAME, CITY, STATE, ZIP_CODE, EMPLOYER, OCCUPATION,
    TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID, CAND_ID, TRAN_ID, FILE_NUM,
    MEMO_CD, MEMO_TEXT, SUB_ID
) = range(22)
CANDIDATES = {
    'P80003338': 'Obama',
    'P80003353': 'Romney',
}

# <codecell>

############### Set up variables
# TODO: declare datastructures
data=defaultdict(list)

# <codecell>

#So I can run in ipython notebook and not always from command line.
if fileinput.input().filename():
    input_file=fileinput.input()
else:
    input_file=open("itpas.txt")
csv_file=csv.reader(input_file,delimiter='|')

# <codecell>

############### Read through files
for row in csv_file:
    candidate_id = row[CAND_ID]
    if candidate_id not in CANDIDATES:
        continue

    candidate_name = CANDIDATES[candidate_id]
    zip_code = row[ZIP_CODE]
    data[candidate_name].append(zip_code)
    
    ###
    # TODO: save information to calculate Gini Index
    ##/

# <codecell>

#Make counter objects for counting zip codes for each candidate 
romney=Counter()
romney.update(data['Romney'])
obama=Counter()
obama.update(data['Obama'])

# <codecell>

#make sure to get all the zip codes
zip_codes=[]
for i in data:
    for z in data[i]:
        if len(z)>=5:
            zip_codes.append(z)
zip_codes=set(zip_codes)

# <codecell>

#Calculate the Gini index for each zip code
ginis=defaultdict(list)
for z in zip_codes:
    r=romney[z]
    o=obama[z]
    total=r+o
    ginis[z].append(1-((r/total)**2+(o/total)**2))

# <codecell>

total_transactions=len(data["Romney"])+len(data["Obama"])

# <codecell>

gini=1-sum([(ginis[i][0]/total_transactions)**2 for i in ginis])

# <codecell>

weighted_gini=defaultdict(list)
for g in ginis:
    weight=(romney[g]+obama[g])/total_transactions
#     print ginis[g][0]
    weighted_gini[g].append(ginis[g][0]*weight)
    

# <codecell>

split_gini=sum([weighted_gini[i][0] for i in weighted_gini])

# <codecell>

# TODO: calculate the values below:
# gini = sum(i for i in data)  current Gini Index using candidate name as the class
# split_gini = 0  weighted average of the Gini Indexes using candidate names, split up by zip code
##/

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini

# <codecell>


# <codecell>


