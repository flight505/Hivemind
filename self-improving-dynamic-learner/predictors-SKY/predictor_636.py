"""
Predictor 636
Generated on: 2025-09-09 19:00:43
Accuracy: 43.33%
"""


# PREDICTOR 636 - Accuracy: 43.33%
# Correct predictions: 4333/10000 (43.33%)

def predict_output(A, B, C, D, E):
    if E > 90:
        if B > 50:
            return 1
        else:
            return 4
    if C > 80:
        if E < 30:
            if B < 50:
                return 4
            else:
                return 1
        else:
            return 2
    if B > 60 and C > 70 and E > 50:
        return 2
    if C < 40 and B > 70:
        if D > 40:
            return 4
        else:
            return 3
    if B < 30 and C > 60 and D < 50:
        return 3
    if B + C < 30:
        return 3
    return 1