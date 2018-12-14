#!/usr/bin/python3



import json


import jk_treetaggerwrapper



tt = jk_treetaggerwrapper.PoolOfThreadedTreeTaggers("/srv/tree-tagger")




#result = tt.tagText2("en", "The sun is shining bright today.")
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "We experiment with TreeTagger.")
#print(json.dumps(result, indent="\t"))

result = tt.tagText2("en", "124 blafasel € {")
print(json.dumps(result, indent="\t"))

result = tt.tagText2("en", "124. blafasel €")
print(json.dumps(result, indent="\t"))

