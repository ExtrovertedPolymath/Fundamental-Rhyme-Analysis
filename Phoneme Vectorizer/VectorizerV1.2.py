import numpy as np

# ====== 1. IPA VECTOR DATABASE (Consonants + Vowels, Pulmonic + Non-Pulmonic) ======

ipa_vectors = {
    # === Pulmonic Consonants ===
    'p': [0, 10, 0, 0, 0], 'b': [1, 10, 0, 0, 0],   # Bilabial plosives
    't': [0, 7, 0, 0, 0], 'd': [1, 7, 0, 0, 0],     # Alveolar plosives
    'k': [0, 3, 0, 0, 0], 'g': [1, 3, 0, 0, 0],     # Velar plosives
    'f': [0, 9, 4, 0, 0], 'v': [1, 9, 4, 0, 0],     # Labiodental fricatives
    's': [0, 7, 4, 0, 0], 'z': [1, 7, 4, 0, 0],     # Alveolar fricatives
    'ʃ': [0, 6, 4, 0, 0], 'ʒ': [1, 6, 4, 0, 0],     # Postalveolar fricatives
    'h': [0, 0, 4, 0, 0],                           # Glottal fricative
    'm': [1, 10, 2, 1, 0], 'n': [1, 7, 2, 1, 0],    # Nasals
    'ŋ': [1, 3, 2, 1, 0],                           # Velar nasal
    'l': [1, 7, 6, 0, 1],                           # Lateral approximant
    'r': [1, 7, 6, 0, 0],                           # Alveolar trill
    'j': [1, 4, 6, 0, 0], 'w': [1, 10, 6, 0, 0],    # Approximants

    # === Non-Pulmonic Consonants (Clicks, Implosives, Ejectives) ===
    'ɓ': [1, 10, 0, 0, 0],  # Voiced bilabial implosive
    'ɗ': [1, 7, 0, 0, 0],   # Voiced alveolar implosive
    'ʄ': [1, 4, 0, 0, 0],   # Voiced palatal implosive
    'ɠ': [1, 3, 0, 0, 0],   # Voiced velar implosive
    'ʛ': [1, 1, 0, 0, 0],   # Voiced uvular implosive
    'ǃ': [0, 1, 0, 0, 0],   # Postalveolar click (default values for placeholder)
    'ǀ': [0, 7, 0, 0, 0],   # Dental click
    'ǂ': [0, 4, 0, 0, 0],   # Palatal click
    'ʼ': [0, 7, 0, 0, 0],   # Ejective (placeholder)

    # === Vowels ===
    'i': [0, 0, 0], 'y': [0, 0, 1],                 # Close front
    'e': [1, 0, 0], 'ø': [1, 0, 1],                 # Mid front
    'æ': [2, 0, 0], 'ɛ': [1, 0, 0],                 # Near-open front
    'ɑ': [2, 2, 0], 'ɒ': [2, 2, 1],                 # Open back
    'o': [1, 2, 1], 'u': [0, 2, 1],                 # Close back
    'ə': [1, 1, 0],                                  # Schwa
    'ɪ': [0, 0, 0], 'ʊ': [0, 2, 1],                 # Lax vowels
}

# ====== 2. DIMENSION LENGTH SETUP ======
dimensionality = {
    'consonant': 5,
    'vowel': 3
}
max_distance = {
    5: np.linalg.norm(np.array([1, 10, 7, 1, 1])),  # Max range for consonants
    3: np.linalg.norm(np.array([2, 2, 1]))          # Max range for vowels
}

# ====== 3. SONIC PROXIMITY SCORE (SPS) FUNCTION ======
def calculate_sps(p1, p2):
    if p1 not in ipa_vectors or p2 not in ipa_vectors:
        return "Error: One or both phonemes not in the database."

    vec1 = np.array(ipa_vectors[p1])
    vec2 = np.array(ipa_vectors[p2])

    if len(vec1) != len(vec2):
        return "Error: Cannot compare vowel and consonant directly."

    d = np.linalg.norm(vec1 - vec2)
    d_max = max_distance[len(vec1)]

    sps = 1 - (d / d_max)
    return round(sps, 4)

# ====== 4. INTERACTIVE CLI ======
def interactive_sps_tool():
    print("Enter two IPA phonemes to calculate Sonic Proximity Score (SPS).")
    p1 = input("Phoneme 1: ").strip()
    p2 = input("Phoneme 2: ").strip()
    result = calculate_sps(p1, p2)
    print(f"\nSonic Proximity Score (SPS): {result} / 1.0")

# Run it!
if __name__ == "__main__":
    interactive_sps_tool()

