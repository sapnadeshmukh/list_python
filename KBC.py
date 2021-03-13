question_list=["(*)How many continents are there?",
		"(*)what is the capital of india?",
		"(*)NG me kon se course pdhaye jate hai?"]

first_option=["(1)four","(1)chandigardh","(1)software engineer"]

second_option=["(2)nine","(2)bhopal","(2)counselling"]

third_option =["(3)seven","(3)chennai","(3)toursim"]

four_option =["(4)eight","(4)delhi","(4)agriculture"]

answer_key=[3,4,1]


lifeline =[["(1)seven","(2)nine"],
["(1)bhopal","(2)delhi"],["(1)softaware engineer"],["(2)counselling"]]
	 
lifeline_key=[1,2,1]
index=0
c=0
while index<len(question_list):
	print(question_list[index])
	print(first_option[index])
	print (second_option[index])
	print (third_option[index])
	print (four_option[index])
	a=int(input("Enter your answer:-"))
	if answer_key[index]==a:
		print("Congrats!your answer is correct")
	elif a==5050:
		if c==0:
			print( question_list[index])
			print( lifeline[index])
			c=c+1
        
			user=int(input("enter your answer:---"))
			if user==lifeline_key[index]:
				print("Congrats!!")
			else:
				print("You have quit the game")
				break
		else:
			print("You have already used 5050 lifeline ")
			user=int(input("enter your answer:---"))
			if answer_key[index]==a:
				print("Congrats!your answer is correct")
			else:
				print("Wrong answer!!")
				break


	else:
		print("Wrong answer!!")
		break
	index=index+1