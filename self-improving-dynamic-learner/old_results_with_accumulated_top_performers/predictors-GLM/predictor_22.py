"""
Predictor 22
Generated on: 2025-09-09 04:43:43
Accuracy: 49.99%
"""


# PREDICTOR 22 - Accuracy: 49.99%
# Correct predictions: 4999/10000 (49.99%)

def predict_output(A, B, C, D, E):
    # Handle the specific case that was misclassified as 4 instead of 1 (error 7)
    if A >= 90 and B >= 28 and B <= 36 and D >= 15 and D <= 36:
        return 1

    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 20 and C <= 5 and E < 40) or \
       (B <= 20 and E < 40 and D >= 80) or \
       (B >= 60 and D <= 10 and E <= 40):
        return 3

    # Class 4 conditions
    if (B >= 28 and B <= 36 and D >= 15 and D <= 50) or \
       (B >= 80 and E >= 80) or \
       (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
       (B <= 10 and D >= 40 and E < 10) or \
       (B >= 75 and C <= 10) or \
       (C <= 10 and D >= 90) or \
       (A >= 90 and B <= 10 and E >= 60) or \
       (B <= 20 and C >= 80) or \
       (B >= 40 and C >= 20 and D >= 70 and E >= 70) or \
       (B <= 10 and C <= 10 and D >= 50):
        return 4

    # Class 2 conditions
    if (B >= 60 and A <= 50 and C >= 40 and A > 20) or \
       (B >= 90 and C >= 80) or \
       (B >= 70 and A <= 20) or \
       (B >= 60 and C >= 40 and E >= 90):
        return 2

    # Default to class 1
    return 1