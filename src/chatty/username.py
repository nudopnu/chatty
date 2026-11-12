from random import choice
from itertools import product


ATTRS = [
    "juicy",
    "spicy",
    "golden",
    "sweet",
    "sour",
    "bitter",
    "fresh",
    "frozen",
    "ripe",
    "rotten",
    "crunchy",
    "soft",
    "smooth",
    "fuzzy",
    "shiny",
    "sticky",
    "tasty",
    "exotic",
    "tropical",
    "wild",
    "organic",
    "mini",
    "giant",
    "bloody",
    "radioactive",
    "magical",
    "poisonous",
    "glowing",
    "mysterious",
    "ancient"
]

OBJECTS = [
    "orange",
    "lemon",
    "apple",
    "banana",
    "pear",
    "pineapple",
    "mango",
    "watermelon",
    "strawberry",
    "blueberry",
    "raspberry",
    "grape",
    "cherry",
    "peach",
    "plum",
    "kiwi",
    "coconut",
    "papaya",
    "avocado",
    "pomegranate",
    "dragonfruit",
    "grapefruit",
    "lime",
    "fig",
    "melon",
    "apricot",
    "passionfruit",
    "guava",
    "lychee",
    "persimmon"
]


def generate():
    return " ".join(choice(list(product(ATTRS, OBJECTS)))).title()

if __name__ == "__main__":
    print(generate())
    print(generate())
    print(generate())