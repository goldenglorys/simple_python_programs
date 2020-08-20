class Enemy:
    life = 3

    def __init__(self, x):
        self.energy = x

    def attack(self):
        print("Enemy under attack")
        self.life -= 1

    def checkenemyelife(self):
        if self.life <= 0:
            print("Enemy is down!")
        else:
            print(str(self.life) + " life left")

    def get_energy(self):
        print(self.energy)

    def print_enemy_name(self):
        print('Mortal Enemy')


class EnemyChild(Enemy):
    def print_child_enemy_identity(self):
        print("Mortal Enemy Child")


thanos = Enemy(5)

thanoschild = EnemyChild(2)

thanoschild.print_enemy_name()
thanoschild.print_child_enemy_identity()