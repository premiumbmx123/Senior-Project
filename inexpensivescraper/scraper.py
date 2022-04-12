import os
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

'''
URL = "https://steamcharts.com/top"
gameURLs = []
steamURLs = []
minCPURank = []

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

for i in soup.select("tbody > tr > td > a"):
    gameURLs.append("https://steamcharts.com" + i["href"])

for URL in gameURLs:
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    steamURLs.append(soup.select("div#app-links > a:nth-of-type(1)")[0]["href"])

for URL in steamURLs:
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    if len(soup.select("div:nth-of-type(1) > div.game_area_sys_req_full > ul")) > 0:
        for i in soup.select("div:nth-of-type(1) > div.game_area_sys_req_full > ul > ul > li"):
            if "Processor" in i.text:
                print(i.text)
    else:
        for i in soup.select("div:nth-of-type(1) > div.game_area_sys_req_leftCol > ul > ul > li"):
            if "Processor" in i.text:
                print(i.text)

'''

cluster = os.environ.get("MONGODB_URI")
client = MongoClient(cluster)

db = client.SeniorDesign

scrapeData = db.graphicsCards

URLs = ["https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966937+4294820651&myStore=false", "https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966937+4294821460&myStore=false"]
neweggURLs = ["https://www.newegg.com/p/pl?N=100007671%204131%20601306860%204841%2050001157%204814%208000&PageSize=96", "https://www.newegg.com/p/pl?N=100007671%204131%204841%204814%208000%2050001028&PageSize=96"]

parts = []


for URL in URLs:
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    for i in soup.select("h2 > a[data-price]"):
        parts.append("microcenter.com" + i["href"])

    for i in soup.select("div > div > nav > ul.pages > li > a"):
        if ">" not in i.text:
            page = requests.get("https://www.microcenter.com" + i["href"])
            soup = BeautifulSoup(page.content, "html.parser")
            for j in soup.select("h2 > a[data-price]"):
                parts.append("microcenter.com" + j["href"])

graphicsCardData = {}

for i in parts:
    microcenterLink = "https://" + i

    page = requests.get(microcenterLink)

    soup = BeautifulSoup(page.content, "html.parser")

    if "NOT CARRIED" not in soup.select("p.inventory")[0].text and "SOLD OUT" not in soup.select("p.inventory")[0].text:
        modelNum = soup.select("dl > dd:nth-of-type(2)")[0].text.strip()
        clockSpeed = soup.select(
            "div.SpecTable > div:nth-of-type(11) > div:nth-of-type(2)")
        imageLink = soup.select(
            "div.image-slide > a:nth-of-type(1) > img:nth-of-type(1)")
        name = soup.select("span > span[data-category]")
        price = soup.select("span#pricing")
        manufacturer = soup.select("div:nth-of-type(7) > div:nth-of-type(2)")

        neweggPrice = "N/A"
        neweggLink = ""

        page = requests.get("https://www.newegg.com/p/pl?d=" + modelNum + "+graphics+card&N=4841&N=4841")

        soup = BeautifulSoup(page.content, "html.parser")

        passes = 0

        if not soup.find("span", {"class": "result-message-error"}):
            for j in soup.select("div > div.item-cell > div > a"):
                if "combodeal" not in j["href"].lower():
                    passes += 1
                    if passes > 5:
                        break
                    page = requests.get(j["href"])

                    soup = BeautifulSoup(page.content, "html.parser")

                    if len(soup.select("table.table-horizontal tbody > tr:nth-of-type(3) > td")) > 0:
                        if modelNum == soup.select("table.table-horizontal tbody > tr:nth-of-type(3) > td")[0].text:
                            if soup.find("div", {"class": "is-collapse"}):
                                neweggPrice = soup.select("div.product-pane:nth-of-type(2) > div.product-price > ul > li.price-current")[0].text
                                neweggLink = j["href"]
                            else:
                                neweggPrice = soup.select("div.product-pane > div.product-price > ul > li.price-current")[0].text
                                neweggLink = j["href"]
        microcenterNum = 0
        neweggNum = "N/A"
        savings = 0
        if neweggPrice != "N/A":
            microcenterNum = price[0].text.replace("$","")
            microcenterNum = float(microcenterNum.replace(",", ""))
            neweggNum = neweggPrice.replace("$","")
            neweggNum = float(neweggNum.replace(",", ""))

            savings = (max(neweggNum, microcenterNum) - min(neweggNum, microcenterNum)) / max(neweggNum, microcenterNum)

        graphicsCardData = {
            "modelNum": modelNum,
            "clockSpeed": clockSpeed[0].text,
            "imageLink": imageLink[0]["src"],
            "name": name[0].text,
            "pricing": price[0].text,
            "manufacturer": manufacturer[0].text,
            "newegg": neweggPrice,
            "microcenterLink": microcenterLink,
            "neweggLink": neweggLink,
            "minimum": "Meets 25/25 minimum settings!",
            "savings": savings
        }

        dataArray = []
        dataArray.append(graphicsCardData)

        result = scrapeData.insert_one(graphicsCardData)

