#Count most frequest character

def most_frequent_char(text):
    freq = {}  # Dictionary to store frequency

    for char in text:
        if char != " ":  # Optional: ignore spaces
            freq[char] = freq.get(char, 0) + 1

    # Find the character with the highest frequency
    max_char = max(freq, key=freq.get)
    return max_char, freq[max_char]

# Example usage
input_text = input("Enter a string:")
char, count = most_frequent_char(input_text)
print(f"The most frequent character is '{char}' and it appears {count} times.")
