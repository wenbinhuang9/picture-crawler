from uuid import uuid4
import ssl
import re
import urllib.request
import requests
import  os
ssl._create_default_https_context = ssl._create_unverified_context

headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        #'Host':'https://www.google.com/',
        'Connection':'keep-alive',
        'Accept':'application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5',
        'Referer':'https://www.google.com/',
        'Accept-Encoding':'gzip,deflate,sdch,gbk',
        'Accept-Language':'en-US,en;q=0.8'
}

def getText(url):
   return getTextByHeaders(url, headers)

def getTextByHeaders(url, headers):
    session = requests.session()

    response = session.get(url, headers=headers )

    if (response.status_code != 200) :
        raise ValueError("exception in when loading page")

    response.encoding= "UTF-8"
    return response.text

def downloadPicFromContent(source, filename = ""):
    p = re.compile(r'http.*?.jpg')
    pic_url = re.findall(p, source)

    print(pic_url)
    for i in pic_url:
        if i.find("ess-data=") > 0:
            i_split = i.split("ess-data='")
            i = i_split[1]
            print("i={0}".format(i))
        try:
            downloadPicUlr(i, filename = filename)
        except Exception as e:
            print(e)
            print(i)

def downloadPicUlr(picUrl, filename= "" , format = "jpg"):
    if picUrl.find("ad") > 0 :
        print(picUrl)
        return
    if os.path.exists(filename) == False:
        os.mkdir(filename)

    opener = urllib.request.build_opener()
    opener.addheaders = [(k, v) for k, v in headers.items()]
    urllib.request.install_opener(opener)

    try:
        img_name = str(uuid4())
        print(img_name)
        path =  filename +  img_name + "." + format

        urllib.request.urlretrieve(picUrl, path)

    except Exception as e:
        print(e)

def download(url, filepath):
    content = getTextByHeaders(url, headers)
    downloadPicFromContent(content, filepath)
