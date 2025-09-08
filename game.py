import random
from goblin import Goblin
from hero import Hero
from brodytheboss import Brody

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Create Brody the Boss (just for fun)
    brody = Brody("Brody the Boss", "red")

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins or brody.is_alive()):
        print("\nNew Round!")
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    if brody.is_alive():
        print("Boss Time!!!")
        brody = Brody("Brody the Boss", "red")
        while hero.is_alive() and brody.is_alive():
            damage = hero.strike()
            brody.take_damage(damage)
            print(f"Hero attacks Brody the Boss for {damage} damage! Health is now {brody.health}.")
            damage = brody.attack()
            hero.receive_damage
        if brody.is_alive():
            print (f"The hero has defeated Brody the Boss! ༼ ᕤ◕◡◕ ༽ᕤ")
        else:
            print(f"The hero has been defeated by Brody the Boss. Game Over. (｡•́︿•̀｡)")


    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()
