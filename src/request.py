#! python
# -*- coding: utf-8 -*-

import requests
import urllib.request

class UrlRequester:
    # Request raw html data.
    @staticmethod
    def requestHtml(url, fullName):
        respond = requests.get(url)
        file = open(fullName, "w", encoding = "utf-8")
        file.write(respond.text)
        file.close()

    # Request image.
    @staticmethod
    def requestImage(url, fullName):
        urllib.request.urlretrieve(url, fullName)
