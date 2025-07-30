import os
import string

def preprocess_text(file_path):
    """Reads a text file, removes punctuation, and converts to a set of lowercase words."""
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.translate(translator)
        words = clean_text.lower().split()
        return set(words)
    except FileNotFoundError:
        print(f"❌ Error: '{file_path}' not found.")
        return set()

def calculate_plagiarism(set1, set2):
    """Calculates the percentage of shared words between two sets."""
    if not set1:
        return 0.0
    shared_words = set1.intersection(set2)
    percentage = (len(shared_words) / len(set1)) * 100
    return round(percentage, 2)

# Ask the user for input files
file1 = input("Enter the first essay filename (e.g. essay1.txt): ")
file2 = input("Enter the second essay filename (e.g. essay2.txt): ")

if not file1.endswith(".txt"):
    file1 += ".txt"
if not file2.endswith(".txt"):
    file2 += ".txt"
# Preprocess both essays
essay1_words = preprocess_text(file1)
essay2_words = preprocess_text(file2)

# Only continue if both files were read successfully
if essay1_words and essay2_words:
    # Calculate plagiarism
    plagiarism_percentage = calculate_plagiarism(essay1_words, essay2_words)

    # Display result
    print(f"\nPlagiarism Percentage: {plagiarism_percentage}%")

    if plagiarism_percentage >= 30.0:
        print("⚠️  Result: Plagiarism Detected!")
    else:
        print("✅  Result: No Plagiarism Detected.")
input("\nPress Enter to exit...")

