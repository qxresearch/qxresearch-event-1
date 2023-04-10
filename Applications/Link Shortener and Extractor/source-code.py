import pyshorteners
from urllib.request import urlopen

def link_shortener(link):
    shortener = pyshorteners.Shortener() #class object
    short_link = shortener.tinyurl.short(link)  #shorting the link
    
    #Display
    print('\t[+] Real Link: ' + link)
    print('\t[+] Shortened Link: ' + short_link)

def link_opener(link):

    shortenedUrl = urlopen(link)
    reallink = shortenedUrl.geturl()  #getting real link

    # Display
    print('\t[+] Shortened Link: ' + link)
    print('\t[+] Real Link: ' + reallink)

if __name__ == '__main__' :

    num = input("Enter your choice ...\n" 
                "1. Type 1 for shortening link\n"
                "2. Type 2 for extrcting real link from a shorten link\n")

    link = input("Enter the link: ")    

    if (num == '1') :
       link_shortener(link)
    else :
        link_opener(link)  