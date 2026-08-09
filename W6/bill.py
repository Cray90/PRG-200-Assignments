import random

random.seed(42)

friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]

total_bill = 3750


def split_bill(friends, total):

    share = total / len(friends)
    return share


def pick_lucky(friends):

    return random.choice(friends)


def final_summary(friends, total):

    share = split_bill(friends, total)

    lucky = pick_lucky(friends)

    print("Bill Summary")

    for person in friends:

        if person == lucky:
            lucky_total = share + 50
            print(person, "= NPR", lucky_total)
        else:
            print(person, "= NPR", share)

    print("Lucky Person:", lucky)


final_summary(friends, total_bill)