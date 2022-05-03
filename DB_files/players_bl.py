import details_tables
import DL_utils

class Players():
    def __init__(self):
        self.dlobj = baseDLobject('players')

    def add_player_to_db(self, **kwargs):
        player_details =  {
                            'player_name': kwargs['player_name'],
                            'country': kwargs['country'],
                            'club': kwargs['club'],
                            'season': kwargs['season']
                            }
        row_id = self.dlobj._create(**player_details)

        return row_id

    def list_players(self):
        """
        returns all list of all players in db
        """
        # Passing empty to listby should fetch all players
        players = self.dlobj._listby()
        if not players:
            return []

        return players

    def get_player_details_by_name(self, name):
        """
        Get all rows with player_name = input.. this will filter rows by player name
        """
        player = self.dlobj._listby(player_name=name)
        if not player:
            return None

        # TODO: How to avoid duplicates?
        return player[0]

    def get_players_by_club(self, club):
        players = self.dlobj._listby(club=club)
        if not players:
            return None

        return players

# TODO: Finish other required functions for the BL


class Player_stats():
    def __init__(self):
        self.dlobj = baseDLobject('player_stats')
        self.playerdl = baseDLobject('players')

    def add_player_stasts_to_db(self, **kwargs):
        #TODO : Get Player id and team id.. Need to verify if below logic works

        # Get player id 
        player_id = self.playerdl.get_player_details_by_name(kwargs['name'])
        stats = { 
                    'player': player_id
                    'goals': kwargs['goals'],
                    'assists': kwargs['assists'],
                    'season': kwargs['season'],
                }

        row_id = self.dlobj._create(**player_details)

        return row_id

     def get_player_stats_by_name(self, name):
        player = self.dlobj._listby(player=name)
        if not player:
            return None

        return player

    def update_goals_scored(self, name, season, goals):
        # Fetch player stats, filter by season and then update goals
