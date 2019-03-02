#! python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re

class HtmlParser:
    # Html file.
    __file  = None
    # BeautifulSoup instance.
    __bsoup = None
    # Available tags list.
    __tags  = None
    # Article title.
    __title = None
    # Article publish date.
    __pdate = None
    # Nickname of article's author.
    __nname = None

    # Run parser process.
    def parse(self, fileName):
        self.__import(fileName)
        self.__captureHead()
        self.__captureTags()
        self.__debug()
        self.__clear()

    def __clear(self):
        del self.__file
        del self.__bsoup
        del self.__tags
        del self.__title
        del self.__pdate
        del self.__nname

    # Import html raw data.
    def __import(self, fileName):
        self.__file = open(fileName, "r", encoding = "utf-8")
        self.__bsoup = BeautifulSoup(self.__file.read(), "lxml")
        self.__file.close()

    # Capture head messages.
    def __captureHead(self):
        rawTags = self.__bsoup.find_all("script")
        for tag in rawTags:
            match = re.search("var msg_title.+\s", tag.text)
            if not match:
                continue
            # Capture title.
            self.__title = self.__trim(match.group())
            # Capture publish date.
            match = re.search("var publish_time.+\s", tag.text)
            self.__pdate = self.__trim(match.group())
            # Capture author's nickname.
            match = re.search("var nickname.+\s", tag.text)
            self.__nname = self.__trim(match.group())
            break
        del rawTags

    # Capture tags containing messages.
    def __captureTags(self):
        rawTags = self.__bsoup.find_all(["section", "p"])
        self.__tags = []
        for tag in rawTags:
            if self.__isMeaninglessTag(tag):
                continue
            self.__tags.append(tag)
        del rawTags

    # Capture string between two double quotes in a string.
    @staticmethod
    def __trim(inString):
        index = inString.find("\"") + 1
        return inString[index : inString.find("\"", index)]

    # Judge if a tag doesn't contain essential messages.
    @staticmethod
    def __isMeaninglessTag(tag):
        return {
            "section" : tag.parent.name == "section",
            "p"       : not tag.has_attr("style"),
        }.get(tag.name, True)

    def __debug(self):
        for t in self.__tags:
            print("[tag]")
            print(t)