"""
Predictor 819
Generated on: 2025-09-09 21:12:13
Accuracy: 46.63%
"""


# PREDICTOR 819 - Accuracy: 46.63%
# Correct predictions: 4663/10000 (46.63%)

def predict_output(A, B, C, D, E):
    if B > 80 and C >= 70 and D < 20 and E > 70:
        return 1
    if E > 90:
        if B > 80 and C < 30:
            return 2
        if D > 80:
            return 3
        return 4
    if C < 25 and E > 50 and B < 60:
        return 4
    if B < 10 and E > 70:
        return 4
    if C < 10 and B < 20 and E > 50:
        return 4
    if B > 60 and D < 30 and E < 40:
        return 4
    if B < 40 and C > 60 and D > 40 and E < 40:
        return 4
    if B < 20 and C > 60 and E < 20 and D > 50:
        return 4
    if D > 90 and B > 60 and E > 70:
        return 3
    if D > 90 and E < 20 and C > 50:
        return 3
    if C > 90 and E < 20:
        return 3
    if C > 80 and B < 40 and E < 30:
        return 3
    if B > 60 and C > 70 and D < 10 and E < 50:
        return 3
    if B < 25 and C < 35 and D > 80:
        return 3
    if B < 20 and C < 20:
        return 3
    if B < 40 and C < 45 and E < 40 and D < 50:
        return 3
    if B > 60 and C > 70:
        return 2
    if B > 80 and C < 25 and D < 50:
        return 2
    if B > 80 and E < 20:
        return 2
    return 1