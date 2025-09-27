"""
Predictor 32
Generated on: 2025-09-09 05:10:51
Accuracy: 55.04%
"""


# PREDICTOR 32 - Accuracy: 55.04%
# Correct predictions: 5504/10000 (55.04%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if B <= 15 and C <= 12 and E < 40:
        return 3
    if B <= 32 and C < 50 and E < 40 and A >= 90:
        return 3
    if B <= 32 and C < 50 and E < 40 and A < 90 and D < 80:
        return 3
    if C <= 10 and E <= 10 and D < 40:
        return 3
    if D <= 10 and E < 20:
        return 3
    if C >= 90 and A <= 50 and B >= 60:
        return 3
    
    # Class 4 conditions
    if B >= 28 and B <= 36 and D >= 15 and D <= 36:
        return 4
    if D >= 15 and D <= 36 and C >= 80 and E >= 50:
        return 4
    if B >= 70 and C <= 20 and E >= 50:
        return 4
    if C <= 10 and D >= 90 and B > 15:
        return 4
    if C <= 10 and D >= 60 and E >= 60:
        return 4
    if B <= 15 and D >= 40 and E <= 10:
        return 4
    if E >= 90:
        return 4
    if B >= 80 and E >= 80:
        return 4
    if D >= 30 and D <= 36 and E >= 60:
        return 4
    
    # Class 2 conditions
    if (B >= 65 and A <= 50 and C >= 70 and A > 20):
        return 2
    if (B >= 65 and A <= 50 and E < 10 and C >= 35):
        return 2
    if (B >= 80 and A >= 80 and C >= 50 and D >= 30):
        return 2
    
    # Default to class 1
    return 1