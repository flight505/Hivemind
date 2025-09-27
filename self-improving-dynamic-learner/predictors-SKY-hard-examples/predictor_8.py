"""
Predictor 8
Generated on: 2025-09-09 17:09:43
Accuracy: 44.82%
"""


# PREDICTOR 8 - Accuracy: 44.82%
# Correct predictions: 4482/10000 (44.82%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if C >= 75:
        if B > 60:
            return 2
        else:
            return 1
    if B < 20:
        if C < 25:
            return 3
        elif D < 20:
            return 3
        elif A > 70:
            return 4
        elif C > 70:
            return 4
        else:
            return 1
    if C < 40:
        if B > 70 and D > 70 and E > 70:
            return 2
        elif B > 70 and E > 50:
            return 4
        elif A > 70 and B > 70:
            return 4
        elif D > 50 or B > 40:
            return 1
        else:
            return 3
    else:
        if B > 50 and D > 65:
            return 3
        elif B > 70:
            return 2
        elif D < 30 and E < 50:
            return 4
        else:
            return 1