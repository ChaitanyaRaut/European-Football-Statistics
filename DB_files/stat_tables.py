import sqlobject
import details_tables as *

class Player_stats(sqlobject.SQLObject):
    tournament = sqlobject.ForeignKey('Tournaments') 
    player = sqlobject.ForeignKey('Players')
    goals = sqlobject.IntCol()
    assists = sqlobject.IntCol()
    season  = sqlobject.UnicodeCol(length = 255)


class Team_stats(sqlobject.SQLObject):
    tournament = sqlobject.ForeignKey('Tournaments') 
    club = sqlobject.ForeignKey('Teams')
    matches = sqlobject.IntCol()
    matches_won = sqlobject.IntCol()
    matches_lost = sqlobject.IntCol()
    matches_drawn = sqlobject.IntCol()
    goals_for = sqlobject.IntCol()
    goals_against = sqlobject.IntCol()
    points = sqlobject.IntCol()
    season = sqlobject.UnicodeCol(length = 255)







