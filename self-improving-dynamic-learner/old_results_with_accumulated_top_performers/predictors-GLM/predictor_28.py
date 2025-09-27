"""
Predictor 28
Generated on: 2025-09-09 05:02:48
Accuracy: 54.16%
"""


# PREDICTOR 28 - Accuracy: 54.16%
# Correct predictions: 5416/10000 (54.16%)

def predict_output(A, B, C, D, E):
    # Class 1 conditions
    if (B >= 85 and C >= 85 and D >= 85 and E >= 50) or (D >= 85 and (C >= 60 or A <= 30)):
        return 1
    
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B >= 50 and B < 60 and C <= 26 and E <= 35) or \
       (B <= 30 and C <= 35 and E < 40) or \
       (B >= 60 and D <= 10):
        return 3
    
    # Class 4 conditions
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (B >= 70 and C <= 30 and D <= 80) or \
       (B <= 10 and C >= 60) or \
       (E >= 90 and D < 80) or \
       (C <= 10 and D >= 60) or \
       (B >= 60 and C <= 20) or \
       (B >= 60 and B <= 70 and E >= 75):
        return 4
    
    # Class 2 conditions
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
       (B >= 90 and C >= 80) or \
       (B >= 90 and E >= 80) or \
       (B >= 85 and C <= 20) or \
       (B >= 90 and C <= 45 and E >= 50 and A > 30):
        return 2
    
    # Default to class 1
    return 1