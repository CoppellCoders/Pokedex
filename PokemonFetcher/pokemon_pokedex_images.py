import requests
import urllib.request
from bs4 import BeautifulSoup

def get_pokemon_image_url():
    fw = open('pokemon_image_url.txt', 'w')
    for x in range(151):
        url = r'https://www.pokemon.com/us/pokedex/' + str(x+1)
        source_code = requests.get(url).text
        bs4_obj = BeautifulSoup(source_code, features="html.parser")
        image_url = bs4_obj.find_all('link', {'rel': 'image_src'})[0]
        href = image_url.get('href')
        print(href)  # prints url of image to console
        fw.write(href + "\n")  # writes urls of images to the text file
    fw.close()

def download_pokemon_images():
    fr = open('pokemon_image_url.txt', 'r')  # make sure the file lines is 151
    lines = fr.read().split("\n")
    for x in lines:
        urllib.request.urlretrieve(x, r'C:/Users/Badol/PycharmProjects/googleImageSpider/pokemon_images/pokemon_' + str(x)[56:])  # any file location is fine
    fr.close()


download_pokemon_images()