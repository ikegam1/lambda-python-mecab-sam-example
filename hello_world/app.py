import os
import sys
import json

# preload libmecab
import ctypes
libdir = os.path.join(os.getcwd(), '/var/task/lib')
libmecab = ctypes.cdll.LoadLibrary(os.path.join(libdir, 'libmecab.so'))

import MeCab

# IPA辞書を利用
ipadic_tagger = MeCab.Tagger('-r /dev/null -d /var/task/lib/mecab/dic/ipadic')
# NEologdを利用
neologd_tagger = MeCab.Tagger('-r /dev/null -d /var/task/lib/mecab/dic/mecab-ipadic-neologd')


def lambda_handler(event, context):
    
    keyword = event['queryStringParameters']['keyword']

    print (ipadic_tagger.parse(keyword))
    print (neologd_tagger.parse(keyword))
    return {
        "statusCode": 200,
        "body": json.dumps({
            "ipadic": ipadic_tagger.parse(keyword),
            "neologd": neologd_tagger.parse(keyword)
        }),
    }
