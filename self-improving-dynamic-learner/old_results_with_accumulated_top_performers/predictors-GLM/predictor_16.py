"""
Predictor 16
Generated on: 2025-09-09 04:31:11
Accuracy: 54.28%
"""


# PREDICTOR 16 - Accuracy: 54.28%
# Correct predictions: 5428/10000 (54.28%)

def predict_output(A, B, C, D, E):
    # Class 1 conditions
    if A >= 85 and B >= 85 and C >= 85 and D >= 85 and E >= 50:
        return 1
    
    # Class 3 conditions
    if B <= 15 and C < 50 and E < 50 and D <= 80 and A < 80:
        return 3
    if C <= 10 and E < 50 and D < 85:
        return 3
    if E < 10 and C < 50 and B > 50 and D < 70:
        return 3
    if C < 50 and E < 30 and D > 70 and D < 85:
        return 3
    if B >= 45 and B <= 50 and C < 20:
        return 3
    if D <= 5 and E < 25:
        return 3
    if D >= 70 and E >= 80 and B >= 60:
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
    if D < 10 and E > 40:
        return 4
    if E < 10 and D > 70:
        return 4
    if E >= 80 and B >= 70:
        return 4
    if C <= 10 and D >= 80:
        return 4
    
    # Class 2 conditions
    if B >= 65 and A <= 50 and C >= 70 and A > 20:
        return 2
    if B >= 90 and C >= 80:
        return 2
    if B >= 90 and D >= 60:
        return 2
    if A <= 10 and B >= 70 and C >= 40:
        return 2
    
    # Default to class 1
    return 1