# -*- conding: utf-8 -*-


import httplib
import json

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class NewsService(object):

    def getNews(self):
        try:
            conn = httplib.HTTPSConnection("api.hurriyet.com.tr")

            headers = {
                'accept': "application/json",
                'apikey': '5d424338236d445ebc03029b00c7da11'
            }

            conn.request("GET", "/v1/articles?%24top=5", headers=headers)

            res = conn.getresponse()
            data = res.read()

            response = json.loads(data)
            # print(response[1]["Description"])
            # response = json.load(data)
            return (
                response[0]["Title"],
                response[1]["Title"],
                response[2]["Title"],
                response[3]["Title"],
                response[4]["Title"]
            )
        except:
            return (
                "",
                "",
                "",
                "",
                ""
            )



NewsService().getNews()