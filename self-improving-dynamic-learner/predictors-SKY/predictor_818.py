"""
Predictor 818
Generated on: 2025-09-09 21:11:27
Accuracy: 48.89%
"""


# PREDICTOR 818 - Accuracy: 48.89%
# Correct predictions: 4889/10000 (48.89%)

def predict_output(A, B, C, D, E):
    if E > 90:
        if D > 80 and B < 40:
            return 3
        return 4
    if C < 20 and E > 70:
        return 4
    if B < 10 and E > 70:
        return 4
    if C < 10 and B < 20 and E > 50:
        return 4
    if B > 60 and D < 30 and E < 40:
        return 4
    if B > 60 and C > 70 and D < 10 and E < 50:
        return 3
    if B > 80 and C < 25 and D < 50:
        return 2
    if B > 80 and E < 20:
        return 2
    if B > 60 and C > 70:
        return 2
    if B < 20 and C < 20:
        return 3
    if B < 40 and C < 45 and E < 40 and D < 50:
        return 3
    if B < 25 and C < 35 and D > 80:
        return 3
    return 1