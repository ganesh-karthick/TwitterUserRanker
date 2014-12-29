
from ParserUtils.Parser import toLowerCase,getWords

# Stores Parsed tweet information in a class , as well as provides object hook function for parsing json file

class TweetInfo:
    text = list()
    user_mentions = set()
    created_at = ""
    screen_name = ""
    location=""
    unique_screen_names = set()

    def __init__(self, text ,created_at,screen_name,location,user_mentions):
        self.text = ""
        self.user_mentions = set()
        for item in getWords(text):
            if item != "":
                self.text.append(item)
        for item in user_mentions:
            if item != "" and item != screen_name:
                self.user_mentions.add(toLowerCase(item))
        self.created_at = created_at
        self.screen_name = toLowerCase(screen_name)
        self.location = toLowerCase(location)
        if len(self.user_mentions) > 0:
            TweetInfo.unique_screen_names.add(self.screen_name)
        TweetInfo.unique_screen_names.update(self.user_mentions)

    def __str__(self, *args, **kwargs):
        desc_str = self.screen_name + " Tweeted " +  ':'.join(self.text) +" mentioning " + ':'.join(self.user_mentions) + " from " + self.location + " at " + self.created_at
        return desc_str


    def removeSelfMentions(self):
        if self.screen_name in self.user_mentions:
            self.user_mentions.remove(self.screen_name)

def asTweetInfo(dct):
    if 'retweet_count' in dct:
            user_mentions = set()
            users = dct['entities']['user_mentions']
            for item in users:
                if 'screen_name' in item:
                    user_mentions.add(item['screen_name'])
            location = ""
            if 'location' in dct['user']:
                location = dct['user']['location']
            return TweetInfo(dct['text'],dct['created_at'],dct['user']['screen_name'],location,user_mentions)
    return dct

def asPartialTweetInfo(dct):
    if 'retweet_count' in dct:
            user_mentions = set()
            users = dct['entities']['user_mentions']
            for item in users:
                if 'screen_name' in item:
                    user_mentions.add(item['screen_name'])
            return TweetInfo("","",dct['user']['screen_name'],"",user_mentions)
    return dct




