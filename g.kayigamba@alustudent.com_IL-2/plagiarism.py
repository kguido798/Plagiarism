import os
import string
from collections import Counter

def preprocess_text(file_path):
    """Reads a text file, removes punctuation, and returns list of words + word frequency."""
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.translate(translator)
        words = clean_text.lower().split()
        return words, Counter(words)
    except FileNotFoundError:
        print(f"❌ Error: '{os.path.basename(file_path)}' not found.")
        return None, None

# Ensure user enters valid filename
def get_valid_filename(prompt):
    while True:
        filename = input(prompt)
        if not filename.endswith(".txt"):
            filename += ".txt"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        if os.path.isfile(file_path):
            return file_path
        else:
            print(f"⚠️  File '{filename}' not found. Try again.")

# Get both valid essay paths
file1_path = get_valid_filename("Enter the first essay filename (e.g. essay1.txt): ")
file2_path = get_valid_filename("Enter the second essay filename (e.g. essay2.txt): ")

# Preprocess both essays
words1, freq1 = preprocess_text(file1_path)
words2, freq2 = preprocess_text(file2_path)

# Exit if any file failed to load
if words1 is None or words2 is None:
    input("\nPress Enter to exit...")
    exit()

# Sets for plagiarism calculation
set1 = set(words1)
set2 = set(words2)
common_words = set1.intersection(set2)
all_unique_words = set1.union(set2)

# ✅ Plagiarism calculation
plagiarism_percentage = (len(common_words) / len(all_unique_words)) * 100

# ✅ Print common words with their counts
print("\n📝 Common Words and Frequencies:")
for word in sorted(common_words):
    print(f"'{word}': Essay 1 = {freq1[word]} times | Essay 2 = {freq2[word]} times")

# ✅ Search for specific word
search_word = input("\n🔍 Enter a word to search in both essays: ").lower()
count1 = freq1.get(search_word, 0)
count2 = freq2.get(search_word, 0)

if count1 == 0 and count2 == 0:
    print(f"❌ The word '{search_word}' was not found in either essay. → Result: False")
else:
    print(f"✅ Word '{search_word}' found:")
    print(f"   Essay 1: {count1} time(s)")
    print(f"   Essay 2: {count2} time(s)")
    print("→ Result: True")

# ✅ Final plagiarism result
print(f"\n📊 Plagiarism Percentage: {plagiarism_percentage:.2f}%")
if plagiarism_percentage >= 50:
    print("⚠️  Result: Plagiarism Detected!")
else:
    print("✅ Result: No Plagiarism Detected.")

input("\nPress Enter to exit...")
