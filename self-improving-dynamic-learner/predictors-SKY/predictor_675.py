"""
Predictor 675
Generated on: 2025-09-09 19:27:19
Accuracy: 50.27%
"""


# PREDICTOR 675 - Accuracy: 50.27%
# Correct predictions: 5027/10000 (50.27%)

def predict_output(A, B, C, D, E):
    if B < 30 and C < 30:
        if D > 80 and E < 20:
            return 1
        elif E > 50:
            return 4
        else:
            return 3
    if D < 20 and E > 50 and B < 60:
        return 4
    if B > 70 and C > 90 and D > 70:
        return 3
    if B > 60 and C > 50 and A < 50:
        return 2
    if B > 85 and E < 40:
        return 2
    if C > 60 and B < 25:
        return 4
    if C > 80:
        if B > 40 and E > 80:
            return 2
        else:
            return 1
    if E > 90:
        return 4
    if D < 15 and E > 70 and B > 80:
        return 1
    if B > 80 and C < 30 and E > 60:
        return 4
    if C > 85 and B > 60:
        return 1
    if B > 60 and C > 40 and E > 80 and D < 25:
        return 4
    return 1