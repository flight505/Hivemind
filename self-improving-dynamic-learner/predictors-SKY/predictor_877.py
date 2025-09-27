"""
Predictor 877
Generated on: 2025-09-09 21:40:48
Accuracy: 45.33%
"""


# PREDICTOR 877 - Accuracy: 45.33%
# Correct predictions: 4533/10000 (45.33%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if C > 50 and B < 50:
        return 4
    if B > 85 and C > 65 and E < 20:
        return 2
    if B < 10 and C > 80:
        return 1
    if B > 60 and C > 40 and E > 80 and D < 25:
        return 4
    if B > 50 and C > 80 and D > 90 and E < 50:
        return 3
    if B > 90 and C > 90:
        return 2
    if C > 90 and E > 90 and B < 30:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if B + C < 10 and E > 90:
        return 4
    if B < 40 and C > 50 and E < 50 and D < 20:
        return 3
    if B < 5 and C < 45 and E > 60:
        return 4
    if B > 45 and C < 5 and E < 40:
        return 3
    if A > 70 and B > 40 and C < 40 and E < 30 and D > 40:
        return 1
    if B > 80 and C > 60 and E > 80 and D < 50:
        return 4
    if B > 90 and 30 <= C < 50 and E > 50:
        return 2
    if B < 25 and C > 60 and E < 10:
        return 4
    if C < 30 and E > 70 and B > 10 and D < 50:
        return 4
    if E > 90 and B < 60 and C < 30:
        return 4
    if B > 70 and C < 45 and E < 30 and D > 70:
        return 3
    if B < 20 and C < 10 and D > 60 and E < 45:
        return 3
    if B < 40 and C < 40 and E > 90:
        return 3
    if A < 50 and B >= 60 and C > 60 and E < 70 and D > 20:
        return 2
    if B > 90 and 30 < C < 50:
        return 2
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if C > 80 and B > 80 and E < 60:
        return 1
    if D > 80 and B < 30 and C < 20:
        return 1
    return 1