import string
from collections import Counter
import requests

# 1. Fetching the text dataset as provided in the task
url = "https://raw.githubusercontent.com/spyguessgame-boop/own_dataset/refs/heads/main/data.txt"
response = requests.get(url)
response.raise_for_status()

# Extracting and slicing the first 1000 characters
text_data = response.text[:1000]

print("--- Original Text Snippet ---")
print(text_data[:200] + "...\n")  # Printing a small preview of the raw text


# 2. Tokenization Function (with Bonus Challenges handled)
def tokenize_text(text):
    # [Bonus] Remove punctuation by converting text to lowercase and mapping punctuation to None
    # string.punctuation contains: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    clean_text = text.lower()
    clean_text = clean_text.translate(str.maketrans("", "", string.punctuation))

    # Tokenize the text into individual words using split()
    tokens = clean_text.split()

    return tokens


# 3. Processing the data
tokens = tokenize_text(text_data)

# [Bonus] Calculate token metrics using Counter
token_counts = Counter(tokens)
total_tokens = len(tokens)
most_common_token, highest_frequency = token_counts.most_common(1)[0]


# 4. Displaying the Results
print("--- Tokenization Results ---")
print(f"First 10 Tokens: {tokens[:10]}")
print(f"Total Number of Tokens: {total_tokens}")
print(f"Most Frequent Token: '{most_common_token}' (Appears {highest_frequency} times)")