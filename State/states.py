import requests
from bs4 import BeautifulSoup


#Finding all the states

def snames():
    response = requests.get('https://results.eci.gov.in/PcResultGenJune2024/index.htm')
    soup = BeautifulSoup(response.text, 'html.parser')
    state = soup.find('div', class_='flter-btns').find_all('option')
    print("State Names:\n")
    ind = 1
    for i in state[1:]:
        print(ind, ".", i.text)
        ind += 1

def sname_id():
    l = []
    m = []
    response = requests.get('https://results.eci.gov.in/PcResultGenJune2024/index.htm')
    soup = BeautifulSoup(response.text, 'html.parser')
    state = soup.find('div', class_='flter-btns').find_all('option')
    snames()
    k = int(input("Enter the state serial number by verifying above to know the details of the state: "))
    for i in state[1:]:
        link = i.attrs['value']
        l.append(link)
        n = i.text
        m.append(n)
    link1 = l[k-1]
    print("\nResults:\n")
    print("STATE NAME:", m[k-1])
    return link1

