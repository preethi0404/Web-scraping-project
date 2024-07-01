import requests
from bs4 import BeautifulSoup
response = requests.get('https://results.eci.gov.in/PcResultGenJune2024/index.htm')
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all the party names
# Finding total seats won by a party
# [TO DO]Finding which party won maximum and minimum seats


def party_names():
    party = soup.find('tbody').find_all('tr')
    print("Parties Participated:")
    ind = 1
    for i in party:
        l = list(i)
        print(ind, ".", l[1].text)
        ind += 1

def seats_won():
    party = soup.find('tbody').find_all('tr')
    for i in party:
        l = list(i)
        seats = l[3].a.text
        print(l[1].text, "won", seats, "seats")

def winning1(): # To get link of each party to know their winning candidates details
    l = []
    m = []
    party = soup.find('tbody').find_all('tr')
    print("****************************************************************************")
    party_names()
    print("****************************************************************************")
    for i in party:
        link = i.find('a').attrs['href']
        l.append(link)
        r = list(i)
        m.append(r[1].text)
    k = int(input("Enter the party serial number by verifying above to know the winning candidates result:"))
    print("\nResults:\n")
    print("PARTY NAME:", m[k-1])
    link1 = l[k-1]
    return link1
