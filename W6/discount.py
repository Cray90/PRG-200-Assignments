TAX_RATE = 0.13


def apply_discount(price, percent):

    discount = price * percent / 100

    return price - discount


def apply_tax(price):

    return price + (price * TAX_RATE)


def final_price(price, discount_pct):

    discounted_price = apply_discount(price, discount_pct)

    return apply_tax(discounted_price)