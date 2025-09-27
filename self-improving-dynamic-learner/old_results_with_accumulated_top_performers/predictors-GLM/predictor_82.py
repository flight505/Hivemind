"""
Predictor 82
Generated on: 2025-09-09 06:23:45
Accuracy: 48.45%
"""


# PREDICTOR 82 - Accuracy: 48.45%
# Correct predictions: 4845/10000 (48.45%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (E <= 30 and B >= 75) or \
       (E <= 5 and D <= 10) or \
       (D >= 90 and E >= 70 and B >= 60):
        return 3
    
    # Class 4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (E >= 90 and not (A <= 10 and B >= 40 and C <= 10)) or \
         (C <= 10 and D >= 90) or \
         (B >= 80 and E >= 80) or \
         (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
         (B <= 10 and D >= 40 and E < 10) or \
         (A >= 90 and B <= 10 and E >= 60) or \
         (B >= 40 and B <= 50 and C >= 60 and D >= 40) or \
         (B <= 20 and D >= 20 and E <= 25) or \
         (E >= 80 and B >= 30 and B <= 40 and C >= 60):
        return 4
    
    # Class 2 conditions
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20 and D <= 10) or \
         (B >= 90 and C >= 80) or \
         (A <= 10 and B >= 40 and C <= 10):
        return 2
    
    # Default to class 1
    else:
        return 1