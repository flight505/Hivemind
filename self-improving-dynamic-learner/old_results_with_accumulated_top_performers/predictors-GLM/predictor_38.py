"""
Predictor 38
Generated on: 2025-09-09 05:27:28
Accuracy: 54.91%
"""


# PREDICTOR 38 - Accuracy: 54.91%
# Correct predictions: 5491/10000 (54.91%)

def predict_output(A, B, C, D, E):
    # Class 1 conditions
    if (E >= 90 and D < 80 and C >= 70 and B < 50) or \
       (B >= 95 and D < 20 and C <= 70):
        return 1
    
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B >= 40 and B <= 60 and C >= 40 and C <= 50 and E >= 90) or \
       (E < 20 and B > 60 and C < 50 and D > 80) or \
       (E < 20 and B >= 75 and C <= 10) or \
       (B >= 60 and C < 50 and D < 50 and E < 50):
        return 3
    
    # Class 2 conditions
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
       (B >= 90 and C >= 80) or \
       (B >= 85 and A >= 80 and C >= 40 and C <= 50 and E >= 70) or \
       (B >= 85 and E >= 90 and C >= 50 and C <= 70):
        return 2
    
    # Class 4 conditions
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (B <= 10 and C >= 70) or \
       (B >= 80 and E >= 80) or \
       (B >= 55 and B <= 60 and C >= 60 and D >= 15 and D <= 25) or \
       (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
       (B <= 10 and D >= 40 and E < 10) or \
       (B >= 50 and B <= 60 and C >= 80 and D <= 20) or \
       (B >= 75 and C <= 10 and E >= 20) or \
       (C <= 10 and D >= 90) or \
       (A >= 90 and B <= 10 and E >= 60) or \
       (B <= 20 and D >= 50 and E <= 25) or \
       (E >= 90 and D < 80 and 
        not (B <= 20 and C >= 50) and 
        not (B >= 30 and C >= 70) and 
        not (B >= 50 and C >= 70)):
        return 4
    
    # Default to class 1
    return 1