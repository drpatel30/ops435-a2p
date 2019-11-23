#!/usr/bin/env python3
# Student ID: c7-drpatel30
'''OPS435 Assignment 1 - Fall 2019
Program: a2_class.py 
Author: "Dhyeykumar Patel"
The python code in this file (a1_class.py) is original work written by
"Dhyeykumar Patel". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
class Date:
    ''' Class creats Date object with Year, Month , and Day attributed
        available Methods:
        date_to_days(): calculates no of days from epoch date
        to given date.  
        Day_of_week: Returns day of week
         
    '''
    def __init__(self,year,month,day):
        '''constructor for time object''' 
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        '''return a string representation for the object self'''
        return '%.4d/%.2d/%.2d' % (self.year, self.month, self.day)
    def __repr__(self):
        '''return a string representation for the object self'''
        return '%.4d-%.2d-%.2d' % (self.year, self.month, self.day)
#############3 add method to support + operator overload   
    def __add__(self, d2):
        '''
        Function to add a Date object or Integer to a Date object while using '+' operater
        '''
        if type(d2) == int:
            a=self.date_to_days()
            c=a+d2
            day_1=c   
            def days_to_date(c):
                c1 = 0
                c2 = 0
                d = 1
                new_year = 1970
                while d > 0:
                    if c > 0 and c < 365:
                        break 
                    else:
                        if ( new_year % 4 == 0 and new_year % 100 != 0 or new_year % 400 == 0 ):
                            c = c - 366    								     															
                            c1+=1
                            new_year +=1
                            d = c
                        else:    
                            c= c- 365 
                            c2+= 1
                            new_year +=1 
                            d = c 
                new_year = new_year
                rdays = day_1 - ((c1 * 366) + (c2 * 365)) 
                if 	( new_year % 4 == 0 and new_year % 100 != 0 or new_year % 400 == 0 ):
                    list_a = [31, 29 , 31, 30 ,31,30,31,31,30,31,30,31]
                else:        
                    list_a = [31, 28 , 31, 30 ,31,30,31,31,30,31,30,31]    
                c3 = 0
                while True: 
                    if rdays < 0:
                       break  
                    elif rdays > 0:
                        if rdays > list_a[c3] :
                            rdays = rdays - list_a[c3]
                            if rdays == list_a[c3]:
                                c3+=1
                                rdays=list_a[c3]
                                break	   
                            elif c3>11:                   
                                c3=0
                                rday=0
                                break   
                            elif rdays < list_a[c3]:
                                c3+=1
                                rdays=rdays
                                break
                            else:
                                c3 +=1
                        elif rdays < list_a[c3]:
                            c3=0
                            rdays=rdays+1
                            break
                    else:
                        c3=0
                        rdays=1
                        break
                return Date(new_year,c3+1,rdays)
            return days_to_date(c)    
        else:
            a=self.date_to_days()
            b=d2.date_to_days()
            c=a+b
            return c
################ Sub method to support - operation overload               
    def __sub__(self, d2):
        '''
        Subtract a date object or an integer from a Date object   
        '''
        if type(d2) == int:
            a=self.date_to_days()
            c=a-d2
            def days_to_date(c):
                x=c//365
                #x, rem_days= divmod(c,365)
                new_year = 1970 
                d = 0
                z=0
                for a in range(0,x):
                    if ( new_year % 4 == 0 and new_year % 100 != 0 or new_year % 400 == 0 ):	
                         c = c - 366
                         if c > 0:
                             new_year +=1
                             d=c
                    else:
                         c = c - 365
                         if c > 0:
                             new_year += 1
                             d = c
                rem_days = d
                if rem_days != 0:
                    if 	( new_year % 4 == 0 and new_year % 100 != 0 or new_year % 400 == 0 ):
                        list_a = [31, 29 , 31, 30 ,31,30,31,31,30,31,30,31]
                    else:        
                        list_a = [31, 28 , 31, 30 ,31,30,31,31,30,31,30,31]    
                    count=0
                    for one in list_a: 
                        rem_days= rem_days - one
                        if rem_days > 0:
                            count+=1
                            rem_day=rem_days
                else:
                    count=1
                    rem_day = 1 
                return Date(new_year,count + 1,rem_day + 1)
            return days_to_date(c)  
        else:
            a=self.date_to_days()
            b=d2.date_to_days()
            c=a-b
            return c   

############ Leap year Function
    def leap_year(self):
        '''
        Function determined if the year is leap year or not and
        determines maximum days for february
        '''   
        if (  self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0 ):
            return 29
        else:
            return 28
########### Days in month folder
    def days_in_mon(self):
        ''' returns list of the days in month'''
        feb_max=self.leap_year()
        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        return list(mon_max.values())
########### date_to_Days converter        
    def date_to_days(self):
        '''Calculates no of Days from Epoch date'''
        new_year= self.year - 1970
        b = 0
        c = 0
        d = 0
        for a in range(1970,self.year):
            if ( a % 4 == 0 and a % 100 != 0 or a % 400 == 0 ):
                b = b+1
            else:
                c = c+1
        e=self.month - 1
        list_a = self.days_in_mon()
        for a in list_a[0:e]:
            d=d+a        
        days = (b * 366) + (c * 365) + d + (self.day - 1)  
        return days
############## Days to date function    
    def days_to_date(c):
        '''Calculates Date from Epoch date after given number of days '''
        x= c%365
        new_year = x + 1970
        d = 0
        for a in range(1970,new_year):
            if ( a % 4 == 0 and a % 100 != 0 or a % 400 == 0 ):	
                d+=1        
        rem_days = c-(((x-d) * 365)+(d*366))
        if rem_days != 0:
            if 	( new_year % 4 == 0 and new_year % 100 != 0 or new_year % 400 == 0 ):
                list_a = [31, 29 , 31, 30 ,31,30,31,31,30,31,30,31]
            else:        
                list_a = [31, 28 , 31, 30 ,31,30,31,31,30,31,30,31]    
            count=0
            while rem_days > 0:
                for one in list_a: 
                    rem_days= rem_days - one
                    count+=1
        else:
            count=1
            rem_days = 1 
        return Date(new_year,count,rem_days)    
############# Tomorrow Function    
    def tomorrow(self):
        '''d.tomorrow() -> Date object for next day
        tomorrow() takes all attributes from self object and calculates next date
        e.g. d.tomorrow() -> '2018/01/01'
        '''
        mon_max = self.days_in_mon()
        tmp_day = self.day + 1
        if tmp_day > mon_max[self.month - 1]:
            to_day = tmp_day % mon_max[self.month - 1]
            tmp_month = self.month + 1
        else:
            to_day = tmp_day
            tmp_month = self.month + 0
        if tmp_month > 12:
            to_month = 1
            new_year = self.year + 1
        else:
            to_month = tmp_month + 0
            new_year = self.year
        next_date = Date(new_year,to_month,to_day) 
        return next_date
############## Yesterday Function
    def yesterday(self):
        '''d.yesterday() -> Date object for previous day
        yesterday() takes all attributes from self object and calculates previous date
        d = 2018-01-01
        e.g. d.yesterday() -> 2017-12-31
        '''        
        mon_max = self.days_in_mon()
        if self.day == 1 and self.month != 1:
            tmp_month = self.month - 1
            tod_day = mon_max[tmp_month-1]
            tod_month = tmp_month
            tm_year = self.year
        elif self.day == 1 and self.month == 1:
            tmp_month = 12
            tod_day = mon_max[tmp_month-1]
            tod_month = tmp_month
            tm_year = self.year - 1
        else:    
            tod_day = self.day - 1
            tod_month = self.month + 0
            tm_year = self.year	
        next_date = Date(tm_year,tod_month,tod_day) 
        return next_date
############# Day of week function
    def day_of_week(self):
        '''
        Calculates day of week using reference from Epoch date
        '''
        days=self.date_to_days()
        dx,d1=divmod(days,7)
        d1=d1+4
        return d1	
