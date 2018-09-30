import requests
from bs4 import BeautifulSoup


def get_pokemmon_height():
    fw = open('pokemon_heights.txt', 'w')
    for x in range(151):
        url = r'https://www.pokemon.com/us/pokedex/' + str(x + 1)
        print(url)  # prints out url
        source_code = requests.get(url).text
        bs4_obj = BeautifulSoup(source_code, features='html.parser')
        height = bs4_obj.find_all('span', {'class': 'attribute-value'})[0]
        height = str(height)
        if len(height) is 43:
            fw.write(height[30:36] + "\n")
        elif len(height) is 44:
            fw.write(height[30:37] + "\n")
    fw.close()


def get_pokemmon_weight():
    fw = open('pokemon_weights.txt', 'w')
    for x in range(151):
        url = r'https://www.pokemon.com/us/pokedex/' + str(x + 1)
        print(url)  # prints out url
        source_code = requests.get(url).text
        bs4_obj = BeautifulSoup(source_code, features='html.parser')
        weight = bs4_obj.find_all('span', {'class': 'attribute-value'})[1]
        weight = str(weight)
        if len(weight) is 44:
            fw.write(weight[30:37] + "\n")
        if len(weight) is 45:
            fw.write(weight[30:38] + "\n")
        if len(weight) is 46:
            fw.write(weight[30:39] + "\n")
        if len(weight) is 47:
            fw.write(weight[30:40] + "\n")
    fw.close()

