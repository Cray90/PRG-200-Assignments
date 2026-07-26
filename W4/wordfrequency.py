text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""


def word_frequency(text):

    text = text.lower()

    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = text.replace("?", "")

    words = text.split()

    count = {}

    for word in words:

        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1

    items = list(count.items())

    items.sort(key=lambda x: x[1], reverse=True)

    print("Top 3 words:")

    for i in range(3):
        print(items[i][0], "-", items[i][1], "times")


word_frequency(text)