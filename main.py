from braille_map import key_to_dot, dots_to_char
import json, os

def decode_braille_sequence(sequence):
    decoded = []
    for combo in sequence:
        dots = [key_to_dot.get(c.upper(), '') for c in combo if c.upper() in key_to_dot]
        dots.sort()
        key = ",".join(dots)
        decoded.append(dots_to_char.get(key, '?'))
    return "".join(decoded)

def edit_distance(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0: dp[i][j] = j
            elif j == 0: dp[i][j] = i
            elif s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]
            else: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[n][m]

def suggest_words(decoded, dictionary, learning_data):
    suggestions = sorted(dictionary, key=lambda word: (
        edit_distance(decoded, word) - learning_data.get(word, 0)))
    return suggestions[:5]

def load_dictionary(language):
    file_map = {
        'en': 'dictionary_en.txt',
        'hi': 'dictionary_hi.txt'
    }
    return open(file_map.get(language, 'dictionary_en.txt')).read().splitlines()

def update_learning_log(chosen_word):
    log_path = 'learning_log.json'
    if os.path.exists(log_path):
        with open(log_path) as f:
            data = json.load(f)
    else:
        data = {}
    data[chosen_word] = data.get(chosen_word, 0) + 1
    with open(log_path, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    print("Select language: [en] English | [hi] Hindi")
    lang = input("Language code: ").strip().lower()
    dictionary = load_dictionary(lang)

    learning_data = {}
    if os.path.exists("learning_log.json"):
        with open("learning_log.json") as f:
            learning_data = json.load(f)

    print("Enter Braille input using QWERTY key mapping (e.g., DQ DK DQ):")
    qwerty_groups = input("Braille Input: ").strip().split()
    decoded = decode_braille_sequence(qwerty_groups)
    print(f"Decoded Word: {decoded}")

    suggestions = suggest_words(decoded, dictionary, learning_data)
    print("Suggestions:")
    for i, word in enumerate(suggestions):
        print(f"{i+1}. {word}")

    choice = input("Select the correct word (1-5), or press Enter to skip: ")
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(suggestions):
            update_learning_log(suggestions[idx])
            print(f"Learned correction: {suggestions[idx]}")
