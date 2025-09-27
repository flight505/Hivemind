"""
Predictor 31
Generated on: 2025-09-09 05:07:18
Accuracy: 55.86%
"""


# PREDICTOR 31 - Accuracy: 55.86%
# Correct predictions: 5586/10000 (55.86%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if B <= 15 and C <= 12 and E < 40:
        return 3
    
    # Class 4 conditions
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (C <= 10 and D >= 90 and B > 15) or \
       (C <= 10 and D >= 60 and E >= 60) or \
       (B <= 15 and D >= 40 and E <= 10) or \
       (E >= 90) or \
       (B >= 80 and E >= 80) or \
       (D >= 30 and D <= 36 and E >= 60):
        return 4
    
    # Class 2 conditions
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
       (B >= 90 and C >= 80):
        return 2
    
    # Default to class 1
    return 1