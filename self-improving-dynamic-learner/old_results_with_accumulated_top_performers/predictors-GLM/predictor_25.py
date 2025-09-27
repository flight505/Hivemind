"""
Predictor 25
Generated on: 2025-09-09 04:53:45
Accuracy: 51.40%
"""


# PREDICTOR 25 - Accuracy: 51.40%
# Correct predictions: 5140/10000 (51.40%)

def predict_output(A, B, C, D, E):
    # Class 1 conditions: very high values
    if B >= 90 and C >= 90:
        return 1
    
    # Class 3 conditions: low values and specific patterns
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 20 and C <= 5 and E < 40) or \
       (B <= 15 and E < 40 and D > 70 and D < 85) or \
       (E < 10 and C < 50 and B > 50) or \
       (B <= 15 and C <= 10 and E < 50) or \
       (E < 30 and D > 80 and B > 60) or \
       (B >= 60 and E <= 35 and D >= 60) or \
       (B >= 20 and B <= 30 and C >= 40 and D >= 70) or \
       (E < 20 and D < 20 and B < 80):
        return 3
    
    # Class 4 conditions: specific ranges and combinations
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (B >= 80 and E >= 80 and C < 50) or \
       (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
       (B <= 10 and D >= 40 and E < 10) or \
       (B >= 75 and C <= 10) or \
       (C <= 10 and D >= 90) or \
       (A >= 90 and B <= 10 and E >= 60) or \
       (B <= 20 and C >= 90) or \
       (C >= 70 and D <= 20) or \
       (B >= 60 and E >= 80 and C < 90) or \
       (B >= 30 and B <= 45 and D >= 30 and D <= 40) or \
       (B <= 20 and C <= 25 and E >= 70) or \
       (C <= 10 and D >= 50 and E >= 60) or \
       (B >= 20 and B <= 25 and D >= 35 and D <= 40) or \
       (B >= 28 and B <= 36 and D > 36 and D <= 60 and C >= 90):
        return 4
    
    # Class 2 conditions: high values with constraints
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
       (B >= 90 and C >= 80) or \
       (B >= 90 and E >= 90 and C >= 50) or \
       (B >= 80 and C >= 40 and D >= 50):
        return 2
    
    # Default to class 1
    return 1