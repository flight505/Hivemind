"""
Predictor 24
Generated on: 2025-09-09 12:55:24
Accuracy: 57.37%
"""


# PREDICTOR 24 - Accuracy: 57.37%
# Correct predictions: 5737/10000 (57.37%)

def predict_output(A, B, C, D, E):
    ed = E - D

    # Very low C base -> 3, but override to 1 when strong A/B/E present
    if C <= 12:
        if B >= 80 or (A >= 85 and E >= 55):
            return 1
        return 3

    # High C with very low D but very low E -> 1 (avoid false 2)
    if C >= 75 and D <= 10 and E <= 30:
        return 1

    # High C: strong 2 when D very low or B very high
    if C >= 75 and (D <= 10 or B >= 85):
        return 2

    # Near-high C with low D and high E -> 2
    if 70 <= C <= 75 and D <= 15 and E >= 80:
        return 2

    # Class 4: E significantly exceeds D in low-to-mid C
    if C <= 45 and ed >= 35:
        return 4

    # Class 2: mid C with strong B and D
    if 45 <= C <= 60 and B >= 80 and D >= 50:
        return 2

    # Class 2: mid-low C with moderately high B/D and sufficient E
    if 35 <= C <= 50 and B >= 70 and D >= 45 and E >= 50:
        return 2

    # Class 2: low-mid C with very high B and high D
    if 30 <= C <= 40 and B >= 90 and D >= 60:
        return 2

    # Class 2: near-high C with high D and fairly high B
    if 65 <= C <= 75 and D >= 50 and B >= 75:
        return 2

    # Special 4: tiny A with strong B and mid C and low D
    if A <= 5 and B >= 80 and 50 <= C <= 60 and D <= 35:
        return 4

    return 1