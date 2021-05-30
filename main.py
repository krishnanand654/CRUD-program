import os                         #clear the screen

from msvcrt import getch          #user input to continue

print("\n\n\n\n\t\t\t\t*****************C-R-U-D Program*****************\n\n\n")
print("press any key to start")
getch()

#create an empty file if it doesnot exit
f=open("data.txt",'a')
f.close()


#menu
x=0
while x != 5:
    os.system('cls')
    print("\n-----MENU------\n1.Create \n2.Read \n3.Update\n4.Delete\n5.Exit")
    x=int(input("\nEnter your choice  :  "))
    
    
    #create
    if x == 1:
        
        os.system('cls')
        a=str(input("\nEnter Id : "))
        b=str(input("\nEnter Name : "))
        
        f=open("data.txt",'r')
        data=f.readlines()
        f.close()
        
    #eleminating duplication 
        flag=0
        f=open("data.txt",'r')
        for lines in data:
            if b in lines:
                flag=1
                break
        f.close()
        if flag==1:                             #if flag is 1 the item is already in the file.
            print("\nId already exist")
            time.sleep(1)
        if flag==0:                             # if flag is 0 the item is not already present in file and can write to the file
            f=open("data.txt",'a')
            f.write(a)
            f.write("\t"+b+"\n")
            print("\ndata added successfully\n")
            getch()
            f.close()
        
       
        
#read
    if x == 2:
        
        os.system('cls')
        
    #copying
        f=open("data.txt",'r')
        data=f.readlines()
        f.close()

    #sorting
        data.sort()

    #rewriting
        f=open("data.txt",'r+')
        f.writelines(data)
        f.close()

    #reading
        f=open("data.txt",'r')
        print("Id\tName\n--------------------")
        print( f.read())
        f.close()

        print("press any key to go back to MENU")
        getch()

        
    #update
    if x == 3:
        
        os.system('cls')
        
    #searching
        f=open("data.txt",'r')
        print("Id\tName\n--------------------")
        print( f.read())
        f.close()
        s=str(input("\nEnter id of data to be modified : "))
        f=open('data.txt','r')
        flag=0
        index=0

        for line in f:
            index=index+1
            if s in line:
                flag=1
                break
        if flag==0:
            print("\n Id "+s+" not found\n")
            time.sleep(1)
        if flag == 1 :
    #copying
            f=open('data.txt','r')
            data=f.readlines()
            f.close()

    #deleting old data
            del data[index-1]
            f=open('data.txt','w')
            f.writelines(data)
            f.close()

    #read update info
            a=str(input("\nEnter Id : "))
            b=str(input("\nEnter Name : "))
            d=(a+"\t"+b+"\n")
            data.append(d)

    #rewriting
            f=open('data.txt','w')
            f.writelines(data)
            f.close()
            print("\nData updated")
            getch()

            
    #delete
    if x == 4:
        
        os.system('cls')
        
    #searching
        f=open("data.txt",'r')
        print("Id\tName\n--------------------")
        print( f.read())
        f.close()
        s=str(input("\nEnter id to be deleted : "))
        f=open('data.txt','r')
        flag=0
        index=0
        for line in f:
            index=index+1
            if s in line:
                flag=1
                break
        if flag==0:
            print("\n Id "+s+" not found\n")
        if flag == 1 :
    #copying
            f=open('data.txt','r')
            data=f.readlines()
            f.close()

    #deleting
            del data[index-1]
            print("\nData deleted")
            getch()

    #rewriting
            f=open('data.txt','w')
            f.writelines(data)
            f.close()

            
    #exit         
    if x == 5:
        break



