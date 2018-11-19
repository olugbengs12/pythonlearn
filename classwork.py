#program that takes count of numbers entered by a user and also notes the number, do a sum and return an average
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
