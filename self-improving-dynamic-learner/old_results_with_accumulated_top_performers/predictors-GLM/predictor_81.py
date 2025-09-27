"""
Predictor 81
Generated on: 2025-09-09 06:21:17
Accuracy: 53.07%
"""


# PREDICTOR 81 - Accuracy: 53.07%
# Correct predictions: 5307/10000 (53.07%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or (B >= 70 and C <= 30 and D <= 40):
        return 3
    
    # Class 4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (E >= 90) or \
         (C <= 10 and D >= 90) or \
         (B >= 80 and E >= 80) or \
         (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
         (B <= 10 and D >= 40 and E < 10) or \
         (A >= 90 and B <= 10 and E >= 60):
        return 4
    
    # Class 2 conditions
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or (B >= 90 and C >= 80):
        return 2
    
    # Default to class 1
    else:
        return 1