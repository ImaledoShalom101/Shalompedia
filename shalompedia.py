import time
from os import system
classes = {"A": "JSS1", "B": "JSS2", "C": "JSS3", "D": "SS1", "E": "SS2", "F": "SS3"}
print("   Hello user! What is your name?")

user_name = input("    > ")
time.sleep(.5)

proceed_from_selecting_class = False
while not proceed_from_selecting_class:
	print(f"\n\nHello {user_name},\n	> Select your class")
	user_class = input("\n	" + "\n	".join(list(map(lambda one_class: f"{one_class}.  {classes[one_class]}", classes)))  + "\n\n\n	> ")
	try:
		print(f"{user_name} is in {classes[user_class.capitalize().strip().replace('.', '')]}")
		proceed_from_selecting_class = True
	except KeyError as ke:
		system("clear")
		print("Select correctly")
	
time.sleep(.3)
system("clear")


def checking_merge():
	print("This showed and it merged!")


def timer_to_start_quiz(time_length):
	for t in range(time_length):
		print(f"Your questions begin in {time_length} second{'s' if time_length > 1 else ''}")
		time_length -= 1
		time.sleep(1)
		system("clear")
		



timer_to_start_quiz(5)
