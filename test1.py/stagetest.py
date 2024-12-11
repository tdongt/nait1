from hans import *
f=open("info.txt","a",encoding="UTF-8")
mainapp()
#import os
def selecths():
    """f.write("name")
    f.write(" ")
    f.write("age")
    f.write(" ")
    f.write("ID")
    f.write(" ")
    f.write("score")
    f.write("\n")"""
    a=input("Your select :")
    if a=="EXIT":
        print("\033[H\033[J", end="")
        exitapp()
    else:
        a=int(a)
        if a==1:
            keyin(f)
            #a=input("Your select :")
            selecths()
            #i=os.system("cls")
        elif a==2:
            w=open("info.txt","r",encoding="UTF-8")
            stuu=seek(w)
            #print(stuu)
            #print(namekey)
            
            def seekt():
                name=input("Please input student's name who you need to seek!")
                index=0
                namekey=stuu.keys()
                #print(namekey)
                #namekey_list=list(namekey)
                while index<len(namekey):
                    namekey_list=list(namekey)
                    #print(namekey_list)
                    if name==namekey_list[index]:
                        index+=1
                        print(f"This student information:{stuu[name]}")
                        return
                    else:
                        index+=1
                print("System can't find this student's information,please check your input!")
                seekt()
                        
            seekt()
            
            x=0
            while (x==0):
                a=input("Seek continue?y/n")
                if a=="y":
                    seekt()
                else:
                    x=1
                    mainapp()
                    selecths()
        elif a==3:
            w=open("info.txt","r",encoding="UTF-8")
            preup=seek(w)
            print(preup)
            upinfo=upda(preup)
            print(upinfo)
            with open('info.txt', 'w', encoding='utf-8') as file:
                for key,value in upinfo.items():
                    line = ' '.join(value)
                    file.write(line + '\n')
            mainapp()
            selecths()

        elif a==4:
            w=open("info.txt","r",encoding="UTF-8")
            predele=seek(w)
            #print(predele)
            #m=open("info.txt","w",encoding="UTF-8")
            deleinfo=deledata(predele)
            print(type(deleinfo))
            # 打开文件，准备写入
            with open('info.txt', 'w', encoding='utf-8') as file: 
            # 遍历字典中的每个键值对
                for key,value in deleinfo.items():
            # 将键和值转换为字符串，并用空格分隔
                    line = ' '.join(value)
            # 将转换后的字符串写入文件，每个键值对占一行
                    file.write(line + '\n')
            mainapp()
            selecths()
        elif a==5:
            w=open("info.txt","r",encoding="UTF-8")
            showall(w)
            #a=input("Your select :")
            selecths()
        #elif a==6:
            #w=open("info.txt","r",encoding="UTF-8")
            #sco=sort(w)
            #print(sco)
        else:
            print("Your input has error,please checking and try again!")
            mainapp()
          

#a=input("Your select :")
selecths()
