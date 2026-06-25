import requests
from bs4 import BeautifulSoup

# Links with the input data for exercise
# The first link is provided by Data Annotation, and the second one by me
# doc_url = 'https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub'
# doc_url = 'https://docs.google.com/document/d/e/2PACX-1vSbI6M_07HZvM09VAswz_gdgUXRy-bfbEiKD6-fbFyccs95iR5JMoamxf3MwbbC4UwUT0pC50QS-Z-y/pub'
# Links with the input data to solve the coding assessment exercise
# The first link is provided by Data Annotation, and the second one by me
# doc_url = 'https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub'
doc_url = 'https://docs.google.com/document/d/e/2PACX-1vQsDL5wy2A6lxStWxf5VEz4U_nGfCuvWCKDfKCgAUE7C3EVa8pupYd0RFOC7MJtq5g8amPJWlF3GWaG/pub'
resp = requests.get(doc_url)

soup = BeautifulSoup(resp.text, 'html.parser')
text = soup.get_text(separator='\n')

table = soup.find('table')

X = []
Y = []
character = []
for row in table.find_all('tr')[1:]:
  cells = row.find_all('td')
  X.append(int(cells[0].get_text(strip=True)))
  Y.append(int(cells[2].get_text(strip=True)))
  character.append(cells[1].get_text(strip=True))

x_max = max(X)
y_max = max(Y)

matrix_msg = [[' ' for _ in range(x_max+1)] for _ in range(y_max+1)]

for i in reversed(range(y_max+1)):
  if i in Y:
    for k in range(len(Y)):
      if Y[k] == i:
        matrix_msg[y_max-i][X[k]] = character[k]

for i in range(y_max+1):
  msg_part = ''
  for j in range(x_max+1):
    msg_part += matrix_msg[i][j]
  print(f'{msg_part}')
