"""
Predictor 213
Generated on: 2025-09-09 14:17:08
Accuracy: 59.25%
"""


# PREDICTOR 213 - Accuracy: 59.25%
# Correct predictions: 5925/10000 (59.25%)

def predict_output(A, B, C, D, E):
    if B + C < 15 and E > 85:
        return 4
    if A > 85 and B < 15 and C < 10 and D > 85:
        return 4
    if B > 45 and C < 30 and E < 10:
        return 1
    if B < 40 and C > 55 and E < 45 and D < 20:
        return 3
    if B < 10 and C < 50 and E > 55:
        return 4
    if B > 40 and C < 10 and E < 45:
        return 3
    if A > 65 and B > 35 and C < 45 and E < 35 and D > 35:
        return 1
    if A > 70 and B < 40 and C > 55 and E < 45:
        return 1
    if B > 55 and C < 30 and E < 35 and D > 75:
        return 1
    if B < 40 and C > 55 and E < 45 and D < 15 and A > 65:
        return 1
    if B > 75 and C > 55 and E > 75:
        return 1
    if B > 85 and C > 55 and 15 <= E < 55:
        return 1
    if C > 80 and B > 55:
        return 1
    if B > 65 and C > 60 and E > 85:
        return 1
    if A > 85 and B > 55 and C < 45 and E < 35:
        return 1
    if A < 15 and B > 85 and C > 65:
        return 1
    if B > 65 and C < 30 and E < 35:
        return 1
    if A > 85 and C > 85:
        return 1
    if B > 85 and C < 25 and E > 35 and A < 30:
        return 1
    if A > 10 and B < 15 and C < 25 and D > 55:
        return 1
    if A > 75 and B < 50 and C < 45 and E < 25:
        return 1
    if B > 70 and C > 75 and E < 30 and D < 15:
        return 1
    if C > 75 and E > 75 and B < 35 and A < 55:
        return 2
    if A < 30 and B > 40 and C < 35 and E > 55:
        return 2
    if C > 90 and E > 80:
        return 2
    if A < 20 and B < 20 and C > 90:
        return 2
    if B < 30 and C > 55 and E < 15:
        return 4
    if B > 85 and C < 20 and E > 35:
        return 4
    if C < 35 and E > 65 and B > 15 and D < 55:
        return 4
    if C < 25 and E >= 45 and A > 15:
        return 4
    if B > 75 and E > 75 and C < 35:
        return 4
    if B > 75 and E > 75 and C < 55:
        return 4
    if B < 25 and C > 65 and E < 40 and D < 35:
        return 4
    if B < 40 and C > 55 and E < 45 and D < 55:
        return 4
    if E > 85 and B < 65 and C < 45:
        return 4
    if C < 30 and D > 85 and E < 25:
        return 4
    if B > 65 and C < 30 and E < 20:
        return 4
    if E > 85 and B > 55 and C < 45:
        return 4
    if B < 15 and E < 15:
        return 4
    if C < 10 and D > 75 and B > 45:
        return 4
    if B > 65 and C < 50 and E < 35 and D > 65:
        return 3
    if B < 45 and C < 45 and E > 85:
        return 3
    if B < 35 and C < 30 and E < 45:
        return 3
    if B > 55 and C < 30 and E < 25 and D < 55:
        return 3
    if B > 35 and C < 35 and E < 35 and B < 85 and A < 85:
        return 3
    if B < 30 and C < 30 and E < 45:
        return 3
    if B < 45 and C > 65 and E < 55 and D < 55:
        return 3
    if 35 < B < 55 and 30 < C < 50 and 30 < E < 50:
        return 3
    if E < 20 and B > 35 and 25 < C < 55:
        return 3
    if B > 65 and C > 65 and D > 85 and E > 75:
        return 3
    if B > 25 and C < 15 and E < 25:
        return 3
    if B < 55 and C < 55 and E < 35 and D < 65:
        return 3
    if 50 < B < 70 and 30 < C < 50 and E < 25 and D > 65:
        return 3
    if A < 55 and B >= 55 and C > 55 and E < 65:
        return 2
    if A < 45 and B > 55 and C > 65 and 60 < E < 85:
        return 2
    if A < 55 and B > 55 and C > 55 and E < 25:
        return 2
    if B > 85 and 25 < C < 55:
        return 2
    if A + B > 155 and C < 45 and E > 45:
        return 2
    return 1