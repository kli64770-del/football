from menu1 import menu2,TEAMS,MACHES
from all_function import add_team,show_teams_all,add_match
from valid import check_if_str,check_if_number,check_if_played

print("main file")

def main():
    while True:
        menu2()
        choise_option=int(input("please enter a number (0-7): "))


        if choise_option==0:
            print("goodbye!!!")
            break

        if choise_option==1:
            print(add_team(check_if_number(),check_if_str()))

        if choise_option==2:
            show_teams_all()

        if choise_option==3:
            check_if_played(check_if_number(),check_if_number())
            add_match(check_if_number(),check_if_number())


            

        



main()