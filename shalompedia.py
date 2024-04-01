import time
from os import system


def checking_merge():
	print("This showed and it merged!")


def introduction():
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
	
	time.sleep(.5)
	system("clear")
	
	
	
	def timer_to_start_quiz(time_length):
		for t in range(time_length):
			print(f"Your questions begin in {time_length} second{'s' if time_length > 1 else ''}")
			time_length -= 1
			time.sleep(1)
			system("clear")
		begin_quiz()
			
	
	
	
	timer_to_start_quiz(3)


quiz_questions = '''What is the largest mammal in the world?
   a) Elephant
   b) Blue Whale
   c) ***Blue Whale***
   d) Giraffe
  
9. What is the main function of the heart?
   a) Pumping blood
   b) Digestion
   c) Breathing
   d) ***Pumping blood***
  
10. Who is the author of the Harry Potter series?
    a) J.R.R. Tolkien
    b) ***J.K. Rowling***
    c) Stephen King
    d) Suzanne Collins
  
3. What is the chemical symbol for gold?
   a) Au
   b) Fe
   c) ***Au***
   d) Cu'''

correct_and_wrong_answers = {}

def begin_quiz():
	global correct_and_wrong_answers
	
	for question_with_answer in quiz_questions.split("  \n"):
		
		question, options = question_with_answer.split("\n", 1)[0], question_with_answer.split("\n", 1)[1]
		question_unnumbered = question.split(".", 1)[1].strip() if "." in question[0:3] else question
		
		answer_index = len(correct_and_wrong_answers)
		print((f"\n{answer_index+1}. " if '***' in options else '') + question_unnumbered)
		
		
		if "***" in options:
			for option in options.split("\n"):
				if "***" in option:
					option = option.replace("***", "")
					correct_and_wrong_answers[str(answer_index+1)] = [option.strip()]
					
				print(option)
			user_selected_answer = input("  > ")
			correct_and_wrong_answers[str(answer_index+1)].append(user_selected_answer.strip())
			
		else:
			print("\n    Answer for this question is broken from database.\n    Kindly contact developer.")
			time.sleep(2)
		system("clear")
			
		

introduction()
#print(correct_and_wrong_answers)