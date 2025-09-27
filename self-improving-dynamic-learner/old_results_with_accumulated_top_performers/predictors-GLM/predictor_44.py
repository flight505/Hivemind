"""
Predictor 44
Generated on: 2025-09-09 05:36:59
Accuracy: 56.44%
"""


# PREDICTOR 44 - Accuracy: 56.44%
# Correct predictions: 5644/10000 (56.44%)

def predict_output(A, B, C, D, E):
    # Special case: very high values
    if A >= 90 and B >= 90 and C >= 80 and D >= 80:
        return 1
    
    # Class 3 conditions: low E with specific patterns
    if (E <= 16 and B >= 35 and B <= 40 and C >= 30 and C <= 40) or \
       (E <= 16 and D >= 45 and D <= 60 and C >= 35 and C <= 40) or \
       (B <= 15 and C <= 12 and E < 40) or \
       (E < 20 and B >= 60 and C < 50) or \
       (B <= 20 and E < 20 and C < 50):
        return 3
    
    # Class 4 conditions: specific patterns with moderate B and D ranges
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (E >= 90 and B < 50 and C <= 60) or \
       (B <= 20 and D >= 50 and E <= 25) or \
       (C <= 10 and D >= 90) or \
       (B >= 75 and C <= 10) or \
       (A >= 50 and B >= 55 and C <= 25 and E >= 90) or \
       (A <= 10 and B >= 90 and D <= 5) or \
       (C <= 20 and D >= 30 and E >= 90) or \
       (C <= 15 and B >= 60 and D >= 50):
        return 4
    
    # Class 2 conditions: high B with specific constraints
    if (B >= 65 and A <= 50 and C >= 70 and A > 20 and D <= 10) or \
       (B >= 90 and C >= 80) or \
       (A <= 10 and B >= 90 and C >= 70 and D <= 5):
        return 2
    
    # Default to class 1
    return 1