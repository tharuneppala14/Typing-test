import random
import time

sentences = [
    "Python is easy to learn",
    "Practice makes programming better",
    "I am learning Python programming",
    "Coding is a useful skill",
    "Python is a popular language"
]

sentence = random.choice(sentences)

print("===== Typing Test =====")
print("\nType the following sentence:")
print(sentence)

input("\nPress Enter when you are ready...")

start_time = time.time()

user_text = input("Type here: ")

end_time = time.time()

time_taken = end_time - start_time

correct_words = 0

original_words = sentence.split()
typed_words = user_text.split()

for i in range(min(len(original_words), len(typed_words))):
    if original_words[i].lower() == typed_words[i].lower():
        correct_words += 1

total_words = len(typed_words)

if time_taken > 0:
    speed = (total_words / time_taken) * 60
else:
    speed = 0

print("\n===== Result =====")
print("Time Taken:", round(time_taken, 2), "seconds")
print("Total Words:", total_words)
print("Correct Words:", correct_words)
print("Typing Speed:", round(speed, 2), "words/minute")

if user_text.lower() == sentence.lower():
    print("Result: Excellent! 🎉")
else:
    print("Result: Keep Practicing!")
