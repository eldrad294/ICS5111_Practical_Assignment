from src.visual.visual_handler import visual
#visual().bar_handler()
# visual().boxplot_handler()
# visual().pieplot_handler()
from src.textprocessing.SentimentAnalyzer import SentimentAnalyzer
sa = SentimentAnalyzer()
pred = sa.predict("""This was the worst visit to an urgent care I have ever been to. I waited over three hours for a doctor to see me. Nothing urgent about this place. The doctor finally saw me she said she would write a prescription for me. Again I waited about 20 minutes. Finally I left my "room" and went to the nurses station to get my prescription that was just sitting there. At this point in time after waiting so long all the pharmacies were closed and it was too late ti be filled. Then I got a bill from them for the amount my insurance didn't cover and it was $200. They billed it as an emergency room visit. After arguing with my insurance and then calling Chandler regional  they said all their visits are charged that way. Never mind the bill , the fact that I had to wait to see someone, then when I was finally graced with the presence of some doctor for a mere five minutes only to be given a prescription that I couldn't fill, I called the facility and they were unapologetic. It was ridiculous. They are awful and do not provide quality care and then charge you for their crappy service.""")
print(pred)