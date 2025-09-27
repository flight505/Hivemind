"""
Predictor 111
Generated on: 2025-09-09 13:16:29
Accuracy: 51.18%
"""


# PREDICTOR 111 - Accuracy: 51.18%
# Correct predictions: 5118/10000 (51.18%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 90:
        return 4
    if B < 25 and C > 60 and E < 40:
        return 4
    if C > 90 and E < 5:
        return 4
    if B > 65 and C < 30 and E > 60:
        return 4
    if B < 20 and C < 15:
        return 3
    if C < 15 and B < 35:
        return 3
    if C > 50 and E < 30 and D > 70:
        return 3
    if 40 < C < 50 and B > 55 and D < 20:
        return 3
    if B < 50 and C > 40 and D > 80:
        return 3
    if A > 90 and B > 70 and C > 35 and D > 90:
        return 3
    if 20 < A < 40 and B > 60 and C > 70:
        return 2
    if E > 80 and B > 60 and C > 40:
        return 2
    if B > 70 and 45 < C < 55 and E < 30:
        return 2
    return 1