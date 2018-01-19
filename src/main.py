#from src.visual.visual_handler import visual
# if __name__ == '__main__':
#     visual().bar_handler()
# visual().boxplot_handler()
# visual().pieplot_handler()
from src.visual.csv_plots import csv_plots
#csv_plots().N_of_user_comments_distribution_per_business_states()
#csv_plots().N_of_primary_categories()
#csv_plots().N_of_secondary_categories()
#csv_plots().retrieve_comment_distribution_by_category()
#csv_plots().user_comments_over_time()
#csv_plots().Average_review_length_per_star_rating()
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
#pred = sa.predict(sentence)
#print(pred)
#print(sa.test_set())
#
# ---------------------------------------
#
# from src.db.core import Core
# c = Core()
# city = 'Woodmere'
# business_category = 'Food'
# c.populate_table_business_user_sentiment(state=state)
#
# time = ['Sunday','10:00']
# coordinates = [43.8409,-79.3996]
# c.get_suggested_businesses('Food',coordinates,time,100)
#
# c.get_business_cluster('state')
#
#c.get_business_user_graph(city=city,business_category=business_category)
#
# c.data_mine_top_N_users(N=10,top_trending_word_count=20,pos=True)