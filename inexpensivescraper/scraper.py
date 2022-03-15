import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

cluster = "mongodb+srv://seniorbois:Somethingsomethingdarkside123!!@cluster0.bpwqg.mongodb.net/SeniorDesign?retryWrites=true&w=majority"
client = MongoClient(cluster)

db = client.SeniorDesign

scrapeData = db.graphicsCards

URL = "https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966937&myStore=false"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

parts = []

for i in soup.select("h2 > a[data-price]"):
    parts.append("microcenter.com" + i["href"])

graphicsCardData = {}

for i in parts:
    page = requests.get("https://" + i)

    soup = BeautifulSoup(page.content, "html.parser")
    SKU = soup.select("dd.SKUNumber")
    clockSpeed = soup.select(
        "div.SpecTable > div:nth-of-type(11) > div:nth-of-type(2)")
    imageLink = soup.select(
        "div.image-slide > a:nth-of-type(1) > img:nth-of-type(1)")
    name = soup.select("span > span[data-category]")
    price = soup.select("span#pricing")
    manufacturer = soup.select("div:nth-of-type(7) > div:nth-of-type(2)")

    graphicsCardData = {
        "SKU": SKU[0].text,
        "clockSpeed": clockSpeed[0].text,
        "imageLink": imageLink[0]["src"],
        "name": name[0]["data-name"],
        "pricing": price[0].text,
        "manufacturer": manufacturer[0].text
    }

    dataArray = []
    dataArray.append(graphicsCardData)

    result = scrapeData.insert_one(graphicsCardData)

scrapeData = db.cpus

URL = "https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966995+4294820689&myStore=false"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

parts = []

for i in soup.select("div.detail_wrapper"):
    print("NOT CARRIED" not in i.select("div.stock")[0].text)
    if "NOT CARRIED" not in i.select("div.stock")[0].text:
        parts.append("microcenter.com" + i.select("h2 > a[data-price]")[0]["href"])

cpuData = {}

for i in parts:
    page = requests.get("https://" + i)

    soup = BeautifulSoup(page.content, "html.parser")
    SKU = soup.select("dd.SKUNumber")
    imageLink = soup.select(
        "div.image-slide > a:nth-of-type(1) > img:nth-of-type(1)")
    name = soup.select("span > span[data-category]")
    price = soup.select("span#pricing")

    cpuData = {
        "SKU": SKU[0].text,
        "imageLink": imageLink[0]["src"],
        "name": name[0]["data-name"],
        "pricing": price[0].text,
        "manufacturer": "Intel"
    }

    dataArray = []
    dataArray.append(cpuData)

    result = scrapeData.insert_one(cpuData)
