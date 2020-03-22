import requests
from bs4 import BeautifulSoup as bs

link = ("https://kawalcorona.com")
web = requests.get(link).text
parse = bs(web, "html.parser")
def banner():
    print ("[1] Data Corona Global")
    print ("[2] Data Corona Lokal")
def corona1():
    for i in (parse.find_all("div", class_='col-sm-12 col-md-6 col-lg-6 col-xl-3')):
        print("_" * 50)
        print(i.find('div', class_='text-white').get_text())
def corona2():
    for y in (parse.find_all("div", clas_="row row-cards")):
        print("_"*50)
        print(y.find("tbody"))

if __name__=="__main__":
    banner()
    masuk = input("Masukkan Pilihan>> ")
    if masuk == "1":
        corona1()
    elif masuk == "2":
        print("Coming Soon!!")
    else:
        print("Salah Input!!")