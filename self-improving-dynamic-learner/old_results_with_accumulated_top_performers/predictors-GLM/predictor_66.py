"""
Predictor 66
Generated on: 2025-09-09 06:03:57
Accuracy: 48.55%
"""


# PREDICTOR 66 - Accuracy: 48.55%
# Correct predictions: 4855/10000 (48.55%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 30 and D >= 80 and C < 50 and E >= 20) or \
       (D <= 10 and E < 40) or \
       (E < 15 and C < 50):
        return 3
    
    # Class 4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (B >= 80 and C <= 35 and D >= 60 and A >= 50) or \
         (A >= 75 and B >= 90 and C <= 45) or \
         (A >= 40 and B >= 90 and E >= 60) or \
         (C >= 50 and D >= 25 and E >= 80) or \
         (B >= 50 and B <= 60 and D >= 30 and E >= 80) or \
         (E >= 90 and D < 80 and B < 50):
        return 4
    
    # Class 2 conditions
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
         (B >= 90 and C >= 80) or \
         (C >= 80 and D <= 15 and E >= 90) or \
         (A <= 20 and B >= 90 and C >= 80 and D >= 80):
        return 2
    
    # Default to class 1
    else:
        return 1