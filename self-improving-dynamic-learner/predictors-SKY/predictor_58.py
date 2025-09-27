"""
Predictor 58
Generated on: 2025-09-09 12:42:29
Accuracy: 43.12%
"""


# PREDICTOR 58 - Accuracy: 43.12%
# Correct predictions: 4312/10000 (43.12%)

def predict_output(A, B, C, D, E):
    # Conditions for 4
    if C > 60 and E > 80:
        return 4
    if C > 60 and E < 10:
        return 4
    if C < 25 and E > 90:
        return 4
    if B > 80 and E > 80 and C < 30:
        return 4
    if C < 30 and E > 70 and B < 40:
        return 4
    if E < 10 and B < 40 and C < 50 and D < 80:
        return 4
    if B < 20 and C > 70 and E < 35 and D < 30:
        return 4
    # Conditions for 3
    if B < 20 and C < 25 and E > 10:
        return 3
    if 40 < B < 60 and C > 60 and E < 40:
        return 3
    if B > 60 and C < 25 and E < 20 and D < 50:
        return 3
    if B > 40 and C < 30 and E < 30:
        return 3
    if B < 25 and C < 25 and E < 40:
        return 3
    if B < 40 and C > 70 and E < 50 and D < 50:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if E < 15 and B > 40 and 30 < C < 50:
        return 3
    # Conditions for 2
    if B > 60 and C > 75:
        return 2
    if B > 80 and E > 70 and C < 50:
        return 2
    if E > 70 and B < 30:
        return 2
    if A < 50 and B > 60 and C > 60 and E < 20:
        return 2
    if B > 90 and 30 < C < 50:
        return 2
    if A + B > 160 and C < 40:
        return 2
    if A < 40 and B > 60 and C > 70 and 65 < E < 80:
        return 2
    return 1