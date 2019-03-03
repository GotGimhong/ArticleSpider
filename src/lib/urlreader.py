#! /lib python
# -*- coding: utf-8 -*-

# Column title(pattern) of article's title.
__pattern_title         = "标题"
# Column title(pattern) of publish time.
__pattern_publish_time  = "发布时间"
# Column title(pattern) of article's url.
__pattern_url           = "URL"

# Correct the given string.
def __correct(string):
    # Solve encoding problem, such as '\xa0'.
    string = "".join(string.split())
    # These characters cannot exist in a file or directory's name.
    for ch in [ "\\", "/", ":", "?", "*", "<", ">", "|", "." ]:
        string = string.replace(ch, "")
    return string

# Read all urls
def read(fileName):
    import xlrd
    import re
    from lib import pathdefine
    workbook = xlrd.open_workbook("%s\\%s" % (pathdefine.xlsx, fileName))
    sheet = workbook.sheet_by_index(0)
    # Capture column 'title', 'publish time' and 'url'.
    tindex  = -1
    pindex = -1
    uindex  = -1
    for index in range(0, sheet.ncols):
        head = sheet.col(index)[0].value
        if re.match(__pattern_title, head, re.I):
            tindex = index
        elif re.match(__pattern_publish_time, head, re.I):
            pindex = index
        elif re.match(__pattern_url, head, re.I):
            uindex = index
        if tindex >= 0 and pindex >=0 and uindex >= 0:
            break
    assert(tindex >= 0 and pindex >= 0 and uindex >= 0)
    # Set up a table with publish time and title as key and url as value.
    table = {}
    result = {}
    for index in range(1, sheet.nrows):
        title = __correct(sheet.cell(index, tindex).value)
        pdate = sheet.cell(index, pindex).value
        pdate = pdate[0 : pdate.find(" ")].replace("-", "")
        # Check duplication.
        if title in table:
            table[title] += 1
        else:
            table[title] = 1
            result["%s@%s" % (pdate, title)] = sheet.cell(index, uindex).value
    # Record duplication.
    dup = 0
    with open("201812.txt", "a", encoding = "utf-8") as file:
        file.write("标题 : 重复次数\n")
        for key, value in table.items():
            if value == 1:
                continue
            file.write("%s : %d\n" % (key, value - 1))
            dup += (value - 1)
        file.write("实际导出数 : %d = 数据总数 : %d - 重复总数 : %d\n" % (len(table), sheet.nrows - 1, dup))
        file.close()
    del table
    return result
