paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
count = 0

for word in words:
    if word == "python":
        count += 1

print(f'The word "python" appears {count} time(s).')