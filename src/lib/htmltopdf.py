#! /lib python
# -*- coding: utf-8 -*-

def run(content, fileName):
    # Create directory for image caches.
    import os
    from lib import pathdefine
    if not os.path.exists(pathdefine.pdf):
        os.makedirs(pathdefine.pdf)
    try:
        import pdfkit
        config = pdfkit.configuration(wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        pdfkit.from_string(content, "%s\\%s.pdf" % (pathdefine.pdf, fileName), configuration = config)
    except OSError:
        # An error may occur here sometimes but has no influence on output, just pass it.
        pass
    except IOError:
        # An error may occur here sometimes but has no influence on output, just pass it.
        pass
