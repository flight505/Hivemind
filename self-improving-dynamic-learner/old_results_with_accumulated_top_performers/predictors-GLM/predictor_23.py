"""
Predictor 23
Generated on: 2025-09-09 04:48:21
Accuracy: 49.47%
"""


# PREDICTOR 23 - Accuracy: 49.47%
# Correct predictions: 4947/10000 (49.47%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or (C <= 10 and E < 50) or (E < 10 and C < 50 and B > 50) or (B <= 15 and E < 40 and D > 70 and D < 85):
        return 3
    
    # Class 4 conditions
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (E >= 90 and D < 80) or \
       (B >= 80 and E >= 80) or \
       (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
       (B <= 10 and D >= 40 and E < 10) or \
       (B >= 75 and C <= 10) or \
       (C <= 10 and D >= 90) or \
       (A >= 90 and B <= 10 and E >= 60) or \
       (B <= 30 and D <= 30 and C > 70) or \
       (B <= 30 and D >= 50 and E <= 25 and A > 60) or \
       (E <= 5 and D >= 70) or \
       (E >= 75 and B <= 25) or \
       (B <= 20 and D >= 50):
        return 4
    
    # Class 2 conditions
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
       (B >= 90 and C >= 30 and A <= 50) or \
       (B >= 60 and D <= 20 and E >= 70):
        return 2
    
    # Default to class 1
    return 1