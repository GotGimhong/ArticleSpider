#! /lib python
# -*- coding: utf-8 -*-

# Headers used to feign an explorer request.
__htmlHeaders = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36",
}

# Headers used to feign an explorer request.
__imageHeaders = {
    "User-Agent" : "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
}

# Request raw html data.
def requestHtml(url):
    import urllib.request
    request = urllib.request.Request(url, None, __htmlHeaders)
    try:
        respond = urllib.request.urlopen(request)
        return respond.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        print("requestHtml : Error %s" % error.msg)

# Request image.
def requestImage(url):
    import urllib.request
    request = urllib.request.Request(url, None, __imageHeaders)
    try:
        respond = urllib.request.urlopen(request)
        return respond.read()
    except urllib.error.HTTPError as error:
        print("requestImage : Error %s" % error.msg)
