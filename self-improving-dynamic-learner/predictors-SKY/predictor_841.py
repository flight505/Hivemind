"""
Predictor 841
Generated on: 2025-09-09 21:24:20
Accuracy: 55.17%
"""


# PREDICTOR 841 - Accuracy: 55.17%
# Correct predictions: 5517/10000 (55.17%)

def predict_output(A, B, C, D, E):
    if D < 10 and E > 80:
        return 1
    if B < 20 and C < 15:
        if E > 50:
            return 4
        else:
            return 3
    if B < 20 and C > 80:
        return 3
    if B < 20 and 20 < C < 60:
        return 3
    if C < 20 and D > 80:
        if B < 35:
            return 1
        else:
            return 4
    if B < 15 and C < 30 and E > 70:
        if D > 70:
            return 1
        else:
            return 4
    if C < 10 and B > 40 and E < 40:
        return 3
    if B > 60 and C >= 70:
        if C > 90 or A > 50:
            return 1
        elif D < 20 and E < 10:
            return 1
        elif D < 20:
            return 4
        else:
            return 2
    if E > 90 and C < 30:
        return 4
    if C < 5 and B > 20:
        if D > 50:
            return 4
        else:
            return 3
    if C < 10 and B > 20 and D < 50 and E > 70:
        return 4
    if B > 80 and E > 90:
        return 4
    if B > 70 and C < 60 and E > 70:
        return 4
    return 1