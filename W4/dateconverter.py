bs_months = [
    "Baisakh", "Jestha", "Ashadh", "Shrawan",
    "Bhadra", "Ashwin", "Kartik", "Mangsir",
    "Poush", "Magh", "Falgun", "Chaitra"
]

customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"}
]


def convert_date(date_str, from_cal, to_cal):

    if from_cal == to_cal:
        return date_str

    parts = date_str.split("-")

    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])

    if from_cal == "AD" and to_cal == "BS":
        year = year + 56

    elif from_cal == "BS" and to_cal == "AD":
        year = year - 56

    return str(year) + "-" + parts[1] + "-" + parts[2]


for customer in customers:

    converted = convert_date(customer["date"], customer["cal"], customer["need"])

    if customer["style"] == "iso":
        output = converted

    else:
        parts = converted.split("-")
        year = parts[0]
        month = int(parts[1])
        day = int(parts[2])

        if customer["need"] == "BS":
            month_name = bs_months[month - 1]
            output = str(day) + "th " + month_name + ", " + year + " BS"
        else:
            output = converted + " AD"

    print(customer["name"], "| Original:", customer["date"], customer["cal"], "| Converted:", output)