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
    # Send request.
    url = "http://mp.weixin.qq.com/s?__biz=MjM5MTIzMzA0Ng==&mid=2651222013&idx=2&sn=f87a10ea5e0d84c30a444026fdf50342&chksm=bd4a6a848a3de392d893f8c9a81dc46864e94bf6f87ed02b9c5f6c1a7bd5f6f6c08a32902f12&scene=0#rd"
    text = urlrequester.requestHtml(url)
    # Parse html.
    text = htmlparser.parse("debug", text)
    # Export to pdf.
    htmltopdf.run(text, "debug")

if __name__ == "__main__":
    import sys
    cmd = sys.argv[1]
    if cmd == "run":
        __run(sys.argv[2])
    elif cmd == "clean":
        __clean()
    elif cmd == "debug":
        __debug()
    else:
        print("Unknown cmd...")
