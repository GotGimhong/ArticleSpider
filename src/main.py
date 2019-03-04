#! python
# -*- coding: utf-8 -*-

# Run process.
def __run(fileName):
    # Get urls.
    from lib import urlreader
    table = urlreader.read(fileName)
    total = len(table)
    print("%d files in total." % (total))
    # Make...
    from lib import urlrequester
    from lib import htmlparser
    from lib import htmltopdf
    index = 0
    for key, url in table.items():
        # Send request.
        text = urlrequester.requestHtml(url)
        # Parse html.
        text = htmlparser.parse(key, text)
        # Export to pdf.
        htmltopdf.run(text, key)
        index += 1
        print("%d done, %d left." % (index, total - index))
    print("Done.")
    del table

# Clean up caches.
def __clean():
    import os
    from lib import pathdefine
    def removeAll(directory):
        for root, dirs, files in os.walk(directory, topdown = False):
            for name in files:
                print("%s\\%s" % (root, name))
                os.remove("%s\\%s" % (root, name))
            for name in dirs:
                print("%s\\%s" % (root, name))
                os.rmdir("%s\\%s" % (root, name))
    removeAll(pathdefine.html)
    removeAll(pathdefine.imgs)

# Debug
def __debug():
    # Make...
    from lib import urlrequester
    from lib import htmlparser
    from lib import htmltopdf
    key = ""
    url = ""
    # Send request.
    text = urlrequester.requestHtml(url)
    # Parse html.
    text = htmlparser.parse(key, text)
    # Export to pdf.
    htmltopdf.run(text, key)

if __name__ == "__main__":
    import sys
    # BeautifulSoup.prettify() may causes a large
    # amount of recursion, which might be more than
    # default limit (1000) of the system. Try resetting
    # it if necessary.
    # sys.setrecursionlimit(value bigger than 1000...)
    cmd = sys.argv[1]
    if cmd == "run":
        __run(sys.argv[2])
    elif cmd == "clean":
        __clean()
    elif cmd == "debug":
        __debug()
    else:
        print("Unknown cmd...")
