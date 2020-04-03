import bs4
import requests

url = "https://www.worldometers.info/coronavirus/#countries"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')

table = soup.find_all('table')[0]


data = []

for tr in table.find_all('tr')[1:-1]:

    name = tr.find_all('td')[0].text.strip()
    total_case = tr.find_all('td')[1].text.strip()
    new_case = tr.find_all('td')[2].text.strip()
    deaths = tr.find_all('td')[3].text.strip()
    data.append((name, total_case, new_case, deaths))

print(*data, sep="\n")