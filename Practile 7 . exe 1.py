text = input("Enter the email/text block: ")

symbols = ["@", ".", "!"]

for symbol in symbols:
    count = 0

    for character in text:
        if character == symbol:
            count += 1

    print(f"'{symbol}' occurs {count} time(s)")

