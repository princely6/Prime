largest = None
smallest = None
while True:
    sp = input("Enter a number: ")
    if sp == "done" : break
    try:
        num = float(sp)
    except:
# print "Please enter a number as input or \'done\'"
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = num
    if largest is None:
        largest = num
    elif num < smallest :
        smallest = num
def done(largest,smallest):
    print ("Maximum is", int(largest))
    print ("Minimum is", int(smallest))
done(largest,smallest)
