"""
Predictor 788
Generated on: 2025-09-09 20:50:33
Accuracy: 46.91%
"""


# PREDICTOR 788 - Accuracy: 46.91%
# Correct predictions: 4691/10000 (46.91%)

def predict_output(A, B, C, D, E):
    if B < 25 and C < 25:
        if D < 20 or E < 20:
            return 1
        else:
            return 3
    if C < 25 and D > 60:
        if E < 40:
            return 1
        else:
            return 4
    if C > 80 and B < 40:
        return 3
    if C > 55 and E < 30 and B > 50:
        return 4
    if B > 60 and C > 60:
        if D < 20:
            return 1
        elif D > 80 and E > 60:
            return 3
        elif A < 50:
            return 2
        else:
            return 1
    if B > 60 and D > 70 and E > 50 and C < 50:
        return 3
    if E > 90 and C > 50:
        return 1
    if B > 80 and C < 30 and E > 60:
        return 4
    if B < 20 and E > 70:
        return 3
    if B < 30 and C > 50 and E < 30:
        return 3
    if B > 70 and C > 85 and E < 40:
        return 2
    return 1