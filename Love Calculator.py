# Functions with input

def calculate_love_score(name1, name2):
    word1 = "TRUE".lower()
    word2 = "LOVE".lower()

    result1 = 0
    result2 = 0

    for letter in name1 + name2.lower():
        if letter in word1:
            result1 += 1

    for char in name1 + name2.lower():
        if char in word2:
            result2 += 1

    print(f"Love Score = {result1}{result2}")


calculate_love_score("Kanye West", "Kim Kardashian")



