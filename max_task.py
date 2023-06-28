from datetime import datetime

list = []

n = int(input("Please enter the count of task must be done : \n"))

# get start and end time as input from user

for i in range(n):
    dic={}
    start_time = input("please enter the start time in (yyyy/mm/dd hh:mm:ss) => \n")
    start = datetime.strptime(start_time, "%Y/%m/%d %H:%M:%S")
    terminate_time = input("please enter the terminate time in (yyyy/mm/dd hh:mm:ss) => \n")
    terminate = datetime.strptime(terminate_time, "%Y/%m/%d %H:%M:%S")
    dic.update({"start time" : start, "terminate time" : terminate})
    list.append(dic)

# sort by termination time

for i in range(n):
    for j in range(i,n):
        if (list[i]["terminate time"] > list[j]["terminate time"]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp


# selecting tasks

selected = []
selected_count = 0
T = datetime.fromisoformat("0001-01-01 00:00:00")

for i in range(n):
    if list[i]["start time"] >= T :
        dic2 = {}
        selected_count = selected_count + 1
        start = datetime.strftime(list[i]["start time"] , "%Y-%m-%d %H:%M:%S")
        terminate = datetime.strftime(list[i]["terminate time"] , "%Y-%m-%d %H:%M:%S")
        dic2.update({"start time" : start, "terminate time" : terminate})
        selected.append(dic2)
        T = list[i]["terminate time"]

# Output selected tasks

for i in range(selected_count):
    print("selected task" , (i+1) ," :\n" , selected[i])

print("-----------------------------------------------------------------------------------")
print("total number of tasks can be done : " , selected_count)