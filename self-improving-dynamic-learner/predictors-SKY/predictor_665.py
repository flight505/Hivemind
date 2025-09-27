"""
Predictor 665
Generated on: 2025-09-09 19:20:02
Accuracy: 44.36%
"""


# PREDICTOR 665 - Accuracy: 44.36%
# Correct predictions: 4436/10000 (44.36%)

def predict_output(A, B, C, D, E):
    if C > 90 and E < 25 and B < 50:
        return 3
    if C > 90 and E < 25 and B >= 50:
        return 4
    if B > 60 and C > 50 and E < 30:
        return 4
    if B < 20 and C > 80:
        return 1
    if B < 10 and E > 70:
        return 3
    if B > 70 and E < 30:
        return 2
    if B < 10 and C < 10 and E > 40:
        return 4
    if D > 90 and B < 60:
        return 3
    if B < 35 and C < 10 and E < 10:
        return 3
    if E > 90:
        if B > 70:
            return 3
        return 4
    if B < 20 and C < 20 and E < 40:
        return 3
    if B > 60 and C > 75 and E > 65:
        return 2
    if B > 80 and C < 30 and E > 60:
        return 4
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if B > 70 and C < 20:
        return 1
    return 1