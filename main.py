import urllib.request as ur
import urllib.parse as up
import urllib.error
import re
import json

while True:
    num=input("Problem num:")
    if(num=='-1'): break
    cid=input("Contest id:")
    if(cid=='-1'): url = "http://218.5.5.242:9018/JudgeOnline/problem.php?id=" +num
    else: url = "http://218.5.5.242:9018/JudgeOnline/problem.php?cid="+cid+"&pid=" +num

    header = {
        "User-Agent":"Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    request=ur.Request(url,headers=header)
    reponse=ur.urlopen(request).read()
    with open("jfaojif.html","wb") as f:
        f.write(reponse)

    reponse=reponse.decode()

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

    try:
        for port in defaultPorts:
            url="http://localhost:"+str(port)
            headers={
                "Content-Type": "application/json"
            }

            req=ur.Request(url,exportData)
            req.add_header("Content-Type","application/json")
            ur.urlopen(req)
    except:
        print('end')

