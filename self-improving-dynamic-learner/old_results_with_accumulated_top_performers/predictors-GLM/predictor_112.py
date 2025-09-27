"""
Predictor 112
Generated on: 2025-09-09 07:42:22
Accuracy: 47.78%
"""


# PREDICTOR 112 - Accuracy: 47.78%
# Correct predictions: 4778/10000 (47.78%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions: low B, low C, low E patterns
    if (B <= 15 and C <= 12 and E < 40) or (C <= 10 and E < 40) or (B <= 20 and E < 20):
        return 3
    # Class 4 conditions: specific B and D ranges or very high E
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36 and A < 90) or (E >= 85) or (B >= 95 and C <= 10) or (D <= 10 and E >= 70) or (E <= 10 and B >= 40):
        return 4
    # Class 2 conditions: high B with moderate A and high C, or very high B and C, or very high B alone
    elif (B >= 65 and A <= 50 and A > 20 and C >= 70) or (B >= 90 and C >= 80) or (B >= 85):
        return 2
    # Exception case: very high A and very high C should be class 1
    elif A >= 90 and B >= 55 and C >= 95:
        return 1
    # Default to class 1
    else:
        return 1