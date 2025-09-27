"""
Predictor 51
Generated on: 2025-09-09 23:21:45
Accuracy: 40.24%
"""


# PREDICTOR 51 - Accuracy: 40.24%
# Correct predictions: 4024/10000 (40.24%)

def predict_output(A, B, C, D, E):
    # Conditions for 3
    if C < 5 and D > 50:
        return 3
    if B < 10 and D > 80:
        return 3
    if C > 90 and D > 90:
        return 3
    if A < 5 and C < 10:
        return 3
    # Conditions for 2
    if C > 90 and D < 10:
        return 2
    if B > 70 and C > 80:
        return 2
    if B > 90:
        return 2
    if A > 90 and E < 10:
        return 2
    if B < 10 and C > 90:
        if A > 60:
            return 4
        else:
            return 2
    # Conditions for 4
    if A < 10 and B > 70:
        return 4
    if C < 20 and D > 40:
        return 4
    if D > 50 and E < 20:
        return 4
    if B > 60 and E < 20:
        return 4
    if C > 70 and E > 60:
        return 4
    if C > 70 and B < 30 and E < 40:
        return 4
    else:
        return 1