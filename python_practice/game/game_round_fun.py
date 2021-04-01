import random


def fight(enemy_hp, enemy_power):
    my_hp = 1000
    my_power = 200

    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        print(my_hp)

        if my_hp <= 0:
            print("I lost!")
            break
        elif enemy_hp <= 0:
            print("I won!")
            break


if __name__ == "__main__":
    # 利用列表推导式生成hp
    hp = [x for x in range(990, 1010)]
    enemy_hp = random.choice(hp)

    enemy_power = random.randrange(190, 200)

    fight(enemy_hp, enemy_power)
