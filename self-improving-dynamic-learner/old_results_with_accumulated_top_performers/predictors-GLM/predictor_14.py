"""
Predictor 14
Generated on: 2025-09-09 04:24:49
Accuracy: 50.71%
"""


# PREDICTOR 14 - Accuracy: 50.71%
# Correct predictions: 5071/10000 (50.71%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C < 50) or (C <= 10):
        return 3
    
    # Class 4 conditions
    if E >= 90 and C >= 60:
        return 1
    if E >= 90:
        return 4
    if A > 80 and C < 10 and D < 20:
        return 1
    if B >= 28 and B <= 36 and D >= 15 and D <= 36:
        return 4
    if B >= 80 and E >= 80:
        return 4
    if B <= 10 and C <= 5 and D >= 60 and E >= 60:
        return 4
    if B <= 10 and D >= 40 and E < 10:
        return 4
    if B >= 75 and C <= 10 and not (A > 80 and D < 20):
        return 4
    if C <= 10 and D >= 90:
        return 4
    if A >= 90 and B <= 10 and E >= 60:
        return 4
    if B <= 20 and D >= 50 and E <= 25:
        return 4
    if C >= 90 and B < 30 and E < 20:
        return 4
    
    # Class 2 conditions
    if A <= 10 and B >= 70:
        return 2
    if A <= 20 and B >= 45 and C <= 30:
        return 2
    if A >= 70 and B >= 70 and E <= 10:
        return 2
    if B >= 75 and C >= 45 and D >= 40 and D <= 90:
        return 2
    if (B >= 65 and A <= 50 and C >= 70 and A > 20):
        return 2
    if (B >= 80 and A >= 90 and C >= 40):
        return 2
    
    # Default to class 1
    return 1