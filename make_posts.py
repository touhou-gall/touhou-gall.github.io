from datetime import datetime
now = datetime.now()
filepath=input("이미지 폴더 위치 입력하세요. ")
tags=input("입력할 태그를 입력하세요. (입력방식: 마리사, 앨리스, 레이무)")
title=input("제목을 입력하세요. ")

tags=tags.split(', ')
fp = open('tags_list.txt','rb')
have_tags=fp.read().split(b'\r\n')
fp.close()
for tag in tags:
    if tag in have_tags:
        pass
    else :
        fp=open('tags_list.txt','ab')
        fp.write('\n'+tag)
        fp.close()
        fp=open('_tags'+tag+'.md','w')
        fp.write("---\nname: "+tag+"\ntitle: "+tag+"\nimage: /files/covers/opensource.jpg\n---\n")
        fp.close()
fp=open()



