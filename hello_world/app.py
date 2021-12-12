import os
import sys
import json

# preload libmecab
import ctypes
libdir = os.path.join(os.getcwd(), '/var/task/lib')
libmecab = ctypes.cdll.LoadLibrary(os.path.join(libdir, 'libmecab.so'))

import MeCab

# IPA辞書を利用
ipadic_tagger = MeCab.Tagger('-O wakati -r /dev/null -d /var/task/lib/mecab/dic/ipadic')
# NEologdを利用
neologd_tagger = MeCab.Tagger('-O wakati -r /dev/null -d /var/task/lib/mecab/dic/mecab-ipadic-neologd')


def lambda_handler(event, context):
    

    text = '中居正広の金曜日のスマイルたちへ'
    print (ipadic_tagger.parse(text))
    print (neologd_tagger.parse(text))
    return {
        "statusCode": 200,
        "body": json.dumps({
            "ipadic": ipadic_tagger.parse('中居正広の金曜日のスマイルたちへ'),
            "neologd": neologd_tagger.parse('中居正広の金曜日のスマイルたちへ')
        }),
    }
