"""
Predictor 42
Generated on: 2025-09-09 05:34:32
Accuracy: 55.94%
"""


# PREDICTOR 42 - Accuracy: 55.94%
# Correct predictions: 5594/10000 (55.94%)

def predict_output(A, B, C, D, E):
    # Special case: very high balanced values
    if A >= 60 and B >= 90 and C >= 60 and D >= 70 and E >= 80:
        return 1
        
    # Class 3 conditions
    if (E < 10 and (B >= 60 or (B <= 30 and C < 50))) or \
       (B <= 15 and C <= 12 and E < 40) or \
       (B <= 20 and E < 20 and C < 50):
        return 3
    
    # Class 4 conditions
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (E >= 90 and B < 50 and C <= 60) or \
       (B <= 20 and D >= 50 and E <= 25) or \
       (C <= 10 and D >= 90) or \
       (B >= 75 and C <= 10) or \
       (B >= 75 and E >= 80 and D <= 40) or \
       (C <= 10 and D >= 50):
        return 4
    
    # Class 2 conditions
    if (A <= 20 and B >= 60 and D <= 10) or \
       (B >= 90 and C >= 80) or \
       (B >= 85 and D >= 80 and A >= 50) or \
       (B >= 80 and D >= 50 and E < 20) or \
       (B >= 65 and A <= 50 and C >= 70 and A > 20 and D <= 10):
        return 2
    
    # Default to class 1
    return 1