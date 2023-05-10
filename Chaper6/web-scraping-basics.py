import requests
from bs4 import BeautifulSoup
import pandas as pd

start_url = 'https://en.wikipedia.org/wiki/Tesla,_Inc.'
downloaded_html = requests.get(start_url)
soup = BeautifulSoup(downloaded_html.text, "html.parser")

# Save a local copy
with open('downloaded.html', 'w') as file:
    file.write(soup.prettify())

# Get the sales and revenue table by index
full_table = soup.select('table.wikitable tbody')[1]

# Extract the table column headings
table_head = full_table.select('tr th')
print('---------------')

# Extract the table column headings and clean up
table_columns = []
for element in table_head:
    column_label = element.get_text(separator=" ", strip=True)
    column_label = column_label.replace(' ', '_')
    table_columns.append(column_label)

# Extract the data table but skipping header row

table_rows = full_table.select('tr')
table_data = []
for index, element in enumerate(table_rows):
    if index > 0:
        row_list = []
        values = element.select('td')
        for value in values:
            row_list.append(value.text.strip())
        table_data.append(row_list)


# Create a Pandas DataFrame
df = pd.DataFrame(table_data, columns=table_columns)
print(df.to_string())





