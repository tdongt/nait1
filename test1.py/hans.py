
def exitapp():
    print("########################################\n")
    print("#########Thanks for your using!#########\n")
    print("################bye bye#################\n")
    print("########################################\n")
def mainapp():
    print("########################################\n")
    print("#######***Student info manager***#######\n")
    print("#########1.key in students'info#########\n")
    print("#########2.seek students'info###########\n")
    print("#########3.update students'info#########\n")
    print("#########4.delete students'info#########\n")
    print("#####5.show all students'infomation#####\n")
    print("#########6.students'score sort##########\n")
    print("##########input EXIT for exiting########\n")
    print("####Please according to your require####\n")
    print("#select and input a number in 1/2/3/4/5#\n")
    print("########################################\n")

def keyin(f):
    x=1
    while(x==1):
        #f.write("\n")
        f.write(input("Please input student name:"))
        f.write(" ")
        f.write(input("Please input student age:"))
        f.write(" ")
        f.write(input("Please input student sex:"))
        f.write(" ")
        f.write(input("Please input student number:"))
        f.write("\n")
        a=(input("Key in more student info?y/n"))
        if a=="n":
            x=0
            f.close()
    mainapp()

def showall(f):
    a="n"
    while (a=="n"):
        for line in f:
            line=line.strip()
            linex=line.split(" ")
            print(linex)
        a=input("Back to main interface?y/n")
        if a=="y":
            mainapp()
            f.close()
def sort(f):
    scoinfo=[]
    for line in f:
        line=line.strip()
        linex=line.split(" ")
        scoinfo.extend(linex)
    i=0
    print(scoinfo)
    sco={}
    for i in range(0, len(scoinfo), 4):
        group=scoinfo[i:i+4]
        students={group[3]:group}
        print(students)
    f.close()
    return sco
def seek(f):
    stuinfo=[]
    for line in f:
        line=line.strip()
        linex=line.split(" ")
        stuinfo.extend(linex)
    i=0
    stu={}
    for i in range(0, len(stuinfo), 4):
        group=stuinfo[i:i+4]
        students={group[0]:group}
        stu[group[0]]=group
    #print(stu)
    #namekey=stu.keys()
    #print(namekey)
    f.close()
    return stu
    
def deledata(da):
    #print(da)
    name=input("Please input student's name who you want to delete!")
    namekey=da.keys()
    #print(namekey)
    key_list=list(namekey)
    print(key_list)
    index=0
    while index<len(key_list):
        if name==key_list[index]:
            index+=1
            print("Finding student!")
            dele=da.pop(name)
            print(f"Deleting student information:{dele}")
            return da
        else:
            index+=1
    #if index>len(key_list):
        #print("System can't find this student's information,please check your input!")
def upda(ta):
    name=input("Please input student's name who you want to update!")
    nakey=ta.keys()
    print(nakey)
    nakey_list=list(nakey)
    print(nakey_list)
    index=0
    while index<len(nakey_list):
        if name==nakey_list[index]:
            index+=1
            x=input("Please input name:")
            y=input("Please input age:")
            z=input("Please input sex:")
            w=input("Please input number:")
            ta[name]=[x,y,z,w]
            ta.update({x: ta.pop(name)})
            return ta
        else:
            index+=1
    


   

     
    

        
        
                

        
    
    




