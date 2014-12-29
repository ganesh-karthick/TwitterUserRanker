__author__ = 'gk'

# Parses JSON file contain Tweets in the following format per line
#
# {
#     "text": "Over ongeveer een uur landt @MarsCuriosity op de rode planeet!",
#     "created_at": "Mon Aug 06 04:29:10 +0000 2012",
#     "entities": {
#         "user_mentions": [
#             {
#                 "indices": [
#                     28,
#                     42
#                 ],
#                 "id_str": "15473958",
#                 "id": 15473958,
#                 "name": "Curiosity Rover",
#                 "screen_name": "MarsCuriosity"
#             }
#         ],
#         "hashtags": [],
#         "urls": []
#     },
#     "user": {
#         "lang": "en",
#         "created_at": "Tue May 11 16:38:20 +0000 2010",
#         "utc_offset": 3600,
#         "verified": false,
#         "description": "Arts, AIOS interne geneeskunde, promovendus. Actief binnen CDA (bestuur afdeling Leiden) en CDJA (ex-vz. werkgroep VWS). ",
#         "friends_count": 735,
#         "profile_image_url_https": "https://si0.twimg.com/profile_images/1079663082/pasfoto_normal.png",
#         "followers_count": 575,
#         "screen_name": "Arjen_Joosse",
#         "location": "Leiden",
#         "favourites_count": 9,
#         "statuses_count": 5256,
#         "id": 142737491,
#         "name": "Arjen Joosse"
#     },
#     "retweet_count": 0,
#     "id": 232332465388257280
# }

import re
import json
import os
from pprint import pprint

class Parser:
    fileName = ""
    size = 0

    def __init__(self,fileName):
        super().__init__()
        self.fileName = fileName
        self.size = os.path.getsize(fileName)

    def parseFile(self, objectHook):
        json_file = open(self.fileName)
        objectList = list()
        try:
            count = 0
            for line in json_file:
                 objectList.append(json.loads(line,object_hook=objectHook))
                 count+=len(line)
                 print("Read %d bytes out of %d bytes \r" % (count, self.size))
        except KeyError as e:
            print(" Key Error in line  , Exception %s" % e)
            print(line)
        json_file.close()
        return objectList

def toLowerCase(string):
    return string.lower()
def getWords(string):
    return re.sub('[^A-Za-z0-9]+', ' ', string.lower()).split(' ')



