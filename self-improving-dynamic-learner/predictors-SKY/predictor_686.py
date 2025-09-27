"""
Predictor 686
Generated on: 2025-09-09 19:36:30
Accuracy: 59.02%
"""


# PREDICTOR 686 - Accuracy: 59.02%
# Correct predictions: 5902/10000 (59.02%)

def predict_output(A, B, C, D, E):
    if C > 90 and D > 80:
        return 1
    if B > 90 and C > 70 and E < 30:
        return 1
    if B < 5 and C > 70:
        return 4
    if B < 10 and C < 10 and D > 75 and E > 90:
        return 4
    if B > 50 and C < 5 and E < 20:
        return 3
    if B < 10 and D < 5:
        return 3
    if D < 10 and E < 25:
        return 3
    if C < 25 and D > 95:
        return 3
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if B > 80 and C < 30 and E > 60:
        return 4
    if B > 60 and C > 40 and E > 80 and D < 25:
        return 4
    if B > 70 and C > 60 and E > 80:
        return 1
    if B > 90 and 30 <= C < 50 and E > 50:
        return 2
    if A > 80 and B > 70 and C < 50 and E < 50:
        return 1
    if B > 90 and C < 20 and E > 40:
        return 4
    if C < 25 and E > 75:
        return 4
    if B > 65 and C < 30 and A > 50:
        return 4
    if C >= 85 and E < 20 and B < 50:
        return 4
    if C > 80 and D < 20 and B < 40:
        return 4
    if B < 20 and C < 20:
        return 3
    if 55 < B < 65 and D > 70:
        return 3
    if A < 10 and D < 10 and B > 40:
        return 3
    if A < 50 and B > 60 and B + C > 120:
        return 2
    return 1