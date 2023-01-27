"""
File: py2.py
Author: Abdullah Sufian
Date: 11/18/2022
Lab Section: LAB 33
Email:  asufian1@umbc.edu
Description:  This program has multiple functions and we will use file IO and dictionaries to be able to use and operate the function needed.We have text files and data files for us to make sure these functions work. Like get first student to enter,if student in class, student count and many more functions
"""

# Comment the line below out if your have the load_dictionary function working!!
# Comment the line below out if your have the load_dictionary function working!!

from dataEntryP2 import fillAttendanceData

# Comment the line above out if your have the load_dictionary function working!!
# Comment the line above out if your have the load_dictionary function working!!


def list_all_students_checked_in_before(date, time, data):
    """
   this goes through data and checks which students checked in early 
   :param date: This is the day when the students checked in
   :param time: This is the time when students checked in
   :param data: this is the dictionary
   :return: This returns the list of names that arrived early
   """

#creates two lists
    name_list = []
    f_list = []
#this splits the time and assigns the hr,sec,min using the split
    new_time = time.split(':')
    hour = (new_time[0])
    minute = (new_time[1])
    seconds = (new_time[2])
#this uses a for loop from the data and goes through each time and and makes sure student checks in early
    for i in data:
            for i in data[i]:
                token = i.split(',')[0]
                if (token[3:5] <= minute) and (token[0:2] <= hour) and (token[6:8] < seconds) and (date in i):
                    f_list.append(i)

# uses a for loop which goes through the time and data and helps print out just the name 
    for i in f_list:
        second_value = i
        for i in data:
            if second_value in data[i]:
                name_list.append(i)

    return(name_list)

def list_all_students_checked_in(date, data):
    """
   This goes through the dictionary and checks which studnets has checked in and prints them out
   :param date: This is the day when the students checked in
   :param data: this is the dictionary
   :return: This returns all of the students who have checked in class
   """
#this assigns varibles to date and data and creates two lists
    old_date = date
    data_list = data
    date_list = []
    checked_in = []
# This uses a for loop to go through the data_list and checks if the old date is also in there and then appends it
    for i in data_list:
        for i in data_list[i]:
            if old_date in (i[:]):
                date_list.append(i)
#prints the list
    print(date_list)
#Uses a for loop to go trhough the dates, and again in the data and makes sure student is checked in onto that specific day
    for i in date_list:
        new_date = i
        for i in data_list:
            if new_date in (data_list[i]):
                checked_in.append(i)
#returns checked_in                
    return(checked_in)

def display_attendance_data_for_student(name, data):
    """
   this checks the name and attendance for one student and displays their attendance data
   :param name: This is the name of the student
   :param data: this is the dictionary data
   :return: This returns the list of the attendance data of a student
   """
    #this makes the list and assigns a value to the param
    attend_list = []
    second_attend_list = {}
    value = name
   
   #for loop to go through the dictionaries and if the name is in the dictionary we append to list
    for i in data:
        if value in (i[:]):
            attend_list.append(i)

# uses if statement to see if name is not in the dict it prints the statment below
    if name not in data:
        print("No student of this name in the attendance log") 
#uses for loop to go through the list of students and attendance and if the name is in the dict then it will append it to the dict a second time
    for i in attend_list:
        name = i
        for i in data:
            if name in (i[:]):
                second_attend_list[name] = data[name]
#goes through the list and prints the attendance data
    for i in second_attend_list:
        print(i, second_attend_list[i])


    
def load_dictionary(infile):
    """
   this goes through data and checks which students checked in early
   :param infile: this is the text file
   :return: This returns the data
   """
    #this makes a dictionary and then reads the line in the dict
    data = {}
    Lines = infile.readlines()
    # this goes through the lines and strips the lines and then it combines the name, and also combines the time
    for line in Lines:
        line = line.strip()
        name = line.split(', ')[0] + ', ' + line.split(', ')[1]
        time = line.split(', ')[2] + ', ' + line.split(', ')[3]
        #if statment for if name is not in the dictionary then the new name is in the dictt        
        if name not in data:
            data[name] = []
        #appends the new name and time to dict
        data[name].append(time)
    #returns the dict
    return data


def print_count(value):
    """
   this prints the amount of studnets in each dictionary 
   :param value: this is the value of the dict
   :return: This returns the amount of students in the count
   """
    #makes the lists and makes a count varible

    list_one = []
    list_two = []
    count = 0
    #goes through the param and appends to a list
    for i in value:
        list_two.append(i)
    #goes through list two and appends to list_one
    for i in list_two:
        list_one.append(i)

    for i in list_one:
        count += 1

    print("There were", count, "records for this query")

