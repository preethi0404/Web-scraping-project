from PC.parties import winning1

import requests
from bs4 import BeautifulSoup

# Finding all winning candidates of a party
# Finding all the constituencies won by the winning candidates of a party
# Finding the votes got by the winning candidates



def candidates_won():
    link = "https://results.eci.gov.in/PcResultGenJune2024/" + winning1()
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    party = soup.find('tbody').find_all('tr')
    ind = 1
    print("WINNING CANDIDATES OF THE PARTY:\n")
    for i in party:
        l = list(i)
        name = l[5].text
        print(f"{ind} . {name}")
        ind += 1

def winning_constitutency():
    link = "https://results.eci.gov.in/PcResultGenJune2024/" + winning1()
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    party = soup.find('tbody').find_all('tr')
    print("CONSTITUENCIES WON BY THE PARTY:\n")
    for i in party:
        l = list(i)
        place = l[3].text
        name = l[5].text
        print(f"{name} won at {place[:-3]}")

def votes_won():
    link = "https://results.eci.gov.in/PcResultGenJune2024/" + winning1()
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    party = soup.find('tbody').find_all('tr')
    print("VOTES BY WON BY THE WINNING CANDIDATE OF THE PARTY:\n")
    for i in party:
        l = list(i)
        name = l[5].text
        votes = l[7].text
        print(f"{name} won by getting {votes} votes")
