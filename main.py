import urllib.request as ur
import urllib.parse as up
import requests
import _thread as t
import json

def post(exportData,port):
    try:
        url="http://localhost:"+str(port)

        req=ur.Request(url,exportData)
        req.add_header("Content-Type","application/json")
        ur.urlopen(req)
    except:
        print('end')

def parse(url):
    print(url)

    header = {
        "User-Agent":"Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
#    '''
    request=ur.Request(url,headers=header)
    reponse=ur.urlopen(request).read()

    reponse=reponse.decode()
    '''

    reponse=requests.get(url,headers=header).text
    '''

    a=reponse.find("</title>")+8
    a=reponse.find("<center>",a)+8
    a=reponse.find("<h2>",a)+4
    b=reponse.find("</h2>",a)
    print(reponse[a:b])
    title=reponse[a:b]

    a=reponse.find("时间限制: </span>",b)+13
    b=reponse.find(" Sec",a)
    print(reponse[a:b])
    tme=int(reponse[a:b])

    a=reponse.find("内存限制: </span>",b)+13
    b=reponse.find(" MB",a)
    print(reponse[a:b])
    mmr=int(reponse[a:b])

    a=reponse.find("<h2>样例输入</h2>",b)+11
    if(a!=10):
        a=reponse.find("<pre class=content><span class=sampledata>",a)+42
        b=reponse.find("</span>",a)
        print(reponse[a:b])
        inn=reponse[a:b]

        a=reponse.find("<pre class=content><span class=sampledata>",b)+42
        b=reponse.find("</span>",a)
        print(reponse[a:b])
        out=reponse[a:b]
    else:
        inn=''
        out=''


    defaultPorts = [
        10045, # CP Editor
        1327, # cpbooster
        4244, # Hightail
        6174, # Mind Sport
        10042, # acmX
        10043, # Caide and AI Virtual Assistant
        27121, # Competitive Programming Helper
    ]

    exportData = {
        "name":title,
        "group":"题目列表",
        "url":url,
        "memoryLimit":mmr,
        "timeLimit":tme*1000,
        "tests":[
            {
                "input":inn.replace("\r",""),
                "output":out.replace("\r","")
            },
        ],
    }

    print(exportData)
    exportData=json.dumps(exportData).encode()

    for port in defaultPorts:
        t.start_new_thread(post,(exportData,port))

while True:
    cid=input("Contest id(-1代表无或退出):")
    if(cid=='-1'):
        num=input("Problem num(-1退出):")
        if(num=='-1'): break
        url = "http://218.5.5.242:9018/JudgeOnline/problem.php?id=" +num
        parse(url)
    else:
        frm=input('from:')
        end=input('to:')
        for i in range(int(frm),int(end)+1):
            url = "http://218.5.5.242:9018/JudgeOnline/problem.php?cid="+cid+"&pid=" +str(i)
            parse(url)

    

