#! /lib python
# -*- coding: utf-8 -*-

def writeText(text, fileName):
    with open(fileName, "w", encoding = "utf-8") as file:
        file.write(text)
        file.close()

def writeImage(data, fileName):
    with open(fileName, "wb") as file:
        file.write(data)
        file.close()
