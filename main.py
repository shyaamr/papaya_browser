from tkinter import *
import urllib.request
from bs4 import BeautifulSoup
def go():
	text.delete(1.0, END)
	urlEntry = entry.get()
	url2go = "https://" + urlEntry
	print(url2go)
	with urllib.request.urlopen(entry.get()) as response:
		received_html = response.read()
		parsed_html = BeautifulSoup(received_html, "lxml")
		webTitle = parsed_html.find('title').text
		print(webTitle)

browser_window = Tk()
browser_window.title('Papaya Browser')
label = Label(browser_window, text= 'URL:')
entry = Entry(browser_window)
entry.insert(END, "https://google.com")
button = Button(browser_window, text='Go', command = go)
text = Text(browser_window)
label.pack(side=TOP)
entry.pack(side=TOP)
button.pack(side=TOP)
text.pack(side= TOP)
browser_window.mainloop()
