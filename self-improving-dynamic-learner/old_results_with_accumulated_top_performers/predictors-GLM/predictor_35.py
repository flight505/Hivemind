"""
Predictor 35
Generated on: 2025-09-09 05:22:17
Accuracy: 53.50%
"""


# PREDICTOR 35 - Accuracy: 53.50%
# Correct predictions: 5350/10000 (53.50%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B >= 40 and B <= 60 and C >= 40 and C <= 50 and E >= 90) or \
       (B >= 55 and B <= 60 and C >= 60 and C <= 65) or \
       (C >= 85 and E < 10):
        return 3
    
    # Class 2 conditions
    if (B >= 65 and A <= 50 and C >= 70 and A > 20 and D >= 20 and C <= 90) or \
       (A <= 30 and E >= 70) or \
       (B >= 55 and B <= 65 and C >= 40 and C <= 50 and E >= 60):
        return 2
    
    # Class 4 conditions
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (B <= 10 and C >= 70 and C <= 90) or \
       (B >= 80 and E >= 80) or \
       (B >= 55 and B <= 60 and C >= 60 and D >= 15 and D <= 25) or \
       (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
       (B <= 10 and D >= 40 and E < 10) or \
       (B >= 75 and C <= 10) or \
       (C <= 10 and D >= 90) or \
       (A >= 90 and B <= 10 and E >= 60) or \
       (B <= 20 and D >= 50 and E <= 25) or \
       (E >= 90 and D < 80 and not (B <= 20 and C >= 50) and not (B >= 30 and C >= 70)) or \
       (B >= 30 and B <= 40 and C >= 80 and D <= 20 and E >= 40) or \
       (B <= 20 and C <= 10 and D >= 50):
        return 4
    
    # Default to class 1
    return 1