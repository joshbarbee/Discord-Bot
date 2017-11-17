def main():
    print("My Life: Josh Barbee \nVersion 0.5.1")
    while True:
        print("[1]Family and Early History")
        print("[2]Relationships")
        print("[3]Experiences")
        print("[4]God")
        initchoice = input("What do you want to access?")
        def family (initchoice):
            print("You picked: " +initchoice)
            k = 0
            while k <= 5:
                familychoice = input ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhat family member do you want to look at?\n[0]Family roots\n[1]Su(Mom)\n[2]Scott(Dad)\n[3]Emma(Sister)\n[4]Keegan(Brother)\n[5]Myself\n")
                if familychoice == "1":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n::::Su::::")
                    print("-Attended OU and got her masters from Xavier")
                    print("-Currently is an English teacher at McAuley")
                    print("-Born and raised in Cincinnati")
                    print("-44 years old")
                    choice = input("")
                    if choice == True:
                        break
                elif familychoice == "0":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-My mother's side is from mostly Italy and my father's side is German and Welsh")
                    print("-One of my grandmothers live in Cincinnati, the other lives in Cleveland")
                    choice = input("")
                    if choice == True:
                        break         
                elif familychoice == "2":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n::::Scott::::")
                    print("-Got his bachelor's degree from UC in accounting")
                    print("-Currently a wealth advisor and CPA at Truepoint Wealth Counsel")
                    print("-Born in Olmstead Falls, outside of Cleveland, and moved to Cincinnati for college")
                    print("-45 years old")
                    choice = input("")
                    if choice == True:
                        break

                elif familychoice == "3":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n::::Emma::::")
                    print("-Attending Parsons College in New York for graphic design")
                    print("-She was born in Cincinnati, and lived here until moving to New York for college")
                    print("-Currently 18")
                    print("-She has a boyfriend")
                    choice2 = input("")
                    if choice2 == True:
                        break           
                elif familychoice == "4":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n::::The Devil Child(Keegan)::::")
                    print("-Currently a 6th grader at St. James and he is majoring in annoyance")
                    print("-May have been born on Mars, but probably Cincinnati")
                    print("-He is 11, acts 9, and looks 5")
                    print("-He's single and ready to mingle")
                    choice3 = input("") 
                    if choice3 == True:
                        break                  
                elif familychoice == "5":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-I am, just like I think all of you, a sophomore")
                    print("-In West Cincinnati born and raised")
                    print("-15 years old")
                    print("-Born with only one functioning eye")
                    print("-I had my eye removed the summer of 09")
                    print("-I also have had bouts of asthma in the past but have seem to overcome it")
                    print("-I am a JV/Varsity (it changes based on performance) Bowling Bomber")
                    choice4 = input("")  
                    if choice4 == True:
                        break
                else:
                    break  
                k += 1
        def Relationships(initchoice):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThroughout my life I have formed many personal relationships that have greatly enriched my life:")
            print("1. My grandmother")
            print("2. Mrs. Boomer")
            print("3. Charlie Humbert")
            print("4. Keirnan Cagle")
            print("5. Flossine")
        def Experiences(initchoice):
            print("I have undergone many drastic and life-changing experiences")
            k = 0
            while k < 2:
                choice = input("Access [1]good or [2]bad experiences?")
                if choice == "1":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHere are some of my life changing good experiences:")
                    print("1. Winning my school's geography bee")
                    print("2. Going on vacation with my grandfather and rest of family to Hawaii")
                    print("3. Making it into the Xavier House program")
                    print("4. Traveling out west to places like Yellowstone, the Rockies, the Grand Canyon, and other places")
                    print("5. Learning how to program in Python & other languages")
                    print("6. Adopting my puppy in May of last year")
                    cquadaw101 = input("")
                    if cquadaw101 == True:
                        break
                elif choice == "2":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHere are some of my bad experiences: ")
                    print("1. Having to get my eye removed")
                    print("2. Not branching out as far freshman year")
                    print("3. Having my grandpa die a couple months after taking our family to Hawaii")
                    cquadaw101 = input("")
                    if cquadaw101 == True:
                        break
                k = k+1
        def god(initchoice):
            k = 0
            while k < 2:
                choice = input("[1] Relationship with Church and society \n[2] Relationship with God")
                if choice == "1":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nI have been involved with the church from my youth, but lately have stopped ")
                    print("In 4th grade I was in choir with one of my friends")
                    print("In 6th grade I signed up to be an Altar server and did that until the end of 8th grade")
                    #print("I have since not been so involved within the church but still do community service and interact with society in the way the church teaches")+
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print("I have volunteered at Matthew 25 to help package supply kits being sent out to disaster survivors")
                    print("For the past 2 years I have tutored at the Winton Place Youth Center on Wednesdays")
                    cquadaw101 = input("")
                    if cquadaw101 == True:
                        break
                elif choice == "2":
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nMy relationship with God has been decreasing over time I feel after leaving St. James")
                    print("The only time that I really attend mass or pray to God is during school")
                    print("I do not believe that I have seen God in my life, or maybe I have but haven't realized it")
                    print("The whole idea of God still remains mysterious to me, contributing towards my distancing from Catholicism")
                    cquadaw101 = input("")
                    if cquadaw101 == True:
                        break
                k = k+1
        if initchoice == "1":
            family(initchoice)
        elif initchoice == "2":
            Relationships(initchoice)  
        elif initchoice == "3":
            Experiences(initchoice)
        elif initchoice == "4":
            god(initchoice)
main()
