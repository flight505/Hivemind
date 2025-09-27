"""
Predictor 512
Generated on: 2025-09-09 17:30:49
Accuracy: 58.56%
"""


# PREDICTOR 512 - Accuracy: 58.56%
# Correct predictions: 5856/10000 (58.56%)

def predict_output(A, B, C, D, E):
    if B > 80 and C > 60 and E < 60:
        return 1
    if D > 80 and B < 30 and C < 20:
        return 1
    if B > 90 and 30 <= C < 50 and E < 30:
        return 1
    if B > 70 and C > 60 and E > 80:
        return 1
    if A > 80 and B > 70 and C < 50 and E < 50:
        return 1
    if E > 90 and C > 50 and B < 60:
        return 1
    if C > 90 and E > 90 and B < 70:
        return 1
    if C > 80 and B < 30 and E > 70:
        return 1
    if B > 80 and E > 80 and C < 30:
        return 4
    if C < 30 and E > 70 and B > 10 and D < 50:
        return 4
    if E > 90 and B > 60 and C < 40:
        return 4
    if B > 90 and C < 15 and E > 40:
        return 4
    if B < 20 and C > 70 and E < 35 and D < 60:
        return 4
    if E > 90 and B < 60 and C < 30:
        return 4
    if B > 70 and C < 25 and E < 15:
        return 4
    if C < 30 and E < 40 and D > 60:
        return 4
    if E < 5 and D > 70:
        return 4
    if E > 90 and B > 70 and C > 50:
        return 4
    if A < 50 and B > 60 and C > 60 and E < 70:
        return 2
    if B > 90 and 30 < C < 50:
        return 2
    if C > 95 and E > 85:
        return 2
    if A + B > 160 and C < 40 and E > 50:
        return 2
    if B > 80 and 30 < C < 50:
        return 2
    if B > 70 and C < 45 and E < 30 and D > 70:
        return 3
    if B < 20 and C < 10 and D > 60:
        return 3
    if B < 30 and C < 25 and E < 40:
        return 3
    if B > 60 and C < 25 and E < 20:
        return 3
    if B + C < 30 and D > 80:
        return 3
    if C < 10 and D > 80:
        return 3
    if B > 80 and C > 80 and E < 10:
        return 3
    if E > 90 and B < 60 and C > 30:
        return 3
    return 1