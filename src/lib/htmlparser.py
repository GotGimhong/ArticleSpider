#! /lib python
# -*- coding: utf-8 -*-

def parse(key, content):
    import bs4
    import re
    import os
    from lib import pathdefine
    from lib import filewriter
    from lib import urlrequester
    # Create directory for image caches.
    directory = "%s\\%s" % (pathdefine.imgs, key)
    if not os.path.exists(directory):
        os.makedirs(directory)
    bsoup = bs4.BeautifulSoup(content, "lxml")
    # Remove (useless) javascripts from html.
    for tag in bsoup("script"):
        tag.extract()
    index = 0
    for tag in bsoup("img"):
        if not tag.has_attr("data-src"):
            # Not a image in body.
            if tag.has_attr("src"):
                tag.extract()
            continue
        data = urlrequester.requestImage(tag["data-src"])
        if not data:
            continue
        index += 1
        # Download image to local.
        suffix = tag.has_attr("data-type") and tag["data-type"] or "jpg"
        fileName = "%s\\%s.%s" % (directory, index, suffix)
        filewriter.writeImage(data, fileName)
        # Replace source attribute.
        del tag.attrs["data-src"]
        tag.attrs["src"] = fileName
    return bsoup.prettify()
