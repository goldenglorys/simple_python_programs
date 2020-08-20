class Enemy:
    life = 3

    def attack(self):
        print("Enemy under attack")
        self.life -= 1

    def checkenemyelife(self):
        if self.life <= 0:
            print("Enemy is down!")
        else:
            print(str(self.life) + " life left")


thanos = Enemy()

thanos.attack()
thanos.checkenemyelife()
thanos.attack()
thanos.checkenemyelife()
thanos.attack()
thanos.checkenemyelife()
thanos.attack()
thanos.checkenemyelife()
