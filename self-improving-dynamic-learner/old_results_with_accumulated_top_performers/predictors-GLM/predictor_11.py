"""
Predictor 11
Generated on: 2025-09-09 04:15:26
Accuracy: 57.00%
"""


# PREDICTOR 11 - Accuracy: 57.00%
# Correct predictions: 5700/10000 (57.00%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if B <= 15 and C <= 12 and E < 40:
        return 3
    
    # Class 4 conditions
    if B >= 28 and B <= 36 and D >= 15 and D <= 36:
        return 4
    if B >= 80 and E >= 80:
        return 4
    if B <= 10 and C <= 5 and D >= 60 and E >= 60:
        return 4
    if B <= 10 and D >= 40 and E < 10:
        return 4
    if B >= 75 and C <= 10:
        return 4
    if C <= 10 and D >= 90:
        return 4
    if A >= 90 and B <= 10 and E >= 60:
        return 4
    if B <= 20 and D >= 50 and E <= 25:
        return 4
    
    # Class 2 conditions
    if B >= 65 and A <= 50 and C >= 70 and A > 20:
        return 2
    if B >= 90 and C >= 80:
        return 2
    
    # Default to class 1
    return 1