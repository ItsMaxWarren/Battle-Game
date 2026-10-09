import random

print("========================\n      BATTLE GAME\n========================")


class enemy:

    def __init__(self, name, minHP, maxHP, minDamage, maxDamage):
        self.name = name
        self.hp = random.randint(minHP, maxHP)
        self.maxHealth = self.hp
        self.minDamage = minDamage
        self.maxDamage = maxDamage

    def attack(self):
        damage = random.randint(self.minDamage, self.maxDamage)
        chance = random.randint(1, 100)
        is_crit = False

        if chance <= 12:
            damage *= 2
            is_crit = True

        return damage, is_crit

    def takeDamage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0


goblin = enemy("Goblin", 80, 100, 13, 17)
orc = enemy("Orc", 120, 160, 18, 23)
skeleton = enemy("Skeleton", 70, 90, 10, 15)
dragon = enemy("Dragon", 150, 175, 25, 35)
enemies = [goblin, orc, skeleton, dragon]


class player:
    def __init__(self, name, health, minDamage, maxDamage):
        self.name = name
        self.health = health
        self.maxHealth = health
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.healAmount = 3
        self.damageBoostAmount = 0
        self.damageBoostAttacks = 0

    def attack(self):
        damage = random.randint(self.minDamage, self.maxDamage)
        chance = random.randint(1, 100)
        is_crit = False

        if chance <= 20:
            damage *= 2
            is_crit = True

        return damage, is_crit

    def takeDamage(self, damage):
        self.health -= damage

        if self.health < 0:
            self.health = 0

    def healing(self):
        Heal = 25

        if self.healAmount != 0:
            self.health += Heal
            self.healAmount -= 1
        else:
            print("No potions available!")

        if self.health > self.maxHealth:
            self.health = self.maxHealth

        return Heal

    def levelUp(self):
        self.minDamage += 5
        self.maxDamage += 5
        self.healAmount += 1

    def bossBoost(self):
        boost = 20

        self.minDamage += boost
        self.maxDamage += boost
        self.damageBoostAttacks = 3
        return boost

    def showStatus(self, enemy):
        print("----------------------------------------")
        print("              BATTLE STATUS")
        print("----------------------------------------")
        print(f"{self.name}: {self.health}/{self.maxHealth} HP")
        print(f"Damage: {self.minDamage}-{self.maxDamage}")
        print(f"Healing Potions: {self.healAmount}")
        print(f"Damage Boost Potions: {self.damageBoostAmount}")
        print(f"Available Boosted Attacks: {self.damageBoostAttacks}")
        print("----------------------------------------")
        print(f"{enemy.name}: {enemy.hp}/{enemy.maxHealth} HP")


playerName = ""

while playerName == "":
    print("Please nter a valid name!")
    playerName = input("Enter your name: ").strip()
    

player1 = player(playerName, 100, 18, 25)


def game():

    choice = None

    for i in range(len(enemies)):
        currentEnemy = enemies[i]

        print("----------------------------------------")
        print(f"A wild {currentEnemy.name} appeared!")
        print(f"{currentEnemy.name} has {currentEnemy.hp} HP.")
        while True:
            try:
                choice = int(input(""
                                   "----------------------------------------"
                                   "\n1- Attack"
                                   "\n2- Use healing potion"
                                   "\n3- Use damage boost potion"
                                   "\n4- Show status"
                                   "\n5- Run"
                                   "\nChoose: "
                                   ))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if choice == 1:

                damage, is_crit = player1.attack()
                currentEnemy.takeDamage(damage)

                if player1.damageBoostAttacks > 0:
                    player1.damageBoostAttacks -= 1

                    if player1.damageBoostAttacks == 0:
                        player1.minDamage -= 20
                        player1.maxDamage -= 20
                        print("Damage boost has expired!")

                print()
                print("----------------------------------------")
                if is_crit:
                    print("💥 CRITICAL HIT! 💥")
                print(f"You attacked {currentEnemy.name} for {damage} damage!")
                print(f"{currentEnemy.name} has {currentEnemy.hp} HP left.")

                if i == len(enemies) - 2 and currentEnemy.hp <= 0:
                    player1.damageBoostAmount += 1
                    player1.healAmount += 2

                    print("----------------------------------------")
                    print("You defeated the Skeleton!")
                    print("You found a RARE DAMAGE BOOST POTION and 2 HEALING POTION!")
                    print(f"Damage boost potions: {player1.damageBoostAmount}")
                    print("----------------------------------------")
                    break

                if currentEnemy.hp <= 0 and currentEnemy.name != "Dragon":
                    print()
                    print("----------------------------------------")
                    print(f"{player1.name} has won!")
                    print(
                        f"Congratulations, you have defeated {currentEnemy.name}")

                    player1.levelUp()
                    print()
                    print(
                        f"Your damage increased to {player1.minDamage}-{player1.maxDamage}!")
                    print(f"You gained a healing potion!")
                    print(f"Potions: {player1.healAmount}")

                    print("----------------------------------------")
                    print("Preparing for the next enemy...")
                    break

                elif i == len(enemies) - 1 and currentEnemy.hp <= 0:
                    print("----------------------------------------")
                    print("The Dragon has been defeated!")
                    print("🏆 CONGRATULATIONS!")
                    print(
                        f"You defeated all enemies!\nYou WON {player1.name}!")
                    print("----------------------------------------")
                    return

                else:

                    damage, is_crit = currentEnemy.attack()
                    player1.takeDamage(damage)

                    print()
                    if is_crit:
                        print("💥 CRITICAL HIT! 💥")
                    print(f"{currentEnemy.name} attacked you for {damage} damage!")
                    print(f"You have {player1.health} HP left.")

                if player1.health <= 0:
                    print("----------------------------------------")
                    print("You Died!")
                    print(f"{currentEnemy.name} has won!")
                    print("----------------------------------------")
                    return

            elif choice == 2:
                if player1.health <= 90 and player1.healAmount != 0:
                    heal = player1.healing()

                    print("----------------------------------------")
                    print(f"You Healed for {heal} HP")
                    print(f"You now have {player1.health} HP")
                    print(f"Potions: {player1.healAmount}")

                else:
                    print("----------------------------------------")
                    print("You cant heal right now!")
                    if player1.healAmount == 0:
                        print("You dont have enough healing potions!")

            elif choice == 3:
                if player1.damageBoostAmount != 0:
                    boost = player1.bossBoost()

                    player1.damageBoostAmount -= 1

                    print("You used a SPECIAL damage boost potion!")
                    print(f"Damage increased by +{boost}")
                else:
                    print("----------------------------------------")
                    print("You dont have enough damage boost potions!")

            elif choice == 4:
                player1.showStatus(currentEnemy)

            elif choice == 5:
                print()
                print("You ran like a coward, Battle ends NOW\nLoser")
                return
            else:
                print("Invalid choice")


game()
