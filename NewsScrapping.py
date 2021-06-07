import bs4
import requests


class News:

    def getNewsSoup(self, url):
        agent = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=agent)
        cont = res.content
        soup = bs4.BeautifulSoup(cont, 'html.parser')
        return soup

    def theHindu(self):
        # to get content of frist page
        soup = self.getNewsSoup('https://www.thehindu.com/opinion/editorial/')
        date = []
        pages = []
        titles = []
        list1 = set()
        for i in soup.find_all('div', class_='story-card-news'):
            list1.add(i.h3.a.get('href'))


        # to get content of rest of the page (pagination)
        for i in soup.find_all('li', class_='page-item'):
            if i.a != None:
                pages.append(i.a.get('href'))

        news = set()
        for i in pages:
            soup = self.getNewsSoup(i)

            for i in soup.find_all('div', class_='story-card-news'):
                list1.add(i.h3.a.get('href'))

        # adding all pages content to news array
        for i in list1:
            s = self.getNewsSoup(i)
            date.append(s.find('none').text[1:-1])
            # titles.append(s.find('h2', class_='intro').text)
            print(titles)
            print(date)
            for j in s.find_all('p', class_='drop-caps'):
                news.add(j.text)
                # print(j.text)
        return dict({'paper':'theHindu','titles':titles,'data':list(news), 'dates': date, 'links': list(list1)})

    def hindustanTimes(self):
        soup = self.getNewsSoup('https://www.hindustantimes.com/editorials')
        list = []
        _currentPage = 2
        date = []
        link =[]
        titles =[]
        while (_currentPage < 3):
            for i in soup.find(class_='home').find('section', class_='container').find('section',
                                                                                       class_='mainContainer').find('section', class_='listingPage').find_all('div', class_='cartHolder'):
                link.append(i.get('data-weburl'))
                soup = self.getNewsSoup(i.get('data-weburl'))
                for j in soup.find_all('div', class_='detail'):
                    date.append(soup.find('div', class_= 'dateTime').text[11:-5])
                    # titles.append((soup.find('h1', class_='hdg1').text))
                    print(titles)
                    if j.find_all('p') != []:
                        _article = ""
                        for k in j.find_all('p'):
                            _article += k.text
                        list.append(_article)

            print("----------------------------------------")
            soup = self.getNewsSoup('https://www.hindustantimes.com/editorials/page-' + _currentPage.__str__())
            _currentPage += 1
        ##### RESULT ARE STORED INTO THIS ####
        # for i in list:
        #     print(i)
        return dict({'paper':'hindustanTimes','titles':titles,'data': list, 'dates': date, 'links':link})

    def timesOfIndia(self):
        soup = self.getNewsSoup('https://timesofindia.indiatimes.com/blogs/toi-editorials/')
        list = []
        # _currentPage = "01"
        n = 0;
        link = []
        date =[]
        titles=[]
        while (n < 7):
            for i in soup.find_all('div', class_='detail'):  # getting all page links
                try:
                    page_soup = self.getNewsSoup(i.h2.a.get('href'))
                    link.append(i.h2.a.get('href'))
                    # print(i.h2.a.get('href'))
                except:
                    continue
                date.append(page_soup.find('div', class_='meta').span.text)
                titles.append(page_soup.select_one('div.show-header>h1').text)

                _article = ""
                for j in page_soup.select('div.main-content > p'):
                    _article += j.text
                list.append(_article)
            print(list)
            n += 1
            _currentPage = soup.find('a', class_='next').get('href')  # getting all next page links
            soup = self.getNewsSoup(_currentPage)
            print(_currentPage)
        return dict({'paper':'timeOfIndia','titles':titles,'data': list, 'dates': date, 'links': link})

    def theQuint(self):
        soup = self.getNewsSoup('https://www.thequint.com/voices/opinion')
        list =[]
        date = []
        n=1
        link =[]
        titles = []
        while(n<10):
            for i in soup.find_all('a', class_='_3aBL6'):
                print(i.get('href')+'#read-more')

                new_soup = self.getNewsSoup(i.get('href')+'#read-more')
                link.append(i.get('href')+'#read-more')
                date.append(new_soup.find('time').text)
                titles.append(new_soup.find('h1', class_='headline').text)
                article = ""
                for j in new_soup.select('div.story-element > div > p'):
                    article += j.text
                list.append(article)
            soup = self.getNewsSoup('https://www.thequint.com/voices/opinion/'+str(n))
            n+=1
            return dict({'paper':'theQuint','titles':titles,'data': list, 'dates':date, "links": link})

    def theWire(self):
        soup = self.getNewsSoup('https://m.thewire.in/byline/editorial')
        list = []
        dates = []
        link =[]
        n = 1
        while(n<5):
            for i in soup.find_all('a', class_='featured_stories'):
                # print(i.get('href'))
                page_soup = self.getNewsSoup(i.get('href'))
                article = ""
                link.append(i.get('href'))
                for j in page_soup.select('div.story-detail >p'):
                    article += j.text
                list.append(article)
                dates.append(page_soup.find('div', class_='mark').text[0:12])
                # print(dates)
            # print(list)
            n+=1
            soup = self.getNewsSoup('https://m.thewire.in/byline/editorial/page'+str(n) )
        return dict({'paper':'theWire','data': list, 'dates': dates,'link':link})

    def aspirantworld(self):
        soup = self.getNewsSoup('https://aspirantworld.in/category/editorialanalysis/https://aspirantworld.in/category/editorialanalysis/')
        list = []
        dates = []
        n =2
        while(n<5):
            for i in soup.find_all('h2', class_='entry-title'):
                print(i.a.get('href'))
                new
            soup = self.getNewsSoup('https://aspirantworld.in/category/editorialanalysis/page/'+str(n)+'/')
            n+=1

