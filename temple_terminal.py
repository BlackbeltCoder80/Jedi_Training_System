# My Jedi Terminal I careated soemthing like this before. 
# Just went back and grabbed all my notes and lines and brought them here and changed what was needed.
# Frontend seems to be the direction Ill go first but I enjoy the work backend.
from jedi_council import add_jedi, update_jedi_rank
from training_sessions import add_training_session, remove_training_session
from tabulate import tabulate

def main():
    while True:
        print("\n Welcome to the Jedi Temple Terminal")
        print(tabulate([
            ["[1]", "Enroll a New Jedi"],
            ["[2]", "Promote a Jedi to Higher Rank"],
            ["[3]", "Log a Jedi Training Session"],
            ["[4]", "Erase a Jedi Training Session"],
            ["[5]", "Exit the Jedi Temple"]
        ], headers=["Options", "Actions"], tablefmt="fancy_grid"))
        
        choice = input("Select an option: ")

        if choice == "1":
            print("\n[Enroll a New Jedi]")
            name = input("Enter Jedi name: ")
            age = int(input("Enter Jedi age: "))
            jedi_rank = input("Enter Jedi rank (Youngling, Padawan, Knight, Master, Grand Master): ")
            add_jedi(name, age, jedi_rank)

        elif choice == "2":
            print("\n[Promote a Jedi]")
            jedi_id = int(input("Enter Jedi ID: "))
            new_rank = input("Enter new Jedi rank: ")
            update_jedi_rank(jedi_id, new_rank) #double check name

        elif choice == "3":
            print("\n[Log a Jedi Training Session]")
            jedi_id = int(input("Enter Jedi ID: "))
            session_time = input("Enter session time (Morning, Afternoon, Evening): ")
            activity = input("Enter training activity: ")
            duration = int(input("Enter duration in minutes: "))
            force_ability = input("Enter Force ability trained: ")
            add_training_session(jedi_id, session_time, activity, duration, force_ability)   

        elif choice == "4":
            print("\n[Erase a Jedi Training Session]")
            session_id = int(input("Enter training session ID: "))
            remove_training_session(session_id)
        
        elif choice == "5":
            print("\nThe Jedi Temple Terminal is closing. May the Force be with you.")
            break  # double check break 

        else:  
            print("Invalid selection. Please try again.") 

if __name__ == "__main__":
    main()