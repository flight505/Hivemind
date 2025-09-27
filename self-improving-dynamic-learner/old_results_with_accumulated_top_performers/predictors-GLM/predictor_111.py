"""
Predictor 111
Generated on: 2025-09-09 07:40:29
Accuracy: 54.77%
"""


# PREDICTOR 111 - Accuracy: 54.77%
# Correct predictions: 5477/10000 (54.77%)

def predict_output(A, B, C, D, E):
    # Class 3: low B, low C, low E patterns
    if B <= 15 and C <= 12 and E < 40:
        return 3
    # Class 4: specific B and D ranges or very high E
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or (E >= 90):
        return 4
    # Class 2: high B with moderate A and high C, or very high B and C
    elif (B >= 65 and A <= 50 and A > 20 and C >= 70) or (B >= 90 and C >= 80):
        return 2
    # Default to class 1
    else:
        return 1