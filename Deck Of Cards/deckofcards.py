import random


class Deck:
    def __init__(self):
        colors = ["red", "blue", "green", "yellow"]
        self.cards = [[num + 1, colors[color]] for color in range(4) for num in range(10)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(len(self.cards) - 1)

    def __iter__(self):
        return self

    def __next__(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            raise StopIteration


if __name__ == "__main__":
    deck = Deck()
    # shuffle the cards and print after shuffling
    deck.shuffle()
    print(deck.cards)
    # deal a card and print after dealing (pop a card)
    print(deck.deal())
    print(deck.cards)
    # print the cards that remain after dealing
    for card in deck:
        print(card)
    # print an empty list because the iteration make pop to cards
    print(deck.cards)
