# braille-autocorrect-

1. Input Method – QWERTY to Braille
The input is received in the form of Braille characters on QWERTY keys (e.g., D, W, Q, K, O, P for dots 1–6).
Each input character is a combination such as DQ or DK, which corresponds to a dot pattern.
These dot patterns are converted into letters based on a pre-defined Braille-to-character mapping.
2. Word Decoding
The entire input string (such as DQ DK DQ) is translated into an alphabetic string (such as kck)
by assigning each Braille dot pattern to an English letter or contraction.
Standard contractions like 'the', 'and', and 'for' are also handled.
3. Word Suggestion by Edit Distance
After translation, the system seeks a match from a word list (dictionary_en.txt, etc.)
and uses Levenshtein edit distance to determine the nearest valid words.
The 5 most similar words are presented to the user.
4. Learning Mechanism
When a word is chosen by the user from suggestions, it's stored in a learning_log.json.
This file is utilized in subsequent sessions to increase the rank of commonly selected words,
making a customized correction mechanism over time.
5. Multi-language Support
Multiple languages (English and Hindi) are supported by the system by loading individual dictionaries.
The language is selected by users at program initiation
