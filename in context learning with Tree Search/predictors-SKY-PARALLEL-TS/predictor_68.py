"""
Predictor 68
Generated on: 2025-09-09 23:24:50
Accuracy: 55.21%
"""


# PREDICTOR 68 - Accuracy: 55.21%
# Correct predictions: 5521/10000 (55.21%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 85 and C < 10:
        return 2
    if A < 10 and B > 70:
        return 4
    if C < 25 and D > 80 and (B > 30 or A < 70):
        return 4
    if E > 80 and D < 35:
        return 4
    if B > 85 and C > 80:
        return 2
    if B > 70 and D < 20 and A < 80:
        return 3
    if B < 20 and C < 20 and D > 60 and A < 50:
        return 3
    if A > 50 and C < 50 and D > 70 and B > 40:
        return 3
    if D < 15 and C > 40 and B < 80:
        return 3
    if C < 10 and E < 60:
        return 3
    else:
        return 1