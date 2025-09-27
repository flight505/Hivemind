"""
Predictor 29
Generated on: 2025-09-09 05:03:09
Accuracy: 52.75%
"""


# PREDICTOR 29 - Accuracy: 52.75%
# Correct predictions: 5275/10000 (52.75%)

def predict_output(A, B, C, D, E):
    # Class 1: very high values
    if (A >= 85 and B >= 85 and C >= 85 and D >= 85 and E >= 50) or (B >= 100):
        return 1
    
    # Class 2 conditions
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or (B >= 90 and C >= 70) or (B >= 80 and E >= 90):
        return 2
    
    # Class 3 conditions: low B and C, or specific patterns with E
    if (B <= 15 and C <= 12 and E < 40) or (B >= 80 and C <= 25 and E <= 50):
        return 3
    
    # Class 4 conditions: expanded range and special cases
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (B >= 35 and B <= 45 and D >= 50 and D <= 60) or \
       (E >= 90) or \
       (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
       (B >= 80 and E >= 80 and C < 50) or \
       (B >= 60 and C <= 20) or \
       (B <= 10 and E < 20) or \
       (B <= 20 and D >= 50 and E <= 25):
        return 4
    
    # Default to class 1
    return 1