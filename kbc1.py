 
question_list = ["Who founded facebook?",
                 "What is your age?",
                 "How many members are there in your family?",
                 "What is your family income?",
                 "Who won the first cricket world cup?",
                 "Who won the first hockey championship?",
                 "Who is knowmn as the father of the nation?",
                 "Who is the first president of india?",
                 "Who is the nightingale of india?",
                 "who is known as the God of cricket?",
                 "Who is the first man to step on moon?",
                 "How many days in a leap year?",
                 "What is the main objective of clean india mission?",
                 "Where is the main headquarters of ISRO?",
                 "How many matches that sachin played in test cricket?"]

options1_list = ["Nitin", "20", "5", "20000", "West Indies", "Australia", "Jawahar lal nehru", "Rajendra Prasad", "Asha Bhosle", "Brian Lara", "Ban ki moon","366", "To convert black money", "Bangalore", "198" ]
options2_list = ["Dhannu", "29", "4", "30000", "India", "India", "Rajiv gandhi", "Sarvapalli Radhakrishnan", "Lata Mangeshkar", "Sachin Tendulkar", "Elvis perry", "364", "To clean India", "Chennai", "199"]
options3_list = ["Deepanshu", "26", "3", "50000", "Australia", "Ireland", "Subhash chandra bose", "Abdul Kalam", "Sarojini Naidu", "Ricky Ponting", "Neil Armstorng", "370", "To clean Ganga", "Ahmedabad", "200"]
options4_list = ["Mark Zuckerberg", "18", "2", "10000", "Pakistan", "Argentina", "Mahatma Gandhi", "Mohammad Ali Jinnah", "Abida Parveen", "Don Bradman", "Donald Trump", "365", "To clean world", "Delhi", "300"]

var = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
answer_key = (4,3,1,2,1,2,4,1,3,2,3,4,2,1,3)
prize = (1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000)
flagRightAnswer=True
for index in range(15):
    if flagRightAnswer:
        print ("-------------------------------------")
        print ("aapka",var[index],"question yeh hai")
        print ("Q - ",question_list[index])
        print ("1 - ",options1_list[index])
        print ("2 - ",options2_list[index])
        print ("3 - ",options3_list[index])
        print ("4 - ",options4_list[index])
        ans = input("enter your answers\n")
        if ans == "quit":
            flagRightAnswer=False
            print ("aapne game quit kar di hai")
            print ("aap yaha se",prize[index -1],"jeet kar jaa rahe hai")
        elif int(ans) == answer_key[index]:
            print ("aapka jawab sahi hai")
            print ("aap",prize[index],"jeet chuke hain")
        else:
            print ("aapka jawab galat hai")
            flagRightAnswer=False
            print ("aap",prize[index-1],"jeet kar yaha se jaa rahe hai")
        if ans == answer_key[index]:
            print ("aap",prize[index],"jeet chuke hai")