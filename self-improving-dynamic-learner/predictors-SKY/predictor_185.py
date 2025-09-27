"""
Predictor 185
Generated on: 2025-09-09 13:59:56
Accuracy: 52.66%
"""


# PREDICTOR 185 - Accuracy: 52.66%
# Correct predictions: 5266/10000 (52.66%)

def predict_output(A, B, C, D, E):
    if B > 80 and C > 60 and E > 80:
        return 1
    if B > 90 and C > 60 and 20 <= E < 50:
        return 1
    if C > 85 and B > 60:
        return 1
    if B > 70 and C > 65 and E > 90:
        return 1
    if A > 90 and B > 60 and C < 40 and E < 30:
        return 1
    if A < 10 and B > 90 and C > 70:
        return 1
    if B > 70 and C < 25 and E < 30:
        return 1
    if B < 30 and C > 65 and E < 25 and A > 70:
        return 1
    if B > 70 and C < 20 and E > 65 and A > 65:
        return 1
    if B > 60 and C < 25 and E > 70 and A > 65:
        return 1
    if B > 90 and A > 90 and C > 40:
        return 1
    if B > 75 and C > 40 and E < 30:
        return 1
    if D > 90 and E < 30 and B < 30 and C < 30 and A < 20:
        return 1
    if A > 90 and B < 10 and C < 20:
        return 1
    if B > 95 and C > 80 and E > 70 and D > 80:
        return 2
    if A < 10 and B > 90 and E > 90:
        return 2
    if A + B > 170 and E < 30:
        return 2
    if A < 15 and B > 40 and C > 60 and E > 45:
        return 2
    if A + B < 60 and C > 60:
        return 2
    if B > 90 and 30 < C < 50:
        return 2
    if B < 20 and C < 25 and E < 20:
        return 4
    if B < 20 and C > 50 and E < 5:
        return 4
    if B > 80 and C < 10 and E < 10 and A > 90:
        return 4
    if B > 50 and C < 30 and D > 80 and E < 20:
        return 4
    if B < 30 and C > 50 and E < 5:
        return 4
    if B > 80 and C < 30 and E > 70 and A < 60:
        return 2
    if B > 80 and C > 50 and D > 90 and E > 70:
        return 3
    if B > 80 and C > 60 and D > 80 and E < 60:
        return 3
    if C < 10 and E > 70 and B > 60:
        return 4
    if B > 90 and C < 15 and E > 40 and A < 5:
        return 2
    if B > 90 and C < 15 and E > 40:
        return 4
    if B < 25 and C > 60 and E < 10 and D >= 10:
        return 4
    if B < 25 and C > 60 and E < 10:
        return 3
    if B < 50 and C < 50 and E < 30 and D > 70:
        return 4
    if A > 70 and B < 40 and C < 40 and E < 30 and D > 90:
        return 3
    if B < 20 and C > 70 and E < 35 and D < 30:
        return 4
    if B < 35 and C > 60 and E < 40 and D < 50 and A < 70:
        return 4
    if E > 90 and B < 60 and C < 50 and A > 10:
        return 4
    if C < 25 and D > 90 and E < 20:
        return 4
    if B > 70 and C < 25 and E < 15:
        return 4
    if E > 90 and B > 60 and C < 40:
        return 4
    if B < 10 and E < 10:
        return 4
    if B > 90 and C > 90 and E < 15 and A < 5:
        return 3
    if B > 65 and C < 10 and E > 30 and D > 70:
        return 3
    if A < 15 and B > 85 and C < 15 and E > 30:
        return 3
    if B < 40 and C < 40 and E > 90:
        return 3
    if B < 30 and C < 25 and E < 40:
        return 3
    if B > 60 and C < 25 and E < 20 and D < 50:
        return 3
    if B > 40 and C < 30 and E < 30 and B < 90 and A < 90:
        return 3
    if B < 25 and C < 25 and E < 40:
        return 3
    if B < 40 and C > 70 and E < 50 and D < 50:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if E < 15 and B > 40 and 30 < C < 50:
        return 3
    if B > 70 and C > 70 and D > 90 and E > 80:
        return 3
    if B > 30 and C < 10 and E < 20:
        return 3
    if B < 50 and C < 50 and E < 30 and D < 60:
        return 3
    if 55 < B < 65 and 35 < C < 45 and E < 20 and D > 70:
        return 3
    if C < 10 and B < 60:
        return 3
    if A < 50 and B >= 60 and C > 60 and E < 70 and D > 30:
        return 2
    if A < 40 and B > 60 and C > 70 and 65 < E < 80:
        return 2
    if A < 50 and B > 60 and C > 60 and E < 20:
        return 2
    if A + B > 160 and C < 40 and E > 50:
        return 2
    return 1