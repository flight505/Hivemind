"""
Predictor 284
Generated on: 2025-09-09 15:02:29
Accuracy: 55.93%
"""


# PREDICTOR 284 - Accuracy: 55.93%
# Correct predictions: 5593/10000 (55.93%)

def predict_output(A, B, C, D, E):
    if B > 80 and C < 30 and E > 60:
        return 4
    if E > 90 and C < 40 and B < 50:
        return 4
    if B < 30 and C < 40 and E > 80:
        return 4
    if B < 30 and C > 60 and E < 40:
        if D > 80:
            return 1
        else:
            return 3
    if B > 60 and C < 25 and E < 20 and D < 50:
        return 3
    if D > 90 and E < 30:
        return 3
    if B > 90 and C > 90:
        return 2
    if A < 50 and B > 60 and C > 60 and E < 70:
        return 2
    if B > 90 and 30 < C < 50:
        return 2
    if A + B > 160 and C < 40 and E > 50:
        return 2
    if B > 70 and C > 80 and E < 50:
        return 1
    if B > 70 and C < 25 and E < 30:
        return 1
    if A > 70 and B > 40 and C < 40 and E < 30:
        return 1
    return 1