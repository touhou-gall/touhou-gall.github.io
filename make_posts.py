from datetime import datetime
import os
import shutil
def Imagefiles(path):
    res = []
    exef=["jpg","png","gif","JPG","PNG","GIF"]
    try :
        for root, dirs, files in os.walk(path):
            del dirs
            rootpath = os.path.join(os.path.abspath(path), root)

            for file in files:
                filepath = os.path.join(rootpath, file)
                if filepath[-3:] in exef:
                    res.append(filepath)
    except:
        pass

    return res
now = datetime.now()
filepath=input("이미지 폴더 위치 입력하세요. ")
tags=input("입력할 태그를 입력하세요. (입력방식: 마리사, 앨리스, 레이무)")
title=input("제목을 입력하세요. ")

tags_=tags.split(', ')
fp = open('tags_list.txt','r')
have_tags=fp.read().split('\r\n')
fp.close()
for tag in tags_:
    if tag in have_tags:
        pass
    else :
        fp=open('tags_list.txt','a')
        fp.write('\n'+tag)
        fp.close()
        fp=open('_tags/'+tag+'.md','w')
        fp.write(("---\nname: "+tag+"\ntitle: "+tag+"\nimage: /files/covers/opensource.jpg\n---\n").encode('utf-8').decode('utf-8'))
        fp.close()
filename='%4d-%02d-%02d' % ( now.year, now.month, now.day)
filename=filename+'-'+title+'.md'
fp=open('_posts/'+filename,'w')
fp.write('---\ntitle:  \"'+title+'\"\ntags: '+tags+'\n---\n')
filelist=Imagefiles(filepath)
for i in filelist:
    filename=i.split('\\')[-1]
    shutil.copy(i,"content")
    fp.write('[image](\"../content/'+filename+'\")\n')
    
fp.close()

"""
---
title:  "Exclude Post from Search Index"
search: false
tags: 마리사
last_modified_at: 2018-02-19T08:05:34-05:00
---
"""



