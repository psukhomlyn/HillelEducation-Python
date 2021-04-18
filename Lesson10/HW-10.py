class Hero:
    def __init__(self, name):
        self.name = name


class Oldman(Hero):
    def ask_to_bake_kolobok(self, Oldwoman):
        print('Oldman asked Oldwoman to bake Kolobok')
        Oldwoman.find_flour()
        Oldwoman.bake_kolobok()


class Oldwoman(Hero):

    def find_flour(self):
        print('Oldwoman found some flour')

    def bake_kolobok(self):
        print('Oldwoman baked Kolobok')


class Kolobok(Hero):
    def run(self):
        print('Kolobok run')

    def sign_song(self):
        print('Kolobok sign song')

    def die(self):
        print('Kolobok died')


class Rabbit(Hero):

    def meet_kolobok(self, kolobok):
        print('Rabbit met Kolobok')
        kolobok.sign_song()
        kolobok.run()


class Wolf(Hero):

    def meet_kolobok(self, kolobok):
        print('Wolf met Kolobok')
        kolobok.sign_song()
        kolobok.run()


class Bear(Hero):

    def meet_kolobok(self, kolobok):
        print('Bear met Kolobok')
        kolobok.sign_song()
        kolobok.run()

class Fox(Hero):

    def meet_kolobok(self, kolobok):
        print('Fox met Kolobok')
        kolobok.sign_song()

    def eat_kolobok(self, kolobok):
        print('Fox eat Kolobok')
        kolobok.die()


def tale():


    oldman = Oldman('oldman')
    oldwoman = Oldwoman('oldwoman')
    kolobok = Kolobok('kolobok')
    rabbit = Rabbit('rabbit')
    wolf = Wolf('wolf')
    bear = Bear('bear')
    fox = Fox('fox')

    oldman.ask_to_bake_kolobok(oldwoman)
    # oldwoman.find_flour()
    # oldwoman.bake_kolobok()
    kolobok.run()
    rabbit.meet_kolobok(kolobok)
    wolf.meet_kolobok(kolobok)
    bear.meet_kolobok(kolobok)
    fox.meet_kolobok(kolobok)
    fox.eat_kolobok(kolobok)


tale()