'''
scrapeData = db.cpus

URLs = ["https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966995+4294819840&myStore=false", "https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966995+4294820689&myStore=false", ]

parts = []

for URL in URLs:
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    for i in soup.select("div.detail_wrapper"):
        parts.append("microcenter.com" + i.select("h2 > a[data-price]")[0]["href"])

    for i in soup.select("div > div > nav > ul.pages > li > a"):
        if ">" not in i.text:
            print("https://www.microcenter.com" + i["href"])
            page = requests.get("https://www.microcenter.com" + i["href"])
            soup = BeautifulSoup(page.content, "html.parser")
            for j in soup.select("div.detail_wrapper"):
                parts.append("microcenter.com" + j.select("h2 > a[data-price]")[0]["href"])

cpuData = {}

for i in parts:
    microcenterLink = "https://" + i
    page = requests.get(microcenterLink)

    soup = BeautifulSoup(page.content, "html.parser")

    if "NOT CARRIED" not in soup.select("p.inventory")[0].text and "SOLD OUT" not in soup.select("p.inventory")[0].text:
        print(i)
        modelNum = soup.select("dl > dd:nth-of-type(2)")[0].text.strip()
        imageLink = soup.select("div.image-slide:nth-of-type(1) img")
        name = soup.select("span > span[data-category]")
        price = soup.select("span#pricing")

        neweggPrice = "N/A"
        neweggLink = ""

        page = requests.get("https://www.newegg.com/p/pl?d=" + modelNum + "+processor&N=4841&N=4841")

        soup = BeautifulSoup(page.content, "html.parser")

        if not soup.find("span", {"class": "result-message-error"}):
            for j in soup.select("div > div.item-cell > div > a"):
                if "combodeal" not in j["href"].lower():
                    print(j["href"])
                    page = requests.get(j["href"])

                    soup = BeautifulSoup(page.content, "html.parser")

                    if modelNum == soup.select("table:nth-of-type(2) > tbody > tr:nth-of-type(5) > td")[0].text:
                        if soup.find("div", {"class": "is-collapse"}):
                            neweggPrice = soup.select("div.product-pane:nth-of-type(2) > div.product-price > ul > li.price-current")[0].text
                            neweggLink = j["href"]
                        else:
                            neweggPrice = soup.select("div.product-pane > div.product-price > ul > li.price-current")[0].text
                            neweggLink = j["href"]

        cpuData = {
            "modelNum": modelNum,
            "imageLink": imageLink[0]["src"],
            "name": name[0].text,
            "pricing": price[0].text,
            "manufacturer": name[0]["data-brand"],
            "newegg": neweggPrice,
            "microcenterLink": microcenterLink,
            "neweggLink": neweggLink
        }

        dataArray = []
        dataArray.append(cpuData)

        result = scrapeData.insert_one(cpuData)
'''