def get_first_student_to_enter(qdate,data):
    """
   this goes through data and checks which students checked in first
   :param qdate: This is the day when the students checked in
   :param data: this is the dictionary
   :return: This returns the first student to enter
   """
    #false statement to use for later
    student_one = False
    # Goes through the names in the dict keys and get the times    
    for name in data.keys():
        times = data[name]
        # Goes through the times and splits the time string and then assings the date and the time       
        for time in times:
            token = time.split(', ')
            date = token[1]
            timing = token[0]
            # if the param is equal to the date then it goes through the time to seconds conversion            
            if date == qdate:
                comps = timing.split(':')
                time_in_seconds = 0
                #This converts the time into int and then into seconds
                time_in_seconds += int(comps[0])*60*60
                time_in_seconds += int(comps[1])*60
                time_in_seconds += int(comps[2])
                #uses false statment to go through each student and compares the time and stops when the student with the lowest time is found                
                if student_one == False:
                    earliest_student = name
                    earliest_time = time_in_seconds
                    student_one = True
                else:
                    if time_in_seconds < earliest_time:
                        earliest_time = time_in_seconds
                        earliest_student = name
    #returns earliest student                        
    return(earliest_student)




def is_present(name,date,data):
    """
   this goes through data and returns true or false if student is present
   :param date: This is the day when the students checked in  
   :param name: This is the name of the student
   :param data: this is the dictionary
   :return: This returns true or false
   """
    #assigns dict key to variable
    datestime_present = data[name]
    # this goes through the key then splits for the date and if the date is in the dictionary it returns true     
    for i in datestime_present:
        date_present = i.split(', ')[1]
        if date == date_present:
            return True
    #if not in dict this returns false
    return False

def print_list(all_list):
    """
   this goes through the lists and prints out all lists
   :param all_list: This is just all of the list
   :return: This returns the list
   """

    # goes through the lists and prints the lists
    for element in all_list:
        print(element)



def load_roster(roster_file_name = 'rosters.txt'):
    """
   this goes through data and checks which students checked in early
   :param roster: This is the roster of the students in class
   :return: This returns the roster of the class
   """
    # makes a list
    data_Ros = []
    # opens the roster
    roster = open(roster_file_name,'r')
    #this goes through the roster and appends it into a list
    for i in roster:
        data_Ros.append(i.strip())
    return data_Ros

#helper function
# param data is just data for class
#roster is list of all classes students
#returns the dictionary{}
def makeAttendanceCount(data, roster):
    rosterAttendDict = {}
    for student in roster:
        if student in data.keys():
            rosterAttendDict[student] = len(data[student])
        else:
            rosterAttendDict[student] = 0
            
    return(rosterAttendDict)    


    """
    This gets the the students attendance count and shows whos in both class
    :param data: this is the dictionary
    :return: This returns the list of names that arrived early
    """
def list_student_attendance_count(q_numClasses, rosterAttendDict):
    students_who_attended = []
    for student in rosterAttendDict.keys():
        if rosterAttendDict[student] == q_numClasses:
            students_who_attended.append(student)
    return students_who_attended


def connect_to_data_file(filename):
    # will return connection to data file
    infile = ""

    try:
        #infile = open("data.txt", "r")
        #infile = open("dataAllShow1stClass.txt", "r")
        #infile = open("dataAllShow1stAnd2ndClass.txt", "r")
        infile = open(filename, "r")
    except FileNotFoundError:
        print("file was not found, try again")

    return infile  # connection with the file

if __name__ == '__main__':

    infile = connect_to_data_file("dataAllShow1stAnd2ndClass.txt")
    if(infile):
        print("connected to data file...")
    else:
        print("issue with data file... STOP")
        exit(1)

    data = load_dictionary(infile)
    print(data)
    # ************************
    # OR MANUALLY!!!
    # ************************

    # just making sure the data collected is good
   # print_dictionary(data)

    #print("********* Looking up Student Attendance Data ***********")
    #display_attendance_data_for_student("Morrison, Simon", data)
    #display_attendance_data_for_student("Arsenault, Al", data)

    #print("********* Looking to see if Student was present on date ***********")
    #print(is_present("Bower, Amy", "11/5/2022", data))
    #print(is_present("Bower, Amy", "11/17/2022", data))

    # display when students first signed in
    print("**** Students present on this date ****")
    result = list_all_students_checked_in("11/5/2022", data)
    print_list(result)
    print_count(result)

    print("**** Those present on date & before a time assigned ****")
    result = list_all_students_checked_in_before("11/5/2022", "08:55:04", data)
    print_list(result)
    print_count(result)
    roster = load_roster('rosters.txt')
    rosterAttendDict = makeAttendanceCount(data, roster)
    # list the good students that showed up both days
    print("**** Those who attended BOTH classes ****")
    
    students = (list_student_attendance_count(2, rosterAttendDict))
    print('Students who attended both classes: ')
    print(students)
    print('Number of records = {}'.format(len(students)))
    
    
    # list the  students that showed up ONE of the days
    print("**** Those who attended ONE class ****")
    students = (list_student_attendance_count(1, rosterAttendDict))
    print('Students who attended both classes: ')
    print(students)
    print('Number of records = {}'.format(len(students)))
    
    # list the  students that have not shown up
    print("**** Those who have NOT attended a SINGLE class ****")
    students = (list_student_attendance_count(0, rosterAttendDict))
    print('Students who attended both classes: ')
    print(students)
    print('Number of records = {}'.format(len(students)))

    
