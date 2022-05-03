"""
This file will contain tables of players, clubs and leagues.
Database used will be MySQL and python DB liabrary will be sqlobject
"""

import sqlobject

class Tournaments(sqlobject.SQLObject):
    #siteid          = sqlobject.IntCol(notNone=True)
    tournament_name = sqlobject.UnicodeCol(length = 255)
    tournament_type = sqlobject.UnicodeCol(length = 255) #League/european leageu/cup
    country         = sqlobject.UnicodeCol(length = 255) 
    
    class sqlmeta:
        table = 'tournaments'
        createSQL = "ALTER TABLE %s ADD CONSTRAINT type_country UNIQUE(tournament_type, country)" % (table)


class Teams(sqlobject.SQLObject):
    team_name       = sqlobject.UnicodeCol(length = 255)
    country         = sqlobject.UnicodeCol(length = 255)
    domestic_league = sqlobject.ForeignKey('Tournaments') 
    european_league = sqlobject.ForeignKey('Tournaments')
    domestic_cup    = sqlobject.ForeignKey('Tournaments')
    season          = sqlobject.UnicodeCol(length = 255)
    
    class sqlmeta:
        table = 'teams'
        createSQL = "ALTER TABLE %s ADD CONSTRAINT name_country UNIQUE(team_name, country)" % (table)

class Players(sqlobject.SQLObject):
    player_name = sqlobject.UnicodeCol(length = 255)
    country     = sqlobject.UnicodeCol(length = 255)
    club        = sqlobject.ForeignKey('Teams') 
    season      = sqlobject.UnicodeCol(length = 255)
    
    class sqlmeta:
        table = 'players'
        createSQL = "ALTER TABLE %s ADD CONSTRAINT name_country UNIQUE(player_name, country)" % (table)






