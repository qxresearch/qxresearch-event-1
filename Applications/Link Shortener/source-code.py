import pyshorteners

link = input("enter the link:") #variable
shortener = pyshorteners.Shortener() #class object

x = shortener.tinyurl.short(link) #shorting the link

print(x)
