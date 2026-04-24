import pyshorteners
from urllib.request import urlopen, Request
from urllib.parse import urlparse, urlunparse
import socket
import ipaddress
import time
import re

def link_shortener(link):
    try:
        # Validate URL scheme
        parsed = urlparse(link)
        if parsed.scheme not in ['http', 'https']:
            print('\t[-] Invalid URL scheme')
            return
        
        # Check for dangerous patterns in URL
        if any(pattern in link.lower() for pattern in ['localhost', '127.', '::1']):
            print('\t[-] Dangerous URL pattern detected')
            return
        
        shortener = pyshorteners.Shortener()
        try:
            short_link = shortener.tinyurl.short(link)
            
            # Display sanitized output
            print('\t[+] Real Link: ' + link[:100])
            print('\t[+] Shortened Link: ' + short_link if short_link else 'Failed')
        except Exception as e:
            print('\t[-] Error shortening link: ' + str(e)[:50])
    except Exception as e:
        print('\t[-] Error shortening link: ' + str(e)[:50])

def is_safe_url(url):
    """Check if URL is safe to access (SSRF protection)"""
    try:
        parsed = urlparse(url)
        
        # Block localhost and private IP ranges
        hostname = parsed.hostname
        if not hostname:
            return False
        
        # Check for dangerous patterns
        if 'localhost' in hostname.lower():
            return False
        
        # Resolve to IP and check against private ranges
        try:
            ip = socket.gethostbyname(hostname)
            ip_obj = ipaddress.ip_address(ip)
            
            # Block private, loopback, link-local, multicast addresses
            if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local or ip_obj.is_multicast:
                return False
            
            # Block reserved ranges (0.0.0.0/8, 224.0.0.0/4, etc.)
            if ip_obj.is_reserved:
                return False
                
        except socket.gaierror:
            return False
        
        return True
    except Exception:
        return False

def link_opener(link):
    try:
        # Validate URL scheme
        parsed = urlparse(link)
        if parsed.scheme not in ['http', 'https']:
            print('\t[-] Invalid URL scheme')
            return
        
        # SSRF protection - validate before making request
        if not is_safe_url(link):
            print('\t[-] Unsafe URL detected')
            return
        
        # Add timeout and error handling for network requests
        try:
            shortened_url = urlopen(Request(link, method='GET'), timeout=10)
            real_link = shortened_url.geturl()

            # Display sanitized output
            print('\t[+] Shortened Link: ' + link[:100])
            print('\t[+] Real Link: ' + real_link[:100] if real_link else 'Failed')
        except Exception as e:
            print('\t[-] Error opening link: ' + str(e)[:50])
    except Exception as e:
        print('\t[-] Error opening link: ' + str(e)[:50])

if __name__ == '__main__' :

    num = input("Enter your choice ...\n" 
                "1. Type 1 for shortening link\n"
                "2. Type 2 for extracting real link from a shortened link\n")

    link = input("Enter the link: ")    

    if (num == '1') :
       link_shortener(link)
    else :
        link_opener(link)