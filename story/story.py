with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_index = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_index = i
    elif char == target_end and start_index != -1:
        word = story[start_index:i+1]
        words.add(word)
        start_index = -1

answers = {}

for word in words:
    answer = input("Enter a Word for" + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
