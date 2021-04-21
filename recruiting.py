jobs= {
    "C# Developer":[2, 100000],
    "Angular":[1, 135000],
    "Elixir": [1, 120000],
    "React": [1,120000],
    "Node": [1, 115000],
    "Python": [1,95000]
    }

while True:

    choice = input("What Software Developer position would you like to learn more about?: ").strip().title()

    if choice in jobs:
        salary = int(input("What salary are you seeking?: ").strip())
        #check comp requirements

        if salary <= jobs[choice][1]:

            num_openings= jobs[choice][0]

            if num_openings >0:
                print("Email me at taylor.fulton@techcxo.com")
                jobs[choice][0] = jobs[choice][0] - 1
            else:
                print("Sorry, there are no more openings.")
        else:
           print("Sorry, you are out of the budget for that position, but I'd love to stay in touch!")

    else:
        print("I'm not recruiting for that position at this time...")
            

        
