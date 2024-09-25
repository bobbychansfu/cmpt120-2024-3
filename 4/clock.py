
end_time = input("enter end time: ") # i.e. 2:15
'''
index = end_time.find(":")
end_hour = end_time[:index]
end_min = end_time[index+1:]
'''

end = end_time.split(":")
end_hour = int(end[0])
end_min = int(end[1])

for h in range(end_hour + 1):  # i.e [0,1,2]
    for m in range(60):
        print(h,":",m)
        if (h == end_hour and m == end_min):
            break
