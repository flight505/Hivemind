"""
Predictor 288
Generated on: 2025-09-09 15:04:22
Accuracy: 45.55%
"""


# PREDICTOR 288 - Accuracy: 45.55%
# Correct predictions: 4555/10000 (45.55%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if A < 10 and B > 60 and C > 70:
        return 3
    if B < 20 and C > 30 and D > 50:
        return 3
    if B > 50 and B < 80 and C < 30 and D > 70:
        return 3
    if B > 80 and C < 15:
        return 4
    if C < 30 and E > 90:
        return 4
    if B < 10 and E < 10:
        return 4
    if B > 90 and 30 < C < 70:
        return 2
    if B < 30 and C < 40 and E > 60:
        return 2
    if B > 60 and C > 70:
        return 2
    return 1