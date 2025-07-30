import string

# Embed essay contents directly
essay1_text = """
This is the first essay content.
It talks about values, ethics, and Ubuntu leadership in Africa.
"""

essay2_text = """
This essay covers Ubuntu leadership in Africa and values.
It also highlights ethics and shared goals.
"""

def preprocess_text(text):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    words = clean_text.lower().split()
    return set(words)

words1 = preprocess_text(essay1_text)
words2 = preprocess_text(essay2_text)

common_words = words1.intersection(words2)
plagiarism_percentage = (len(common_words) / len(words1)) * 100

print(f"\nPlagiarism Percentage: {plagiarism_percentage:.2f}%")
if plagiarism_percentage > 30:
    print("⚠️  Result: Plagiarism Detected!")
else:
    print("✅  Result: No Plagiarism Detected.")

input("\nPress Enter to exit...")

