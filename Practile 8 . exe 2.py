feedback = input("Enter feedback: ")

target_words = ["badword", "spam", "offensive"]

words = feedback.split()

for i in range(len(words)):
    clean_word = words[i].strip(".,!?;:")
    
    for target in target_words:
        if clean_word.lower() == target.lower():
            words[i] = "****"

filtered_feedback = " ".join(words)

print("Filtered feedback:", filtered_feedback)