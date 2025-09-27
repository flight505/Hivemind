"""
Predictor 282
Generated on: 2025-09-09 15:01:46
Accuracy: 47.15%
"""


# PREDICTOR 282 - Accuracy: 47.15%
# Correct predictions: 4715/10000 (47.15%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if B < 20 and C < 20:
        return 3
    if C > 60 and B < 30 and A < 50:
        return 4
    if D > 80 and C < 20 and E > 30:
        return 4
    if C < 15 and E > 80:
        return 4
    if B >= 60 and C < 25 and E < 40:
        return 3
    if D > 90 and B < 40 and C > 30:
        return 3
    if B > 60 and C > 75 and E > 20:
        return 2
    if B > 90 and C > 50 and E < 30:
        return 2
    if B > 70 and E > 60 and C < 40:
        return 2
    return 1