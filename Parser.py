from bs4 import BeautifulSoup
from Client import Client
from geopy import distance


def parsingFilesToClients(files):
    clients = []
    index = 0
    for file in files:
        with(open('C:\\orders\\' + file, 'rb')) as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            time = soup.find_all('span',
                                 style="font-family: 'Times New Roman',times,serif;"
                                       " color: #000000;"
                                       " font-size: 10px; line-height: 1;"
                                       " *line-height: normal;"
                                       " font-weight: bold;")[2].text
            items = soup.find_all('span',
                                  style="font-family: 'Times New Roman',times,serif; "
                                        "color: #000000; "
                                        "font-size: 10px; "
                                        "line-height: 1; "
                                        "*line-height: normal;")
            if items[11].text == 'Штрихкод':
                phone = items[7].text
            else:
                phone = items[8].text
            client = Client(items[6].text, phone,
                            items[5].text, (items[3].text, items[4].text), time, index)
            clients.append(client)
            index += 1
    return clients


"""
def searchAllRout(indexInClients, allRout, rout):
    if len(indexInClients) != 0:
        for index in indexInClients:
            tmpIndexInClients = copy(indexInClients)
            rout.append(index)
            tmpIndexInClients.remove(index)
            searchAllRout(tmpIndexInClients, allRout, copy(rout))
            rout.remove(index)
    else:
        allRout.append(rout)


def searchKm(rout, clients):
    resultClients = []
    for rou in rout:
        for client in clients:
            if client.index == rou:
                resultClients.append(client)
    startPoint = (53.154340, 24.457668)
    disKm = distance(startPoint, resultClients[0].point).km
    flag = 0
    while flag < (len(resultClients) - 1):
        disKm += distance(resultClients[flag].point, resultClients[flag + 1].point).km
        flag += 1
    return [disKm, resultClients]


def sortClients(clients):
    indexInClients = []
    for client in clients:
        indexInClients.append(client.index)
    allRout = []
    rout = []
    searchAllRout(indexInClients, allRout, rout)
    allKmRout = []
    for rout in allRout:
        kmRout = searchKm(rout, clients)
        allKmRout.append(kmRout)
    allKmRout.sort()
    print(allRout[0])
    print(allRout[1])
    print(allRout[2])
    print(allRout[3])
"""


def initDistance(clients):
    startPoint = []
    for clientIn in clients:
        startPoint.append(clientIn)
        for clientTo in clients:
            if clientIn != clientTo:
                dis = distance.distance(clientIn.point, clientTo.point).km
                clientIn.distanceToPoint.append([dis, clientIn])
    startPoint.sort()
    return startPoint
