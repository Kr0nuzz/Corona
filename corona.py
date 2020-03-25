import requests, json
from bs4 import BeautifulSoup as bs

link = ("https://kawalcorona.com")
link2 = ("https://api.kawalcorona.com/indonesia/provinsi")
web = requests.get(link).text
web1 = requests.get(link2).json()
parse = bs(web, "html.parser")
def banner():
    print ("[1] Data Corona Global")
    print ("[2] Data Corona Lokal")
def corona1():
    for i in (parse.find_all("div", class_='col-sm-12 col-md-6 col-lg-6 col-xl-3')):
        print("_" * 50)
        print(i.find('div', class_='text-white').get_text())
def corona2():
    for i in web1:
        o = (i['attributes']['Provinsi'])
        p = (i['attributes']['Kasus_Posi'])
        q = (i['attributes']['Kasus_Semb'])
        r = (i['attributes']['Kasus_Meni'])
        print("_"*20)
        print(o)
        print("Kasus Positif :", p)
        print("Kasus Sembuh :", q)
        print("Kasus Meninggal :", r)
        print("_"*20)

if __name__=="__main__":
    banner()
    masuk = input("Masukkan Pilihan>> ")
    if masuk == "1":
        corona1()
    elif masuk == "2":
        corona2()
    else:
        print("Salah Input!!")
