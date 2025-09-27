"""
Predictor 850
Generated on: 2025-09-09 21:27:38
Accuracy: 50.58%
"""


# PREDICTOR 850 - Accuracy: 50.58%
# Correct predictions: 5058/10000 (50.58%)

def predict_output(A, B, C, D, E):
    if B < 30 and C < 30:
        if D > 90 and E < 20:
            return 1
        else:
            return 3
    if B < 30 and C > 30:
        if C > 90 or E > 50:
            return 1
        elif D > 70:
            return 1
        else:
            return 3
    if B > 50 and C > 75:
        if E < 20:
            return 4
        else:
            return 2
    if B > 60 and C < 30:
        if D < 50:
            return 1
        elif E > 80:
            return 4
        elif E > 50:
            return 1
        else:
            return 4
    if C < 30 and E > 90:
        if D > 80:
            return 3
        else:
            return 4
    return 1