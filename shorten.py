#First intall pyshorteners

#Second use this code
import pyshorteners

link = input("Link: ")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)
