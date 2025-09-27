"""
Predictor 19
Generated on: 2025-09-09 04:39:27
Accuracy: 56.16%
"""


# PREDICTOR 19 - Accuracy: 56.16%
# Correct predictions: 5616/10000 (56.16%)

def predict_output(A, B, C, D, E):
    # Class 1: very high values
    if A >= 95 and B >= 90 and C >= 90 and D >= 80 and E >= 90:
        return 1
    
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 20 and D <= 10 and E < 30) or \
       (B <= 15 and D <= 10) or \
       (B <= 15 and E <= 10) or \
       (B <= 30 and D >= 80 and C < 50 and E >= 20):
        return 3
    
    # Class 4 conditions
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (B >= 80 and E >= 80 and C < 50) or \
       (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
       (B <= 10 and D >= 40 and E < 10) or \
       (B >= 75 and C <= 10) or \
       (C <= 10 and D >= 90) or \
       (A >= 90 and B <= 10 and E >= 60) or \
       (B <= 20 and D >= 50 and E <= 25) or \
       (B >= 90 and C <= 10) or \
       (B >= 50 and C <= 20 and E >= 90) or \
       (C <= 5 and B >= 50 and E >= 70) or \
       (C >= 60 and B <= 30 and E <= 20) or \
       (B <= 20 and C >= 90):
        return 4
    
    # Class 2 conditions
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
       (B >= 90 and C >= 80):
        return 2
    
    # Default to class 1
    return 1