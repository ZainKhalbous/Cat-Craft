"""
Zain Khalbous,
400546696, engineering 1
ENGINEER 1P13: Integrated Cornerstone Design Projects in Engineering   
Sam Scott, Fall 2024
This file contain the model cat, class cat and its attributes and methonds
 
"""

import random

class Cat:
    """Cat class is containing  number of health, name, 
    number of fish in cat, 
    whether tame or wild, and whether alive or dead
    """
    def __init__(self ,name):
        """__init__ method is to take the name of cat the store its information """
        self.__type="Wild"
        self.__current="Alive"
        self.__name=name
        self.__health=2.0
        self.__fish=0
        
    def feed(self):
        """feed method is to feed a cat so if can alive a fish would be add along with health"""
        random_type=random.randint(1,2)
       
        if self.__current=="Alive": #you cannot feed a dead cat so if alive
            if random_type==1: #if feeded, there is a 50% change to be tame
                self.__type="Tame"
            
            self.__fish+=1
                
            if self.__health<4: #max number of health is 4 
                self.__health+=1
                
                
            if self.__fish>3: #if cat has more than 3 fish, it would be dead and health 0
                self.__current="Dead"
                self.__health=0
                
        if self.__current=="Dead" and self.__fish>3:
            raise Exception
    
    
    def hit(self):
        
        
        """this function is to hit a cat, with decreasing number of fish by 1 and health by 1.5
        Also cat is turn to wild
        """
    
        if self.__health>0:
            self.__health-=1.5
        self.type="Wild"
        if self.__health<=0:
            self.__health=0
            self.__current="Dead"
            
        if self.__current=="Dead":
            raise Exception
           
    def night(self):
        """this function is to let the cat sleep, with subtracting a fish 
        also if cat is tame and fish>0 it return string
        """
        if self.__current=="Alive" and self.__fish>0:# if alive and has fish then subtract fish
            self.__fish-=1 
            if self.__fish<=0: # change cat to wild if fish is zero 
                self.__type="Wild"
            if self.__type=="Tame" and self.__fish>0: #return string if alive and fish>0
                gift=f"{self.__name} left you a gift!"
                return gift
        if self.__current=="Dead":
                raise Exception
            
    def __str__(self):
        """this function is to report the information of cats"""
        report=f"{self.__current} {self.__type} Cat {self.__name}: {self.__health} health, {self.__fish} fish"
        return report
    