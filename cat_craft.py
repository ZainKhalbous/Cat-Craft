"""
Zain Khalbous,
ENGINEER 1P13: Integrated Cornerstone Design Projects in Engineering   
Sam Scott, Fall 2024
this program able user to interact with cats by feeding, hitting, and giving them night of sleep. 
"""


import cat
"""Getting the names of cats"""
cat1=input("What is the name of yor cat?")
cat_1=cat.Cat(cat1)
cat2=input("What is the name of yor cat?")
cat_2=cat.Cat(cat2)
cat3=input("What is the name of yor cat?")
cat_3=cat.Cat(cat3)

c=[cat_1,cat_2,cat_3] #put them in list

choice=0
while choice!=4: #while loop for playing the methods from cat 
    i=1 
    for cats in c: # for loop to print catsk
        
        print(f"{i}. {cats}")
        i+=1
    
    print("1. Feed 2. Hit 3. Night 4. Quit\nChoice: ", end="")
    choice=int(input()) #get user method
    
    if choice!=4:
        print("Which cat? ", end="")
        cat_num=int(input()) #get number of cat
        #play each methon for choosen cat
        if cat_num==1:
            select=cat_1

        elif cat_num==2:
            select=cat_2
            
        elif cat_num==3:
            select=cat_3
            
        if choice==1:
            try:
                select.feed()
                
            except Exception:
                print(("Your cat is dead!"))
                
            
        elif choice==2:
            try:
                select.hit()
            except Exception:
                print(("Your cat is dead!"))
            
            
        elif choice==3:
            try:
                
                select.night()
                print(select.night())
            
            except Exception:
                print(("Your cat is dead!"))


    

        
    

