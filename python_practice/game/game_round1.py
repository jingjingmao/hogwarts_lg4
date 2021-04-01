"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""


def fight():
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    print(my_final_hp)
    print(enemy_final_hp)

    if my_final_hp > enemy_final_hp:
        print("I won!")
    else:
        print("I lost")


fight()
