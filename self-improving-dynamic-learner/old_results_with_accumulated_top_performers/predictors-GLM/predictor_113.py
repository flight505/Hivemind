"""
Predictor 113
Generated on: 2025-09-09 07:42:44
Accuracy: 44.46%
"""


# PREDICTOR 113 - Accuracy: 44.46%
# Correct predictions: 4446/10000 (44.46%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions: low B, low C, low E patterns
    if (B <= 15 and C <= 12 and E < 40) or (C <= 10 and E < 40) or (E <= 20 and B >= 60) or (E <= 25 and C < 50 and D >= 60):
        return 3
    # Class 4 conditions: specific B and D ranges or very high E or other patterns
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or (E >= 90) or (B >= 95 and C <= 15) or (B <= 20 and D >= 50 and E <= 25) or (E <= 10 and B >= 30) or (B <= 10 and C >= 90) or (D <= 10 and E >= 70) or (B <= 15 and D >= 70):
        return 4
    # Class 2 conditions: high B with moderate A and high C, or very high B and C, or high B alone
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or (B >= 90 and C >= 80) or (B >= 85 and B <= 95 and A >= 45) or (A <= 20 and B >= 80):
        return 2
    # Special exception cases
    elif (A >= 90 and B >= 90 and C >= 95) or (E >= 95 and B <= 15) or (A <= 10 and B <= 15 and C >= 90):
        return 1
    # Default to class 1
    else:
        return 1