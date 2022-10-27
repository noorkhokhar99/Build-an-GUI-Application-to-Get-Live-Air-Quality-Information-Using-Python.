from tkinter import *
import requests
from bs4 import BeautifulSoup


# link for extract html data
def getdata(url):
	r = requests.get(url)
	return r.text


def airinfo():
	htmldata = getdata("https://weather.com/en-IN/forecast/air-quality/l/3dbed5c769584b3604a70d40a1a0a9f6ebc99c253d955b548f4978ca101eeca1")
	soup = BeautifulSoup(htmldata, 'html.parser')
	res_data = soup.find(class_="DonutChart--innerValue--2rO41 AirQuality--extendedDialText--2AsJa").text
	air_data = soup.find_all(class_="DonutChart--innerValue--2rO41 AirQuality--pollutantDialText--3Y7DJ")
	air_data=[data.text for data in air_data]
	

	ar.set(res_data)
	o3.set(air_data[0])
	no2.set(air_data[1])
	so2.set(air_data[2])
	pm.set(air_data[3])
	pml.set(air_data[4])
	co.set(air_data[5])
	res = int(res_data)
	if res <= 50:
		remark = "Good"
		impact = "Minimal impact"
	elif res <= 100 and res > 51:
		remark = "Satisfactory"
		impact = "Minor breathing discomfort to sensitive people"
	elif res <= 200 and res >= 101:
		remark = "Moderate"
		impact = "Breathing discomfort to the people with lungs, asthma and heart diseases"
	elif res <= 400 and res >= 201:
		remark = "Very Poor"
		impact = "Breathing discomfort to most people on prolonged exposure"
	elif res <= 500 and res >= 401:
		remark = "Severe"
		impact = "Affects healthy people and seriously impacts those with existing diseases"
	res_remark.set(remark)
	res_imp.set(impact)


# object of tkinter
# and background set to grey
master = Tk("Pyresearch")
master.configure(bg='light grey')

# Variable Classes in tkinter
air_data = StringVar()
ar = StringVar()
o3 = StringVar()
no2 = StringVar()
so2 = StringVar()
pm = StringVar()
pml = StringVar()
co = StringVar()
res_remark = StringVar()
res_imp = StringVar()


# Creating label for each information
# name using widget Label
Label(master, text="Air Quality : ",
	bg="light grey").grid(row=0, sticky=W)
Label(master, text="O3 (μg/m3) :",
	bg="light grey").grid(row=1, sticky=W)
Label(master, text="NO2 (μg/m3) :",
	bg="light grey").grid(row=2, sticky=W)
Label(master, text="SO2 (μg/m3) :",
	bg="light grey").grid(row=3, sticky=W)
Label(master, text="PM2.5 (μg/m3) :",
	bg="light grey").grid(row=4, sticky=W)
Label(master, text="PM10 (μg/m3) :",
	bg="light grey").grid(row=5, sticky=W)
Label(master, text="CO (μg/m3) :",
	bg="light grey").grid(row=6, sticky=W)

Label(master, text="Remark :",
	bg="light grey").grid(row=7, sticky=W)
Label(master, text="Possible Health Impacts :",
	bg="light grey").grid(row=8, sticky=W)


# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=ar,
	bg="light grey").grid(
	row=0, column=1, sticky=W)
Label(master, text="", textvariable=o3,
	bg="light grey").grid(
	row=1, column=1, sticky=W)
Label(master, text="", textvariable=no2,
	bg="light grey").grid(
	row=2, column=1, sticky=W)
Label(master, text="", textvariable=so2,
	bg="light grey").grid(
	row=3, column=1, sticky=W)
Label(master, text="", textvariable=pm,
	bg="light grey").grid(
	row=4, column=1, sticky=W)
Label(master, text="", textvariable=pml,
	bg="light grey").grid(
	row=5, column=1, sticky=W)
Label(master, text="", textvariable=co,
	bg="light grey").grid(
	row=6, column=1, sticky=W)
Label(master, text="", textvariable=res_remark,
	bg="light grey").grid(row=7, column=1, sticky=W)
Label(master, text="", textvariable=res_imp,
	bg="light grey").grid(row=8, column=1, sticky=W)


# creating a button using the widget
b = Button(master, text="Check",
		command=airinfo, bg="Blue")
b.grid(row=0, column=2, columnspan=2,
	rowspan=2, padx=5, pady=5,)

mainloop()
