"""
Predictor 71
Generated on: 2025-09-09 23:24:50
Accuracy: 55.72%
"""


# PREDICTOR 71 - Accuracy: 55.72%
# Correct predictions: 5572/10000 (55.72%)

def predict_output(A, B, C, D, E):
    if A < 5 and B > 90 and C < 5:
        return 2
    if A > 90 and E < 10 and B > 80:
        return 2
    if A < 10 and B > 70:
        return 4
    if C < 10 and D > 90:
        return 4
    if A < 25 and B > 70 and D > 80:
        return 4
    if E > 80 and B < 30 and C < 50 and D < 40:
        return 4
    if B > 70 and D < 20 and A < 50:
        return 3
    if D > 65 and C < 15 and B < 20:
        return 3
    if A > 50 and C < 50 and D > 70 and B > 40:
        return 3
    if D < 15 and C > 40 and B < 80:
        return 3
    if C < 10 and E < 60:
        return 3
    else:
        return 1