class CardGame(object):

    def __init__(self, cards, people):
        self.cards = cards
        self.people = people

    def shuffle_deck(self):
        self.cards.shuffle()

    def play(self):
        pass


class Poker(CardGame):

    def __init__(self, cards, people, ):
        CardGame.__init__(cards, people)


    def play(self):
        self.shuffle_deck()
        pass


for i, el in enumerate([3, 4, 5]):
    print i
    print el