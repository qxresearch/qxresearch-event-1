import pyshorteners
from urllib.request import urlopen, Request
from urllib.parse import urlparse
import socket

def link_shortener(link):
    try:
        # Validate URL scheme
        parsed = urlparse(link)
        if parsed.scheme not in ['http', 'https']:
            print('\t[-] Invalid URL scheme')
            return
        
        shortener = pyshorteners.Shortener()
        short_link = shortener.tinyurl.short(link)  #shorting the link
        
        #Display
        print('\t[+] Real Link: ' + link)
        print('\t[+] Shortened Link: ' + short_link)
    except Exception as e:
        print('\t[-] Error shortening link: ' + str(e))

def link_opener(link):
    try:
        # Validate URL scheme
        parsed = urlparse(link)
        if parsed.scheme not in ['http', 'https']:
            print('\t[-] Invalid URL scheme')
            return
        
        # SSRF protection - prevent accessing internal IPs
        def is_safe_url(url):
            try:
                response = urlopen(url, timeout=5)
                ip = socket.gethostbyname(parsed.hostname)
                if ip.startswith('127.') or ip.startswith('10.') or ip.startswith('192.168.') or ip.startswith('172.'):
                    return False
                return True
            except:
                return False
        
        shortened_url = urlopen(link, timeout=5)
        real_link = shortened_url.geturl()  # getting real link

        # Display
        print('\t[+] Shortened Link: ' + link)
        print('\t[+] Real Link: ' + real_link)
    except Exception as e:
        print('\t[-] Error opening link: ' + str(e))

if __name__ == '__main__' :

    num = input("Enter your choice ...\n" 
                "1. Type 1 for shortening link\n"
                "2. Type 2 for extrcting real link from a shorten link\n")

    link = input("Enter the link: ")    

    if (num == '1') :
       link_shortener(link)
    else :
        link_opener(link)