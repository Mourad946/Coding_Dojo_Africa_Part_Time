class Player:
    def __init__(self, player_info):
        self.name = player_info.get('name')
        self.age = player_info.get('age')
        self.position = player_info.get('position')
        self.team = player_info.get('team')
    
    @classmethod
    def get_team(cls, team_list):
        return [cls(player_info) for player_info in team_list]

# Given dictionaries
kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# Create Player instances
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# List of players
players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Forward",
        "team": "Philadelphia 76ers"
    },
    {
        "name": "",
        "age": 16,
        "position": "P",
        "team": "en"
    }
]

# Populate new_team variable with Player objects
new_team = Player.get_team(players)

# Display each player's info
for player in new_team:
    print(player.name, player.age, player.position, player.team)



