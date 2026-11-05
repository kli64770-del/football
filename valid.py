from menu1 import TEAMS,MACHES

def check_if_number():
    is_num=False

    while not is_num:
        num=input("please enter number: ")
        if  num.isdigit():
            is_num=True

      
    return num


def check_if_str():
    is_str=False

    while not is_str:
        name=input("please enter name: ")
        if name.isalpha():
            is_str=True
    return name




def check_teams_id(home_id,away_id):
    if int(home_id)==int(away_id):
        
        return "the teams id are the same!!!"
        
        
    home=False
    away=False
    for team in TEAMS:
        if team["id"]==home_id:
            home=True
        if team["id"]==away_id:
            away=True

    if home and away:
        print("we found the teams!!!")
        print(home_id,away_id)

        return home_id,away_id

def check_if_played(home_id,away_id):
    if_played=False
    for match in MACHES:
        if home_id==match["home_team_id"] and away_id == match["away_team_id"]:
            if_played=True 
        if not if_played:
            return "the teams did't played!!!!"

def check_if_exist():
    num=input(" bgbfz njxh: ")
    if_exist=False
    for team in TEAMS:
        if int(num)==team["id"]:
            if_exist=True
            return f"exist"

    if not if_exist:
        return f"not exist..."
       
        
    







