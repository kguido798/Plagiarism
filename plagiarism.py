import os
import string

# The essay content
essay1_text = """ Programming is the backbone of software engineering, serving as the primary tool for transforming ideas into functional applications. It enables engineers to design, develop, and optimize software systems that solve real-world problems. Without programming, the theoretical aspects of software design would remain abstract and unusable. Mastery of programming languages allows engineers to implement algorithms, debug code, and ensure the efficiency of software. Furthermore, programming fosters creativity and innovation, as engineers can experiment with new solutions and technologies. In essence, programming is the bridge between concept and execution, making it indispensable in software engineering.
"""

essay2_text = """ Programming is a fundamental skill in software engineering, as it is the process through which software solutions are built and maintained. It allows engineers to create systems that automate tasks, improve productivity, and address complex challenges. By writing code, engineers can bring software designs to life, ensuring they meet user requirements and perform reliably. Additionally, programming encourages problem-solving and logical thinking, which are critical for optimizing software performance. As technology evolves, programming remains at the core of innovation, enabling engineers to adapt and develop cutting-edge applications. Thus, programming is not just a skill but a necessity in the field of software engineering.
"""
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

