largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        numbers = int(num)
        if smallest is None or numbers < smallest:
            smallest = numbers
        if largest is None or numbers > largest:
            largest = numbers
    except:
        print ("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
