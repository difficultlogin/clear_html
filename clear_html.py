#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, re
from urllib import request

def get_charset(header):
    match = re.search(r'charset=([^\s;]+)', header)

    if match:
        return match.group(1).strip('"\'').lower()
    else:
        return 'utf-8'


def get_html(link):
    with request.urlopen(link) as url:
        charset = get_charset(url.getheader('content-type'))
        return url.read().decode(charset)

def clear_html(html):
    p = re.compile(r'style=".*?"')
    return p.sub('', html)

if __name__ == '__main__':
    # Use:
    #   link - argument command line 1
    #   get_charset - return encoding type
    #   get_html (link) - return original html for link
    #   clear_html (html) - return clear html without attributes 'style'
    #   python3 ./clear_html.py http://testdomain.com

    try:
        link = sys.argv[1]
    except IndexError:
        print('use: ./clear_html.py {link}')
        exit()

    html = get_html(link)
    print(clear_html(html))