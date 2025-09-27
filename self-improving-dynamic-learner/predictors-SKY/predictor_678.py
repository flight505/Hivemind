"""
Predictor 678
Generated on: 2025-09-09 19:29:08
Accuracy: 54.88%
"""


# PREDICTOR 678 - Accuracy: 54.88%
# Correct predictions: 5488/10000 (54.88%)

def predict_output(A, B, C, D, E):
    if B < 30 and C < 30:
        if D > 80 and E < 20:
            return 1
        elif E > 50:
            return 4
        else:
            return 3
    if B > 70 and C < 25:
        return 1
    if C > 80 and E < 30 and B < 60:
        return 4
    if B > 80 and C > 60 and D > 90:
        return 3
    if D > 90 and E < 20 and A > 50:
        return 3
    if C > 80 and B > 60 and E < 50:
        return 1
    if A < 50 and B > 60 and C > 60 and E < 70:
        return 2
    if B > 90 and C < 40 and E < 40:
        return 1
    if B < 20 and C > 60 and E < 30:
        return 4
    if C > 95 and E > 85:
        return 2
    if B > 80 and C < 30 and E > 60:
        return 4
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60:
        return 1
    if B > 60 and C > 40 and E > 80 and D < 25:
        return 4
    if B < 30 and C > 70 and E > 70:
        return 2
    if B > 75 and C > 75:
        return 2
    if B > 50 and C < 15:
        return 3
    if B > 80 and C < 30 and D > 80:
        return 3
    if C < 25 and D > 90 and E < 20:
        return 4
    if B < 20 and C > 70 and E < 50:
        return 1
    return 1