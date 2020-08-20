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


thanos = Enemy(5)

thanos.get_energy()
thanos.attack()
thanos.checkenemyelife()
thanos.attack()
thanos.checkenemyelife()
thanos.attack()
thanos.checkenemyelife()
thanos.attack()
thanos.checkenemyelife()
