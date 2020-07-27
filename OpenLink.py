import requests
from bs4 import BeautifulSoup
import webbrowser

if __name__ == "__main__":

    #health news from library
    for j in range(128,140):
        baseurl = "https://wellness-connect.net/health_topic_detail.php?id="
        url = baseurl + str(j)
        webbrowser.open(url,new=0,autoraise=False)


    """
    #health article
    k = 50
    j = 1
    while j < 3:
        url = "https://wellness-connect.net/health_articles.php?page="+str(k)
        baseurl = "https://wellness-connect.net/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        for i in soup.findAll('a', href=True):
            if i.parent.name == 'h4':
                url2 = baseurl + i['href']
                webbrowser.open(url2, new=0, autoraise=False)
                print(baseurl + i['href'])
        k += 1
        j += 1
    print(k)
    """
    """
    url = "https://wellness-connect.net/health_articles.php?page=27"
    baseurl = "https://wellness-connect.net/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    for i in soup.findAll('a',href=True):
        if i.parent.name == 'h4':
            url2 = baseurl+i['href']
            webbrowser.open(url2,new=0,autoraise=False)
            print(baseurl+i['href'])"""
    #div_level_1 = soup.find('div',class_='row image-service-box')
    #print(div_level_1)
    #div_level_2 = div_level_1.find_all('div',class_='col-md-9')

    #print(div_level_2)
    #print(soup.find_all('div',class_='col-md-9'))