# -*- coding: utf-8 -*-
__autor__ = "Ricksenberg"
__date__ = "0daybitch"
from pyquery import PyQuery as Pq
from urllib import urlencode
import argparse

_banner_ = """_______________________________________________________
 _______  __       __  ___   ___  _______  __       __  ___   ___
|   ____||  |     |  | \  \ /  / |   ____||  |     |  | \  \ /  /
|  |__   |  |     |  |  \  V  /  |  |__   |  |     |  |  \  V  /
|   __|  |  |     |  |   >   <   |   __|  |  |     |  |   >   <
|  |     |  `----.|  |  /  .  \  |  |     |  `----.|  |  /  .  \
|__|     |_______||__| /__/ \__\ |__|     |_______||__| /__/ \__\

_____________________________________________________________________
"""

def run():
    """Search session cookies in pastebin.com"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--word", help="palabra clave que desea buscar")
    parser.add_argument("-u", "--url", help="sitio en donde se desea buscar")
    args = parser.parse_args()
    if args.url:
        try:

            title = args.word + " " + args.url
            for page in range(10):
                params_1 = urlencode({'as_q':"%s" % title})
                params = params_1.replace("%22", '')
                jq = Pq(url=" https://www.google.com/search?%s&source=lnt&tbs=qdr:d&sa=X&ved=0ahUKEwi35d68i-XXAhUDuRQKHVVpB88QpwUIHQ&biw=1366&bih=647" % params,
                        headers={"user-agent": "Mozilla/7.0 (Windows NT 6.1; rv:24.0) Gecko/20140129 Firefox/24.0"})
                jq.make_links_absolute("http://www.google.com")
                for flix in jq("div.rc").children().items():
                    url = flix.find("a").attr("href")
                    if url == "http://www.google.com":
                        url = ""
                    print url
        except:
            print "error de red"
if __name__ == '__main__':
    run()