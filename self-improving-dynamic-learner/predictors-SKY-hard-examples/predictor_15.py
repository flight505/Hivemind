"""
Predictor 15
Generated on: 2025-09-09 17:15:52
Accuracy: 50.10%
"""


# PREDICTOR 15 - Accuracy: 50.10%
# Correct predictions: 5010/10000 (50.10%)

def predict_output(A, B, C, D, E):
    if E > 70 and C < 25:
        return 4
    if B > 60 and C < 25 and E > 40 and A > 10:
        return 4
    if E < 10 and B > 60:
        return 4
    if B > 70 and E > 60 and C < 50 and D < 60:
        return 4
    if B < 25 and C < 25:
        if E < 50:
            if A < 40:
                return 1
            else:
                return 3
        else:
            return 1
    if B > 50 and C > 75 and A < 60:
        return 2
    if C > 75 and A < 70:
        return 2
    if B > 80 and E > 70 and C < 70:
        if D > 80:
            return 3
        else:
            return 2
    if B > 40 and C < 15 and D > 60:
        return 3
    if B > 50 and C < 25 and E < 30 and D < 25:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    return 1