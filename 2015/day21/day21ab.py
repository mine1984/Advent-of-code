# In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.
# Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage.
# Here is what the item shop is selling:
#
# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0
#
# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5
#
# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3
#
# You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item,
#
# What is the least amount of gold you can spend and still win the fight?
# What is the most amount of gold you can spend and still lose the fight?

class Weapon():

    def __init__(self, name, cost, damage):

        self.name = name
        self.cost = cost
        self.damage = damage

class Armor():

    def __init__(self, name, cost, armor):

        self.name = name
        self.cost = cost
        self.armor = armor

class Ring():

    def __init__(self, name, cost, damage, armor):

        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

class Warrior():

    def __init__(self, hp, damage, armor):

        self.hp = hp
        self.damage = damage
        self.armor = armor

class Fight():

    def __init__(self, fight_id, player, boss, cost):

        self.fight_id = fight_id
        self.player = player
        self.boss = boss
        self.cost = cost
        self.win = self.find_winner

    def find_winner(self):

        player_hp = self.player.hp
        player_damage = self.player.damage
        player_armor = self.player.armor
        boss_hp = self.boss.hp
        boss_damage = self.boss.damage
        boss_armor = self.boss.armor
        player_hit = player_damage - boss_armor
        if player_hit < 1:
            player_hit = 1
        boss_hit = boss_damage - player_armor
        if boss_hit < 1:
            boss_hit = 1

        while player_hp > 0 or boss_hp > 0:
            boss_hp += -player_hit
            if boss_hp <= 0:
                return True
            player_hp += -boss_hit
            if player_hp <= 0:
                return False

weapons = {}
weapons[1] = Weapon('Dagger', 8, 4)
weapons[2] = Weapon('Shortsword', 10, 5)
weapons[3] = Weapon('Warhammer', 25, 6)
weapons[4] = Weapon('Longsword', 40, 7)
weapons[5] = Weapon('Greataxe', 74, 8)

armors = {}
armors[0] = Armor('no_armor', 0, 0)
armors[1] = Armor('Leather', 13, 1)
armors[2] = Armor('Chainmail', 31, 2)
armors[3] = Armor('Splintmail', 53, 3)
armors[4] = Armor('Bandedmail', 75, 4)
armors[5] = Armor('Platemail', 102, 5)

rings = {}
rings[-1] = Ring('no_ring', 0, 0, 0)
rings[0] = Ring('no_ring', 0, 0, 0)
rings[1] = Ring('Damage +1', 25, 1, 0)
rings[2] = Ring('Damage +2', 50, 2, 0)
rings[3] = Ring('Damage +3', 100, 3, 0)
rings[4] = Ring('Defense +1', 20, 0, 1)
rings[5] = Ring('Defense +2', 40, 0, 2)
rings[6] = Ring('Defense +3', 80, 0, 3)

players = {}
hp = int(input().split()[2])
damage = int(input().split()[1])
armor = int(input().split()[1])
boss = Warrior(hp,damage,armor)
fights = {}
min_cost = 300
min_fight_id = None
max_cost = 0
max_fight_id = None

for w in range(1,6):
    for a in range(6):
        for r1 in range (-1,7):
            for r2 in range(-1,7):
                if r2 != r1:
                    fight_id = str(w)+str(a)+str(r1)+str(r2)
                    damage = weapons[w].damage+rings[r1].damage+rings[r2].damage
                    armor = armors[a].armor+rings[r1].armor+rings[r2].armor
                    cost = weapons[w].cost+armors[a].cost+rings[r1].cost+rings[r2].cost
                    players[fight_id] = Warrior(100, damage, armor)
                    fights[fight_id] = Fight(fight_id, players[fight_id], boss, cost)
                    if fights[fight_id].win():
                        if min_cost > fights[fight_id].cost:
                            min_cost = fights[fight_id].cost
                            min_fight_id = fight_id
                    if not fights[fight_id].win():
                        if max_cost < fights[fight_id].cost:
                            max_cost = fights[fight_id].cost
                            max_fight_id = fight_id
print(min_cost, min_fight_id)
print(max_cost, max_fight_id)
