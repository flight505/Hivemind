"""
Predictor 70
Generated on: 2025-09-09 06:07:44
Accuracy: 54.03%
"""


# PREDICTOR 70 - Accuracy: 54.03%
# Correct predictions: 5403/10000 (54.03%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (E < 20 and D >= 60 and B > 40) or \
       (E < 20 and E >= 10 and D < 20):
        return 3
    
    # Class 4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (E >= 90 and D < 80 and B < 50 and C < 60) or \
         (B <= 20 and D >= 50 and E <= 25) or \
         (B >= 75 and C <= 10) or \
         (A >= 75 and B >= 60 and C <= 20):
        return 4
    
    # Class 2 conditions
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
         (B >= 90 and C >= 80) or \
         (B >= 70 and A <= 30 and D >= 60):
        return 2
    
    # Default to class 1
    else:
        return 1