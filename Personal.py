file = open(r"C:\Users\glush\Desktop\Python Files\Reminder.txt", "r")
data = file.read()
datalist = data.split("\n")
if datalist[0] == "":
    datalist.pop(0)
if datalist[-1] == "":
    datalist.pop(-1)
print(datalist)
file.close()
while True:
    file = open(r"C:\Users\glush\Desktop\Python Files\Reminder.txt", "w")
    action = input("What action you want to do? (Add, Delete, Change, Clear, Quit)\n")
    if action == 'Add':
        file = open(r"C:\Users\glush\Desktop\Python Files\Reminder.txt", "w")
        adding = input("What do you want to add?\n")
        datalist.insert(1, adding)
        print(datalist)
        file.write('\n'.join(datalist))
    if action == 'Delete':
        file = open(r"C:\Users\glush\Desktop\Python Files\Reminder.txt", "w")
        print(datalist)
        deleting = input("What do you want to delete?\n")
        if deleting in datalist:
            datalist.remove(deleting)
            print(datalist)
            file.write('\n'.join(datalist))
        else:
            print("There is no thing like that in the list, try again.\n")
            continue
    if action == 'Change':
        file = open(r"C:\Users\glush\Desktop\Python Files\Reminder.txt", "w")
        print(datalist)
        changing = int(input("What do you want to change? (from 0)\n"))
        changing2 = input("To what do you want to change?\n")
        if datalist:
            datalist[changing] = changing2
            print(datalist)
            file.write('\n'.join(datalist))
        else:
            print("There is no thing like that in the list, try again.\n")
            continue
    if action == 'Clear':
        file = open(r"C:\Users\glush\Desktop\Python Files\Reminder.txt", "w")
        print(datalist)
        changing = input("Are you sure?\n")
        if changing in "Yes":
            datalist.clear()
            print(datalist)
            file.write('\n'.join(datalist))
    if action == 'Quit':
        file.write('\n'.join(datalist))
        print("Bye!")
        break


    


