"""
Predictor 57
Generated on: 2025-09-09 12:41:44
Accuracy: 54.50%
"""


# PREDICTOR 57 - Accuracy: 54.50%
# Correct predictions: 5450/10000 (54.50%)

def predict_output(A, B, C, D, E):
    # 4 conditions
    if B > 75 and C < 40 and E > 70:
        return 4
    if C < 25 and E > 70:
        return 4
    if B > 80 and E > 80 and C < 30:
        return 4
    if B < 20 and C > 70 and E < 35 and D < 30:
        return 4
    if B > 80 and C > 70 and E < 40:
        return 4
    if C > 50 and B > 45 and E < 30:
        return 4
    if C < 20 and E >= 50 and B < 40:
        return 4
    if E < 10 and B < 40 and C < 20:
        return 4
    # 3 conditions
    if B > 60 and C < 25 and E < 20 and D < 50:
        return 3
    if B > 60 and C < 45 and E < 25 and A < 70:
        return 3
    if B > 40 and C < 30 and E < 30 and B < 90 and A < 80:
        return 3
    if B < 25 and C < 40 and E < 40:
        return 3
    if B < 40 and C > 70 and E < 50 and D < 50:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if E < 15 and B > 40 and 30 < C < 50:
        return 3
    # 2 conditions
    if A < 50 and B > 60 and C > 70:
        return 2
    if B > 90 and 30 < C < 50:
        return 2
    if A + B > 160 and C < 40 and E < 45:
        return 2
    if A < 10 and B < 60 and C < 30 and E > 50:
        return 2
    if C > 60 and D < 10 and E > 50:
        return 2
    if B > 90 and C > 80:
        return 2
    return 1