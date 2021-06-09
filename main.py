from Summarization import Summarization
import NewsScrapping
from Database import Database

a = NewsScrapping.News()
b = Summarization()
mongo = Database()




list = a.timesOfIndia()
# list['paper'] = 'theWire'
# mongo.insert(list)
j =0
newList = []
for i in list['data']:
    newList.append(b.summerize(i))

list['data'] = newList
mongo.insert(list)
