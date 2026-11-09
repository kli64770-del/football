from menu1 import TEAMS,MACHES,menu2
from valid import check_if_number,check_teams_id,check_if_str,check_if_played

def add_team(id_team,name):
    new_team={}
    is_exist=False

    for team in TEAMS:
        if  id_team ==str(team["id"])  or name == team["name"]:
            is_exist=True

    if not is_exist:
        new_team["id"]=id_team
        new_team["name"]=name
        new_team["played"]=0
        new_team["draws"]=0
        new_team["losses"]=0
        new_team["goals_for"]=0
        new_team["goals_against"]=0
        new_team["points"]=0
        TEAMS.append(team)
        return f"the team {name} created!!!!"
    return "try agian"


def show_teams_all():
    if not TEAMS:
        
        no_teams="There are not teams!"

        return no_teams

    for team in TEAMS:  
        print( f"id: {team["id"]} name: {team["name"]}\nplayed: {team["played"]} points: {team["points"]}\n")

def add_match(id_home,id_away):

    goales_home=check_if_number()
    goales_away=check_if_number()
    new_match={}
    new_match["home_team_id"]=id_home
    new_match["away_team_id"]=id_away
    new_match["home_goals"]=goales_home
    new_match["away_goals"]=goales_away
    print("The teams are added to the MACHES list!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    MACHES.append(new_match)

    
def restart_team(team_id):
    for team in TEAMS:
        if team["id"]==team_id:
            team["name"]=0
            team["played "]=0
            team["wins"]=0
            team["draws"]=0
            team["losses"]=0
            team["goals_for"]=0
            team["goals_against"]=0
            team["points"]=0
            print("The team ise deleted!!")
            



