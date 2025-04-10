#Author: McCoy McPeter
#Date: 06/04/2025
#Version: apha 3 (Rev 2)
#Acknowledgemen: Thanks to ChatGPT for reviewing code and giving suggestion for improvement.
#ChatLink: https://chatgpt.com/share/67f4208f-4bd8-800a-8d0d-0ff9ff2fe7c2

#Code Deficiency:
    #Hidden bug:
        #subtract_days() relied on self.__reference_day which was set in add_days()
        #That means it would break if someone called it before add_days()
    #Redundant variables        
    #Poor validation logic:
        #Validation was inside __str__(), but it should have been in __init__() — otherwise, invalid days go unnoticed until it's printed.
    #Circular math:
        #“manually” wrap around the week while % could do that neatly in one line.

'''
Your task is to implement a class called Weeker. Yes, your eyes don't deceive you – this name comes from the fact that objects of that class will be able to store and to manipulate the days of the week.

The class constructor accepts one argument – a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:

Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:

    objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
    the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
    all object's properties should be private;
Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.

Expected output

Mon
Tue
Sun
Sorry, I can't serve your request.

'''

class WeekDayError(Exception):
    pass
	

class Weeker:
    Days_of_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") #acceptable list and order of week days

    def __init__(self, day):
        self.__day = day
       
    def __str__(self):
        if self.__day in self.Days_of_week:
            return self.__day
            
        else:
            raise WeekDayError
       
    #Find an nth day after the current day
    #Implement manual wrapping around (circular operation)
    def add_days(self, n):
       self.__additional_days = n
       self.__reference_day = self.__day
       
       # Compute future nth day from the number of additional days
       if self.Days_of_week.index(self.__reference_day) + self.__additional_days % 7 < len(self.Days_of_week[self.Days_of_week.index(self.__reference_day):]): #Check if the nth day does not exceed the index of the list of week's days
           self.__future_nth_day = self.Days_of_week[self.Days_of_week.index(self.__reference_day) + self.__additional_days % 7]
           self.__day = self.__future_nth_day
       else:
           self.__future_nth_day = self.Days_of_week[self.__additional_days % 7 - len(self.Days_of_week[self.Days_of_week.index(self.__reference_day):])] #Cause cyclic scan through the list of week's days when the nth day exceeds the index of the week's days
           self.__day = self.__future_nth_day
       return self.__day
    
           
    
    #Find a previous nth day from the current day
    #Implement manual wrapping around (circular operation)
    
    #Previous nth day is calculated starting from the current day based on scope.
    #Method prints the current day when the previous nth day is 1
    def subtract_days(self, n):
        self.__previous_days = n
        self.__pass_nth_day = self.Days_of_week[ - (self.__previous_days % 7 - self.Days_of_week.index(self.__reference_day)-1)]
        self.__day = self.__pass_nth_day
        return self.__day
    
try:
    weekday = Weeker('Mon')#Prim.Testdata "Mon"
    print(weekday)
    weekday.add_days(15)#Prim.Testdata 15
    print(weekday)
    weekday.subtract_days(23)#Prim.Testdata 23
    print(weekday)
    weekday = Weeker('Monday')#Prim.Testdata "Monday"
    print(weekday)
except WeekDayError:
    print("Sorry, I can't serve your request.")
    

