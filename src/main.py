from src.visual.visual_handler import visual
# if __name__ == '__main__':
#     visual().bar_handler()
# visual().boxplot_handler()
# visual().pieplot_handler()
#
# ----------------------------------------
#
#from src.textprocessing.SentimentAnalyzer_NB import SentimentAnalyzer
#from src.textprocessing.SentimentAnalyzer_LogisticRegression import SentimentAnalyzer
#from src.textprocessing.SentimentAnalyzer_LDA import SentimentAnalyzer
#from src.textprocessing.SentimentAnalyzer_VADER import SentimentAnalyzer
#sa = SentimentAnalyzer()
#sentence = 'Eh. Unimpressed. Poor waitresses look overworked- we had to ask the manager for refills, got my order wrong twice. Breakfast was a little bland (we got the healthy options & apparently that means no flavor) You have many other better and more delicious options nearby. Sorry morning squeeze, work more on your food and service instead of putting all your effort in a trendy vibe.'
#sentence = 'Pizza here made my night... Good people and great pizza. They can do anything you ask with a great attitude!'
#sentence = "Super good food! My friends and I ordered 2 lbs of shrimp, 2 lbs of crab legs, 2 Cajun fries, sweet potato fries, calamari, and fried catfish! We ate it allllll up. My only concern was that the crabs were a bit difficult to crack but then again I'm used to cracking the Alaskan crab legs. But other than the difficult cracking, the mix of all the seasonings was just a great fusion of flavors to really individualize their seafood from anything I've ever tried. And it was not primetime when we went so service was pretty fast! Hope they're on top of their game when it is busy!"
#sentence = "I waited for my order for over 10 minutes. I ordered two chicken finger kids meals and two adult meals. Had to pull forward and wait another ten minutes for food. When I got home they didn't give me my kids meals."
#sentence = "This place is definitely for hipsters, which me and my boyfriend are not. It is well decorated and feels really 'cool' but the food wasn't anything to rave about. One of those places that people go to just to say they've been there, I guess. I went for dinner, and the dinner menu is actually smaller than their lunch menu? I thought that was weird. All the things that I saw on yelp reviews and I actually wanted to try were not for sale at the time I went. I settled and had curry, it was alright. So they get an okay review, because everything there was okay. Nothing bad, just nothing special. Oh I lied, there was one thing that was pretty great. We paid four bucks for their self-filtered water and it was actually really amazing. LOL. I know that sounds like I totally got ripped off but the water was literally tasteless it felt so weird to drink. Quite the experience. I wouldn't go back for water, but I am glad I tried it once!"
#sentence = "Very unimpressed by their pad Thai.. one of the worst I have had.. lacks flavor and beef tastes like rubber.. I ordered though UberEATS so I don't know if in store it's different but won't be returning for sure!"
#sentence = "I had the pork shank and ate the whole thing. Too bad for my waist line but excellent choice for my belly! it could have fed two and fell off the bone. Delicious."
#sentence = 'Bad bad customer service!!  I was willing to give this place a try. Came in to make some purchases and was completely ignored. Employees were busy conversing among themselves. Waited for about 15minutes for them and was told "some one will be with you shortly" so i just walked out. Best if you take business to Healy or AZ guns!'
#sentence = "Very disappointed! Got the all you can eat crab legs for $50 with my sister in law and they tasted dried out like they were someone else's reheated left overs. Then both of us ended up with very upset stomachs about 30 mins after. So basically we paid $60 each to get diarrhea. Not happy!"
#sentence = "An absolute favourite of mine....I don't understand why this place isn't getting better reviews. I love love Thai food and Pi Toms does it better than any place I have ever been to, hands down. I usually order Pi Tom's own version of Pad Thai....they also have a 'Traditional' version too but I prefer the restaurants own and it is delicious. The ingredients for both dishes are practically the same but Pi Toms dish uses a lighter, more subtle sauce (not ketchup like most traditional pad thai dishes) leaving the flavours of the other ingredients to be fully appreciated. They give pretty decent portion sizes....I rarely finish the entire thing but makes for a great lunch the next day... The mango salad here is to die for! Really fresh ingredients makes this salad extra special and they use a delicious sweet dressing. There are many Pi Toms around Toronto but this one is my personal favourite...its on a nice, fairly quiet street just off Yonge and Wellesley , and has a cute patio complete with romantic lighting, perfect for a dinner date or a relaxing night with a friend. Great service, great place, even better food... what more can you ask for?.."
#sentence = "Very unimpressed by their pad Thai.. one of the worst I have had.. lacks flavor and beef tastes like rubber.. I ordered though UberEATS so I don't know if in store it's different but won't be returning for sure!"
#sentence = "Very disappointed! Got the all you can eat crab legs for $50 with my sister in law and they tasted dried out like they were someone else's reheated left overs. Then both of us ended up with very upset stomachs about 30 mins after. So basically we paid $60 each to get diarrhea. Not happy!"
#sentence = "Not good. My masseuse applied zero pressure. Not worth spending your hard earned cash on."
#sentence = "My expectations were low-I expected good, not great food, reasonably priced.  I made a point of asking for and ordering gluten free foods.  Well the lentil soup was virtually flavorless.  The nachos were nuked in a microwave, half the chips were the crumbs from the bottom of the bag, and the salsa was not spicy but tasted more like marinara.   the \"gluten free\" main course arrived with wheat rather than rice noodles.  I will never return."
# pred = sa.predict(sentence)
# print(pred)
# print(sa.test_set())
#
# ---------------------------------------
#
from src.db.core import Core
c = Core()
state = 'HLD'
business_category = 'Food'
# c.populate_table_business_user_sentiment(state=state)
#
# time = ['Sunday','10:00']
# coordinates = [43.8409,-79.3996]
# c.get_suggested_businesses('Food',coordinates,time,100)
#
# c.get_business_cluster('state')
#
#c.get_business_user_graph(state=state,business_category=business_category)
#
user_ids = ["CxDOIDnH8gp9KXzpBHJYXw",
"bLbSNkLggFnqwNNzzq-Ijw",
"mkbx55W8B8aPLgDqex7qgg",
"6ZC-0LfOAGwaFc5XPke74w",
"3nDUQBjKyVor5wV0reJChg",
"0tvCcnfJnSs55iB6mqPk3w",
"PKEzKWv_FktMm2mGPjwd0Q",
"DK57YibC5ShBmqQl97CKog",
"UYcmGbelzRa0Q6JqzLoguw",
"eZfHm0qI8A_HfvXScwIYsg",
"QJI9OSEn6ujRCtrX06vs1w",
"A0j21z2Q1HGic7jW6e9h7A",
"2EuPAGalYnP7eSxPgFCNDg",
"WJKocp9RE0KatUwh3_DkGg",
"8DGFWco9VeBAxjqsuh1aSw",
"0FMte0z-repSVWSJ_BaQTg",
"U4INQZOPSUaj8hMjLlZ3KA",
"uEvusDwoSymbJJ0auR3muQ",
"RBZ_kMjowV0t6_nv2UKaDQ",
"RQlnSCjuqMnhR3Qk6j4KoA",
"ELcQDlf69kb-ihJfxZyL0A",
"O8eDScRAg6ae0l9Bc24uMA",
"d_TBs6J3twMy9GChqUEXkg",
"WeVkkF5L39888IPPlRhNpg",
"n86B7IkbU20AkxlFX_5aew",
"hWDybu_KvYLSdEFzGrniTw",
"dt9IHwfuZs9D9LOH7gjNew",
"dIIKEfOgo0KqUfGQvGikPg",
"iDlkZO2iILS8Jwfdy7DP9A",
"7Oe6ikklTjVBbEFw9emLcA",
"cMEtAiW60I5wE_vLfTxoJQ",
"HJj82f-csBI7jjgenwqhvw",
"Wc5L6iuvSNF5WGBlqIO8nw",
"pMefTWo6gMdx8WhYSA2u3w",
"QPJJohtGqkMkaN0Gt3TRIg",
"62GNFh5FySkA3MbrQmnqvg",
"4wp4XI9AxKNqJima-xahlg",
"0BBUmH7Krcax1RZgbH4fSA",
"SlgpAnj2gQd44EM_Uq6DkQ",
"zgV0ZroIF956gw4cul8MHA",
"qewG3X2O4X6JKskxyyqFwQ",
"5dKknvq65x-SaluuJjT0Kw",
"N3oNEwh0qgPqPP3Em6wJXw",
"gwIqbXEXijQNgdESVc07hg",
"ffPY_bHX8vLebHu8LBEqfg",
"Ry1O_KXZHGRI8g5zBR3IcQ",
"U5YQX_vMl_xQy8EQDqlNQQ",
"M9rRM6Eo5YbKLKMG5QiIPA",
"rCWrxuRC8_pfagpchtHp6A",
"YRcaNlwQ6XXPFDXWtuMGdA"]
N=20
for user_id in user_ids:
    c.get_top_N_trending_words(user_id=user_id, N=N)