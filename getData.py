import COVID19Py
covid19 = COVID19Py.COVID19()
locations = covid19.getLocations()

data = []
for i in range(len(locations)):
    country = locations[i]['country']
    confirmed = locations[i]['latest']['confirmed']
    deaths = locations[i]['latest']['deaths']
    data.append((country, confirmed, deaths))

print(data)
