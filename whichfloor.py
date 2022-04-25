maximum_stories = 10

num = int(input("On what floor of the building is your office? "))

while num > maximum_stories:
	num = int(input("You entered: " + str(num) + " but there are only " + str(maximum_stories) + " floors in this building. Try again... "))

print("Congrats! You work on floor: " + str(num))