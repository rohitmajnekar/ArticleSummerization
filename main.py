from Summarization import Summarization
import NewsScrapping
from Database import Database

a = NewsScrapping.News()
    b = Summarization()
mongo = Database()


list = a.theQuint()
# # list['paper'] = 'theWire'
# mongo.insert(list)
# for i in list:
#     b.summerize(i)