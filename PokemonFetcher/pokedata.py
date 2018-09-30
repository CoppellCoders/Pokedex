
import requests


from bs4 import BeautifulSoup

url = "https://pokemondb.net/pokedex/stats/height-weight"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)

pokeList = open("pokemon.txt", "r")
height = open("height.txt", "w",encoding="utf-8")
weight = open("weight.txt", "w")
descrip = open("descrip.txt", "w")
name_box = soup.findAll('tr')
printcounter =0
temp = "000"
numberCount = 1
arrayList = []
for name_textlist in name_box:
    numberCount+=1
    poke = name_textlist.findAll('td', attrs={'class': 'cell-num'})
    if(numberCount==187):
        break
    printcounter=0
    for lista in poke:
        printcounter+=1
        name = lista.text.strip()
        if printcounter == 1:
            temp = name;
        
        if printcounter == 4 and temp not in arrayList:
            weight.write(name+"\n")
        if printcounter == 2 and temp not in arrayList:
           height.write(name+"\n")
    arrayList.append(temp) 
    


lines = pokeList.read().splitlines()

for word in lines:
    url = "https://pokemondb.net/pokedex/" + word.lower()
   # print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    name_box = soup.find('td', attrs={'class': 'cell-med-text'})
    name = name_box.text.strip()
    descrip.write(name+"\n")