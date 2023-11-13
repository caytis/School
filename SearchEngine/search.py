import pprint
import urllib.request

class HayStack:
    def __init__(self, url, numpages=3):
        self.url = url
        self.numpages = numpages
        self.graph = self.makeGraph()
        self.compute_ranks(self.graph)
        self.index = self.createIndex(self.graph.keys())

    def makeGraph(self):
        pagesLeft = self.numpages
        graph = dict()
        urllineup = list()
        urllineup.append(self.url)
        while urllineup:
            url = urllineup[0]
            urllineup.remove(url)
            pagesLeft -= 1
            if url in graph:
                continue
            req = urllib.request.Request(url, headers={'User-Agent' : 'XY'})
            response = urllib.request.urlopen(req)
            html = response.read().decode().lower()
            links = set(x[1].split("\"")[0] for x in [x[1].split("\"") for x in [x.split("href") for x in html.split("<a")] if len(x) >= 2] if len(x) >= 2)
            graph[url] = links
            if pagesLeft:
                for link in links:
                    urllineup.append(link)
        return graph

    def createIndex(self, urls):
        index = dict()
        for url in urls:
            req = urllib.request.Request(url, headers={'User-Agent' : 'XY'})
            response = urllib.request.urlopen(req)
            file = response.read().decode()
            byehtml = " ".join([x[1] for x in [x.split(">") for x in file.split("<")] if len(x) >= 2]).split()
            wordsextra = list(x.strip('!\"#$%&0123456789()*+,-/:;<=>?@\\^_`{|}~ \n.[]') for x in byehtml)
            for item in wordsextra:
                item = item.lower()
                if item in index and url not in index[item]:
                    index[item].append(url)
                    continue
                testitem = item.replace('\'', 'a')
                if testitem.isalpha() and item not in index:
                    index[item] = [url]
        return index

    def lookup(self, word):
        return self.index[word.lower()]

    def compute_ranks(self, graph):
        d = 0.85     # probability that surfer will bail
        numloops = 10

        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages

        for _ in range(0, numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d) / npages
                for url in graph:   
                    if page in graph[url]:  # this url links to page
                        newrank += d*ranks[url]/len(graph[url])
                newranks[page] = newrank
            ranks = newranks
        self.ranks = ranks
    
if __name__ == '__main__':
    engine = HayStack('http://roversgame.net/cs3270/page1.html',4)
    for w in ['pages','links','you','have','I']:
        print(w)
        pprint.pprint(engine.lookup(w))
    print()
    print('index:')
    pprint.pprint(engine.index)
    print()
    print('graph:')
    pprint.pprint(engine.graph)
    print()
    print('ranks:')
    pprint.pprint({page:round(rank,4) for page,rank in engine.ranks.items()})