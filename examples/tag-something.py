#!/usr/bin/python3



import json


import jk_treetaggerwrapper


def errorCallback(*argv):
	print(argv)
#


tt = jk_treetaggerwrapper.PoolOfThreadedTreeTaggers("/srv/tree-tagger")
tt.onParsingError.add(errorCallback)


bWithConfidence = False


#result = tt.tagText2("en", "The sun is shining bright today.", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "We experiment with TreeTagger.", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "124 blafasel € {", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "124. blafasel €", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

result = tt.tagText2("en", "Two years ago today, Pope Francis was introduced to the world in a rainy St. Peter's Square, asking for prayers. George Weigel, who was there that night with NBC News, is the author of more than 20 books, including the two-volume biography of John Paul II, Witness to Hope and The End and the Beginning, and, most recently, Evangelical Catholicism and Roman Pilgrimage. He is Distinguished Senior Fellow at theEthics and Public Policy Centerwhere he holds the William E. Simon Chair in Catholic Studies. He talks here with NRO about Pope Francis and the Church. — KJL", bWithConfidence=bWithConfidence)
print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "For more information see http://www.wikipedia.org or send email to foo@bla.com .", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "You can't go there, can you?", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "What do you think: Is this correct?", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "We can; and more.", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "This costs 10 $.", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "This costs 10 €.", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "This costs 10 £.", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "Can't go, can't swim.", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "We see [more].", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "She thought 'mabye it will work'.", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

#result = tt.tagText2("en", "She said \"mabye it will work\".", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))





