"""
Predictor 41
Generated on: 2025-09-09 05:29:34
Accuracy: 55.08%
"""


# PREDICTOR 41 - Accuracy: 55.08%
# Correct predictions: 5508/10000 (55.08%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions: low B values with specific C and E ranges
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 20 and E < 20 and C < 50):
        return 3
    
    # Class 4 conditions: specific B and D ranges, high E with low C, or extreme value combinations
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (E >= 90 and B < 50) or \
       (B <= 20 and D >= 50 and E <= 25) or \
       (C <= 10 and D >= 90) or \
       (B >= 75 and C <= 10) or \
       (B >= 80 and E >= 80):
        return 4
    
    # Class 2 conditions: high B with moderate A and high C, or very high B and C
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
       (B >= 90 and C >= 80) or \
       (B >= 85 and A >= 80 and E >= 70):
        return 2
    
    # Default to class 1 for all other cases
    return 1