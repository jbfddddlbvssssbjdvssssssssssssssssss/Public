import http.client
from tkinter import *
import re
import os
import sys


def search_info(country,tmp,key_word):
    result_country = re.search(country, tmp)
    end_country = result_country.end()
    result_search = re.search(key_word, tmp[end_country:])
    end_search = result_search.end()
    s = key_word
    while True:
        if tmp[end_search+end_country+1] == ":":
            i=1
            while tmp[end_search+i+end_country] != ",":
                s += tmp[end_search+i+end_country]
                i+=1
            return s
        else: break


conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")


headers = {
    'x-rapidapi-key': "2c501bdd53msh281d423c869cf15p18f22cjsn36d828e0f50d",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }


conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
res = conn.getresponse()
data = res.read()
tmp = data.decode("utf-8")
country = ["France","Italy","Spain","Switzerland","Germany", "Greece"]
lst_search = ["TotalCases","TotalDeaths","ActiveCases","TotalRecovered"]

root = Tk()
root.title("Covid Statistics in Europe")
root.geometry("930x200")


for i in range(len(country)):
    lab_country = Label(root, text=country[i], font="Arial 12", fg="Red")
    lab_country.place(x=155*i, y=1)


    for j in range (len(lst_search)):
        lab_search = Label(root, text=search_info(country[i],tmp,lst_search[j]), font="Arial 10",fg="Black")
        lab_search.place(x=155*i, y=27*(j+1))


def restartProgram():
    os.execl(sys.executable, os.path.abspath('civid.py'), *sys.argv)


Button = Button(text="Update",font="Arial 14", fg="Black", bg="Red", command=restartProgram)
Button.place(x=1, y=140, width=150, height=40)
root.mainloop()