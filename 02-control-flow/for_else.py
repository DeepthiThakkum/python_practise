successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted three times and failed")

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted three times and failed")
