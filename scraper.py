import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/#countries"

def scraper(state):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="main_table_countries_today")
    content = results.find_all('td')

    countries = []
    total_cases = []
    new_cases = []
    total_deaths = []
    new_deaths = []

    i=1
    start = False
    for entry in content:
        if str(entry.text.strip())=="USA":
            start= True
            i=1
            #print(entry.text.strip())
        if i%19 == 1 and start==True:
            countries.append(entry.text.strip())
        if i%19 == 2 and start==True:
            total_cases.append(entry.text.strip())
        if i%19 == 3 and start==True:
            new_cases.append(entry.text.strip())
        if i%19 == 4 and start==True:
            total_deaths.append(entry.text.strip())
        if i%19 == 5 and start==True:
            new_deaths.append(entry.text.strip())    
        i+=1
    column_names = ["Country","Total Cases","New Cases","Total Deaths","New Deaths"]
    covid19_table ={
        "coloumns": column_names,
        "country": countries,
        "total_cases": total_cases,
        "new_cases": new_cases,
        "total_deaths": total_deaths,
    }

    index=0
    for country in countries:
        if country==state:
            return (f"""
            Find stats for {state}

            Country: {countries[index]}
            Total Cases: {total_cases[index]}
            New Cases: {new_cases[index]}
            Total Deaths: {total_deaths[index]}
            New Deaths: {new_deaths[index]}
            
            """)
        index+=1
    pass


