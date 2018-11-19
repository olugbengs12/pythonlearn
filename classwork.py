total = 0
count = 0
average = 0
while True:
    number = input("Enter a number:")
    try:
        if number == "done":
            break
        total += float(number)
        count += 1
        average = total / count
    except:
        print ("Invalid input")
print ("total:", total, "count:", count, "average:", average)
