from State.State_info import c_id

import requests
from bs4 import BeautifulSoup

# (part2) Finding all winning candidates name in a state, which constituency they have won and which party they belong to

def won_candidate():
    k = c_id()
    print("WINNING DETAILS OF EACH CONSTITUENCY UNDER THIS STATE:\n")
    for i in k:
        c = []
        link = "https://results.eci.gov.in/PcResultGenJune2024/candidateswise-" + i + ".htm"
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        constituency = soup.find('div', class_='page-title').find_all('span')
        for j in constituency:
            c = list(j)
            c1 = c[0].text.split('-')
            x1 = c1[1]
        candi_name = soup.find('div', class_='nme-prty').find_all('h5')
        for e in candi_name:
            x2 = e.text
        ptty_name = soup.find('div', class_='nme-prty').find_all('h6')
        for f in ptty_name:
            x3 = f.text
        print('Constituency Name:', x1, ",", 'Candidate Name:', x2, ",", 'Party Name:', x3)


