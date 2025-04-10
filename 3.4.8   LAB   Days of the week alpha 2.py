#Author: McCoy McPeter
#Date: 02/04/2025
#Version: apha 2 (Rev 1)

#Code Deficiency:
    #Required scope not met
    #subtract_days uses self.__day already updated by add_days to give a wrong result


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
    Days_of_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

    def __init__(self, day):
        self.__day = day 

    def __str__(self):
        if self.__day in self.Days_of_week:
            return self.__day
        else:
            raise WeekDayError
    
    #Find an nth day after the current day
    def add_days(self, n):
       self.__additional_days = n
       # Compute future nth day from the number of additional days
       if self.Days_of_week.index(self.__day) + self.__additional_days % 7 < len(self.Days_of_week[self.Days_of_week.index(self.__day):]): #Check if the nth day does not exceed the index of the list of week's days
           self.__day = self.Days_of_week[self.Days_of_week.index(self.__day) + self.__additional_days % 7]
       else:
           self.__day = self.Days_of_week[self.__additional_days % 7 - len(self.Days_of_week[self.Days_of_week.index(self.__day):])] #Cause cyclic scan through the list of week's days when the nth day exceeds the index of the week's days
       return self.__day
    


    #Find a previous nth day from the current day
    #Value of self.__day is updated by each class method.
    #Method calculates the previous nth day from the last updated value of self.__day
    def subtract_days(self, n):
        self.__previous_days = n
        self.__day = self.Days_of_week[ - (self.__previous_days % 7 - self.Days_of_week.index(self.__day)-1)]
        return self.__day


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
    print(weekday)
except WeekDayError:
    print("Sorry, I can't serve your request.")
    

