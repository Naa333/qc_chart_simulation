from bs4 import BeautifulSoup
import requests
import pandas as pd

# Scrape the CLIA rules from the WSLH website and create a DataFrame
url= "https://wslhpt.org/clia-and-proficiency-testing-changes/"
soup= BeautifulSoup(requests.get(url).content, "html.parser")
table = soup.find("table")
rows = table.find_all("tr")

data = []
for row in rows:
    cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
    data.append(cells)

df = pd.DataFrame(data[1:], columns=data[0])
df.drop(labels= ['WSLH Module', 'Previous WSLH Criteria'], axis=1, inplace=True)
print(df.columns)