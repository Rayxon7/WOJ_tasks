
word = input()
shift = int(input())

result = ""

for letter in word:
    position = ord(letter) - ord("a")
    new_position = (position + shift) % 26
    result += chr(new_position + ord("a"))

print(result)


