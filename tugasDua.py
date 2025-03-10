import random
class Robot:
    def __init__(self, name, hp, att, deff, agi):
        self.name = name
        self.hp = hp
        self.att = att
        self.deff = deff
        self.agi = agi

class Game:
    def __init__(self, fighter_one, fighter_two):
        self.fighter_one = fighter_one
        self.fighter_two = fighter_two

    def hp_below_zero(self, hp):
        if hp < 0:
            return 0
        return hp

    def action(self, fighter1_action, fighter2_action):
        fighter1_dodge = random.randint(1, 100)
        fighter2_dodge = random.randint(1, 100)

        if fighter1_action == 1 and fighter2_action == 1:
            if 0 < fighter1_dodge <= self.fighter_one.agi and fighter2_dodge > self.fighter_two.agi:
                self.fighter_two.hp -= self.fighter_one.att
                self.fighter_two.hp = self.hp_below_zero(self.fighter_two.hp)

                print(f"{self.fighter_one.name} managed to dodge")
                print(f"{self.fighter_two.name}'s hp is {self.fighter_two.hp} now")
            elif 0 < fighter2_dodge <= self.fighter_two.agi and fighter1_dodge > self.fighter_one.agi:
                self.fighter_one.hp -= self.fighter_two.att
                self.fighter_one.hp = self.hp_below_zero(self.fighter_one.hp)

                print(f"{self.fighter_two.name} managed to dodge")
                print(f"{self.fighter_one.name}'s hp is {self.fighter_one.hp} now")
            else:
                self.fighter_two.hp -= self.fighter_one.att
                self.fighter_one.hp -= self.fighter_two.att

                self.fighter_two.hp = self.hp_below_zero(self.fighter_two.hp)
                self.fighter_one.hp = self.hp_below_zero(self.fighter_one.hp)

                print(f"{self.fighter_two.name}'s hp is {self.fighter_two.hp} now")
                print(f"{self.fighter_one.name}'s hp is {self.fighter_one.hp} now")
            
        elif fighter1_action == 1 and fighter2_action == 2 or fighter1_action == 2 and fighter2_action == 1:
            if fighter1_action == 1:
                attacker = self.fighter_one
                defender = self.fighter_two
            else:
                attacker = self.fighter_two
                defender = self.fighter_one

            percent_damage = (50 - defender.deff) / 50
            damage = int(attacker.att * percent_damage)

            defender.hp -= damage
            print(f"{attacker.name} attacked {defender.name}")
            print(f"{defender.name}'s hp is reduced by {damage}")
            print(f"{defender.name}'s hp is {defender.hp} now")

        else:
            print("Both robots are on defend position")


sprout = Robot("Sprout", 200, 22, 15, 24)
rico = Robot("Rico", 150, 27, 14, 26)
hank = Robot("Hank", 280, 16, 23, 16)
barley = Robot("Barley", 235, 24, 14, 20)
winner = None
i = 1

print(f"{'=' * 15} Welcome to Robots Duel {'=' * 15}")
print(f"{' ' * 2}Robot{' ' * 4}Hp{' ' * 4}att{' ' * 4}def{' ' * 4}agi")
print(f"{sprout.name}{' ' * 4}{sprout.hp}{' ' * 4}{sprout.att}{' ' * 5}{sprout.deff}{' ' * 5}{sprout.agi}")
print(f"{rico.name}{' ' * 6}{rico.hp}{' ' * 4}{rico.att}{' ' * 5}{rico.deff}{' ' * 5}{rico.agi}")
print(f"{hank.name}{' ' * 6}{hank.hp}{' ' * 4}{hank.att}{' ' * 5}{hank.deff}{' ' * 5}{hank.agi}")
print(f"{barley.name}{' ' * 4}{barley.hp}{' ' * 4}{barley.att}{' ' * 5}{barley.deff}{' ' * 5}{barley.agi}")

choice1 = int(input("\nChoose first fighter : "))
if choice1 == 1:
    fighter1 = sprout
elif choice1 == 2:
    fighter1 = rico
elif choice1 == 3:
    fighter1 = hank
elif choice1 == 4:
    fighter1 = barley

choice2 = int(input("Choose second fighter: "))
if choice2 == 1:
    fighter2 = sprout
elif choice2 == 2:
    fighter2 = rico
elif choice2 == 3:
    fighter2 = hank
elif choice2 == 4:
    fighter2 = barley

s = fighter1.name + " vs " + fighter2.name
print(f"\n{'=' * 10}{s.center(34)}{'=' * 10}")

game = Game(fighter1, fighter2)
while fighter1.hp > 0 and fighter2.hp > 0:
    print("Choose your action")
    print("1. Attack    2. Defense    3. Give Up")

    action1 = int(input(f"{fighter1.name}: "))
    action2 = int(input(f"{fighter2.name}: "))

    if action1 == 3 and action2 == 3:
        print("Both robots have gave up")
    elif action1 == 3 and action2 != 3:
        print(f"{fighter1.name} has surrendered")
        winner = fighter2
        which_is_winner = "Fighter 2"
    elif action1 != 3 and action2 == 3:
        print(f"{fighter2.name} has surrendered")
        winner = fighter1
        which_is_winner = "Fighter 1"
    else:
        game.action(action1, action2)

    if fighter1.hp == 0:
        winner = fighter2
        which_is_winner = "Fighter 2"
    elif fighter2.hp == 0:
        winner = fighter1
        which_is_winner = "Fighter 1"

    if winner != None:
        print(f"The winner is {which_is_winner}, {winner.name}")
    
    if action1 == 3 and action2 == 3 or winner != None:
        break
    print("\n")
