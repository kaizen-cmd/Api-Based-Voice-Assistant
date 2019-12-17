import requests
import bs4

def readinfo(query):

    res = requests.get("https://www.google.com/search?q={}&oq={}"
                       "&aqs=chrome.0.69i59j0l7.2286j0j7&sourceid=chrome&ie=UTF-8".format(query, query))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    lis = soup.select('div')
    des = lis[25].getText()
    stop = 0
    string = ""
    for i in des:
        if i == ".":
            stop += 1
        if stop == 2:
            break
        string += i
    print(string + ".")