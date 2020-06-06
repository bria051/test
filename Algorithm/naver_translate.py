import os
import sys
import urllib.request
import json
client_id = "ss2uZ9mximctqJH9D5sp"
client_secret = "85JTDZCnVa"

#with open('source.txt','r',encoding='utf8') as f:
#    srcText = f.read()

def choise():
    while(True):
        text = input("번역하실 언어를 선택해주세요:")
        if(text == "한국어"):
            srcText = input("번역할 한국어를 입력해 주세요:")
            a = "ko"
            an = "한국어"
            break
        elif(text == "영어"):
            srcText = input("번역할 영어를 입력해 주세요:")
            a = "en"
            an = "영어"
            break
        elif(text == "중국어"):
            srcText = input("번역할 중국어를 입력해 주세요:")
            a = "zh-CN"
            an = "중국어"
            break
        else:
            print("본 서비스에서 지원하지 않는 언어 입니다.")

    while(True):
        text = input("번역될 언어를 입력해 주세요:")
        if(an == text):
            print("같은 언어는 선택하실 수 없습니다")
        else:
            if(text == "중국어"):
                b = "zh-CN"
                break
            elif(text == "영어"):
                b = "en"
                break
            elif (text == "한국어"):
                b = "ko"
                break
            else:
                print("본 서비스에서 지원하지 않는 언어 입니다.")
    return a, b, srcText

a, b, srcText = choise()

encText = urllib.parse.quote(srcText)
data = "source=" + a + "&target=" + b + "&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()

    res = json.loads(response_body.decode('utf-8'))
    from pprint import pprint
    #pprint(res)

#    with open('translate.txt', 'a',encoding='utf8') as f:
#        f.write(res['message']['result']['translatedText'])
    print(res['message']['result']['translatedText'])

else:
    print("Error Code:" + rescode)