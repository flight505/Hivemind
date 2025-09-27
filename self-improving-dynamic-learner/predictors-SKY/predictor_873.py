"""
Predictor 873
Generated on: 2025-09-09 21:39:33
Accuracy: 45.85%
"""


# PREDICTOR 873 - Accuracy: 45.85%
# Correct predictions: 4585/10000 (45.85%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B < 30 and C > 60:
        if E < 20:
            return 3
        else:
            return 4
    if B < 10 and C > 50:
        return 3
    if C < 15 and E > 50:
        return 4
    if B < 15 and E > 50:
        return 2
    if A > 90 and B > 70 and C < 40:
        return 4
    if B < 5 and C > 50:
        return 4
    if C > 90 and B > 90 and E > 90:
        return 1
    if B > 50 and E < 5 and D < 25:
        return 3
    if B > 70 and C < 45 and D > 90:
        return 3
    if B > 60 and C < 30:
        return 4
    if E > 90:
        return 4
    if B < 40 and C > 80:
        return 4
    if B > 70 and 40 < C < 50:
        return 2
    if B > 90 and C > 80:
        return 2
    if A < 40 and B > 60 and C > 70 and E > 70:
        return 2
    return 1