import sys
import urllib
import urllib2
from wechatconfig import *

url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"

query_args = { 'corpid': CorpID, 'corpsecret': Secret }

def get_accesstoken():
    encoding_args = urllib.urlencode(query_args)
    return urllib2.urlopen(url + encoding_args).read()


if __name__ == '__main__':
    print get_accesstoken()
