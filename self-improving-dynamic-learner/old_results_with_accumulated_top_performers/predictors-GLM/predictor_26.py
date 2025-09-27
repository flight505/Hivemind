"""
Predictor 26
Generated on: 2025-09-09 04:57:03
Accuracy: 52.57%
"""


# PREDICTOR 26 - Accuracy: 52.57%
# Correct predictions: 5257/10000 (52.57%)

def predict_output(A, B, C, D, E):
    # Class 1: very high values
    if B >= 85 and C >= 85 and D >= 85 and E >= 50:
        return 1
    
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B >= 50 and C <= 25 and E <= 35) or \
       (B >= 60 and D <= 10):
        return 3
    
    # Class 4 conditions
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (B >= 70 and C <= 30 and D <= 80) or \
       (B <= 10 and C >= 60):
        return 4
    
    # Class 2 conditions
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
       (B >= 90 and C >= 80) or \
       (B >= 90 and E >= 80) or \
       (B >= 85 and C <= 20):
        return 2
    
    # Default to class 1
    return 1