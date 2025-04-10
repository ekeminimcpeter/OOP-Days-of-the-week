#Author: McCoy McPeter
#Date: 08/04/2025
#Version: beta 1 (Rev 4)
#Acknowledgemen: Thanks to ChatGPT for reviewing code and giving suggestion for improvement.
#ChatLink: https://chatgpt.com/share/67f4208f-4bd8-800a-8d0d-0ff9ff2fe7c2

#Improvement:
    #Hiden bug fixed:
        #Refenced day is set in constructor
    #Inproved validation logic:
        #Validation is in constructor and invalid days don't go unnoticed until it's printed
    #Eliminated Redundant variables
    #Circular math:
        #Wrap around is with % feature
    

class WeekDayError(Exception):
    pass
	

class Weeker:
    __Days_of_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") #acceptable list and order of week days

    def __init__(self, day):
        if day not in self.__Days_of_week:
            raise WeekDayError
        self.__day_index = self.__Days_of_week.index(day)
       
    def __str__(self):
            return self.__Days_of_week[self.__day_index]
            
            
       
    #Find an nth day after the current day
        
    def add_days(self, n): #n = number of additional days
        self.__day_index = (self.__day_index + n) % 7 #Cause cyclic operation with % feature through the list of week's days when the nth day exceeds the index of the week's days
    
    #Find a previous nth day before the current day
    #Method prints the current day when the previous nth day is 1
    
    def subtract_days(self, n): #n = number of previous days
        self.__day_index = (self.__day_index - n) % 7 #Cause cyclic operation with % feature through the list of week's days when the nth day exceeds the lower index of the week's days
    
try:
    weekday = Weeker('Mon')#Prim.Testdata "Mon"
    print(weekday)
    weekday.add_days(10)#Prim.Testdata 15
    print(weekday)
    weekday.subtract_days(15)#Prim.Testdata 23
    print(weekday)
    weekday = Weeker('Monday')#Prim.Testdata "Monday"
except WeekDayError:
    print("Sorry, I can't serve your request.")
    

