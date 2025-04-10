#Author: McCoy McPeter
#Date: 14/03/2025
#Version: apha 1 (Rev 0)

#Code Deficiency:
    #Required scope not met
    #method prints results instead of returning a internally updated value

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
       self.__future_nth_day = 0
       # Compute future nth day from the number of additional days
       if self.Days_of_week.index(self.__day) + self.__additional_days % 7 < len(self.Days_of_week[self.Days_of_week.index(self.__day):]): #Check if the nth day does not exceed the index of the list of week's days
           self.__future_nth_day = self.Days_of_week[self.Days_of_week.index(self.__day) + self.__additional_days % 7]
           print(self.__future_nth_day)
           
       else:
           self.__future_nth_day = self.Days_of_week[self.__additional_days % 7 - len(self.Days_of_week[self.Days_of_week.index(self.__day):])] #Cause cyclic scan through the list of week's days when the nth day exceeds the index of the week's days
           print(self.__future_nth_day)
           


    #Find a previous nth day from the current day
    def subtract_days(self, n):
        self.__previous_days = n
        self.__pass_nth_day = 0
        self.__pass_nth_day = self.Days_of_week[ - ((self.__previous_days -1) % 7) - self.Days_of_week.index(self.__day)]
        #self.__day = self.Days_of_week[- (self.__previous_days % 7)]
        #if self.Days_of_week.index(
        print(self.__pass_nth_day)

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
    

