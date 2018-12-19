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

#result = tt.tagText2("en", "Two years ago today, Pope Francis was introduced to the world in a rainy St. Peter's Square, asking for prayers. George Weigel, who was there that night with NBC News, is the author of more than 20 books, including the two-volume biography of John Paul II, Witness to Hope and The End and the Beginning, and, most recently, Evangelical Catholicism and Roman Pilgrimage. He is Distinguished Senior Fellow at theEthics and Public Policy Centerwhere he holds the William E. Simon Chair in Catholic Studies. He talks here with NRO about Pope Francis and the Church. — KJL", bWithConfidence=bWithConfidence)
#print(json.dumps(result, indent="\t"))

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

text = "Government has announced that bulk diesel consumers like railways and state transport corporations have to purchase diesel at market-determined rates, while diesel purchased at fuel outlets will continue to receive subsidy. Assuming diesel subsidy as Rs.10 per litre, let us examine the effects of the recent government order. Mr.Suresh Kumar (not his real name) living in Bandra, Mumbai, maintains three cars, but we will keep the discussion to the SUV that only he uses. Mr.Kumar's SUV gives him 8 km per litre, and on average he drives about 2,000 km every month. He thus purchases 250 litres of subsidized diesel, and utilizes subsidy of Rs.2,500 (250 litres x Rs.10 per litre) every month, or Rs.30,000 annually, for his SUV. This subsidy is borne by tax payers, which include all citizens including the poor, for whom cost of essentials includes indirect taxes. But for Mr.Kumar, the more he drives around, the more diesel he uses, and the more subsidy he utilizes. On the other hand, domestic worker Sonabai living in a Mumbai chawl, has to travel by BEST bus, spending Rs.30 on bus fare every day to and from work. But BEST, which is a bulk consumer of diesel, has to purchase diesel at market rate, and hikes the bus fare so that Sonabai spends Rs.40 every day instead of Rs.30. That is, Sonabai spends Rs.10 more every day (Rs.3,650 more annually), while Mr.Kumar avails of Rs.30,000 subsidy annually. Let us consider the cost to the environment. Noting that whosoever is responsible for consuming diesel, every litre consumed produces exhaust gases that pollute the environment. Whether Mr.Kumar's SUV carries one passenger or more, it consumes essentially the same quantity of diesel and creates the same quantity of exhaust gases. Mr.Kumar's SUV has a seating capacity of 8 passengers, but usually it has only Mr.Kumar himself. Thus, his SUV is used at 1/8 of its carrying capacity, but the diesel consumed and the consequent pollution caused, is no less. As a single individual, he consumes the diesel that 8 could have used. As assumed earlier, his SUV gives 8 km / litre or, put another way, uses 125 ml / km. Thus, if the SUV had 8 passengers, each passenger would be effectively using 125/8=15.6 ml / km. But since Mr.Kumar's SUV provides transportation only for himself, the per capita diesel consumption of his SUV is 125 ml per km, and produces per capita pollution from burning 125 ml / km. On the other hand, consider Sonabai's bus. It has a seating capacity of 52 and a standing passenger capacity of 24, but when she travels it is �rush-hour� both ways, and the bus is packed with about 100 passengers. While it costs essentially the same to operate the bus whether it is empty or full, it is obviously most economical when the bus is full or over-full � occupancy is a major determinant of the economics of a vehicle. However, economics does not trouble Mr.Kumar when he travels alone in his SUV and fills its tank with subsidized diesel using his credit card. The bus consumes about 0.5-litre of diesel per km @ 2-km per litre. Thus, for every kilometre travelled during rush-hours when the bus carries 100 passengers, each passenger effectively uses 500/100=5 ml of diesel, and is responsible for pollution due to burning 5 ml of diesel. That is, the per capita diesel consumption in a bus is 5 ml per km, producing per capita pollution from burning 5 ml per km. Thus, Mr.Kumar ordinarily consumes 125/5=25 times as much diesel as Sonabai, and is responsible for about 25 times as much exhaust gas pollution as her. And, while she effectively subsidizes his diesel consumption, Sonabai is multiple times more eco-friendly than Mr.Kumar. Finally, consider the traffic congestion on the roads. Mr.Kumar's SUV, like any vehicle, occupies road space when it moves or when it is parked on the roadside. It is true that a SUV is about half the size of a BEST bus, and a bus too occupies road space though only when it is on the move, because it is never parked on the roadside. Nevertheless, the per capita usage of road space has arguments similar to those for diesel consumption, and Mr.Kumar uses much more road space, which is a public good, than Mrs.Sonabai who represents the vast majority of urban poor. Thus Sonabai is far less demanding of civic amenities than Mr.Kumar. Thus, on a per capita basis, Mr.Kumar uses more road space, consumes more diesel, and causes more pollution than Sonabai, and even gets his subsidized diesel at her cost. Further, there are many lakhs of people like Sonabai and only many hundreds of people like Mr.Kumar, and it does not require rocket science to understand who subsidizes whom, and who is more responsible for diesel consumption, vehicle exhaust pollution and road congestion. Further, at the hiked bus fare, Mrs.Sonabai spends Rs.40 per day or Rs.1,200 per month on transport, 20% of her Rs.6,000 per month wages. But Mr.Kumar spends Rs.13,000 per month (250 litres@Rs.52/litre) on diesel for his SUV and it is less than 1% of his declared monthly income of several lakhs. This discussion indicates who is most responsible for some of the ills of urban living, and hopefully will serve to urge government to adhere to its own National Transport Policy, which incentivizes affordable public transport (not Volvo AC buses that Sonabai cannot afford) and disincentivizes use of private motor vehicles. Contrary to Mr.Moily's assertion, charging market rates for bulk diesel consumers forces those who are already poor, to pay more for their living. Thus, the policy of the present and previous Union governments is arguably pro-wealthy and effectively anti-poor."

result = tt.tagText2("en", text)
print(json.dumps(result, indent="\t"))

