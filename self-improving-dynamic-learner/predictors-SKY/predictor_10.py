"""
Predictor 10
Generated on: 2025-09-09 12:10:43
Accuracy: 48.02%
"""


# PREDICTOR 10 - Accuracy: 48.02%
# Correct predictions: 4802/10000 (48.02%)

def predict_output(A, B, C, D, E):
    if C < 35 and E > 70:
        if B < 50:
            if D > 80:
                return 3
            else:
                return 4
        else:
            return 4
    if E < 10 and C > 25 and D > 60:
        return 4
    if C < 30 and B > 90:
        return 4
    if B > 60 and C > 85 and E > 90:
        return 3
    if B < 20:
        return 3
    if B > 60 and C > 60 and E > 50:
        return 2
    return 1