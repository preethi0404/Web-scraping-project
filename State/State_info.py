from State import states

import requests
from bs4 import BeautifulSoup



#Finding total number of constituencies in a state
#Finding all the constituecy names in a state
#Finding all winning parties and how many seats they have won
#(part1) Finding all winning candidate name, which constituency they have won and which party they belong to

def total_seats():
    link = "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-" + states.sname_id() + ".htm"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    party = soup.find('tfoot').find_all('th')
    k = party[1].text
    print("Total seats:", k)

def constituency_name():
    link = "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-" + states.sname_id() + ".htm"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('select', class_= 'custom-select').find_all('option')
    print("NAMES OF ALL CONSTITUENCIES:\n")
    ind = 1
    for i in name[1:]:
        k = i.text.split("-")
        print(ind, ".", k[0])
        ind += 1

def winning_party():
    link = "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-" + states.sname_id() + ".htm"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    l=[]
    print("All winning parties in this state and seats won by them:\n")
    party = soup.find('tbody').find_all('tr')
    for i in party:
        l = list(i)
        name = l[1].text
        seats = l[3].a.text
        print(f"{name} won {seats} seats")


def c_id():
    link = "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-" + states.sname_id() + ".htm"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    m = []
    name = soup.find('select', class_='custom-select').find_all('option')
    for i in name[1:]:
        k = i.attrs['value']
        m.append(k)
    return m

