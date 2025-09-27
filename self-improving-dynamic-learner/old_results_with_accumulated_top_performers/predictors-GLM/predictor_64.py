"""
Predictor 64
Generated on: 2025-09-09 06:01:45
Accuracy: 56.31%
"""


# PREDICTOR 64 - Accuracy: 56.31%
# Correct predictions: 5631/10000 (56.31%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 30 and D >= 80 and C < 50 and E >= 20) or \
       (E < 10 and C < 50 and B > 50 and (A > 40 or D < 60)) or \
       (E < 10 and C >= 70 and D >= 90) or \
       (E < 10 and B >= 80 and C >= 80):
        return 3
    
    # Class 4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (B >= 80 and C <= 35 and D >= 60 and A >= 50) or \
         (B <= 25 and D >= 50 and E <= 20) or \
         (C <= 10 and D >= 40 and E >= 60):
        return 4
    
    # Class 2 conditions
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
         (B >= 90 and C >= 80) or \
         (B >= 65 and C < 50 and D >= 60 and A <= 40):
        return 2
    
    # Default to class 1
    else:
        return 1