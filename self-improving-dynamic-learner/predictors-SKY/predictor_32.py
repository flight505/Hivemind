"""
Predictor 32
Generated on: 2025-09-09 12:24:38
Accuracy: 56.12%
"""


# PREDICTOR 32 - Accuracy: 56.12%
# Correct predictions: 5612/10000 (56.12%)

def predict_output(A, B, C, D, E):
    if C < 35 and E > 75:
        return 4
    if C > 70 and E < 25:
        return 4
    if B > 80 and E > 80 and C < 45:
        return 4
    if B < 20 and C > 70 and E < 35 and D < 30:
        return 4
    if C < 20 and E >= 50:
        return 4
    if B > 60 and C < 25 and E < 20:
        return 3
    if B > 40 and C < 30:
        return 3
    if B < 25 and C < 25 and E < 40:
        return 3
    if B < 40 and C > 70 and E < 50 and D < 50:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if A < 40 and B > 60 and C > 70 and 65 < E < 80:
        return 2
    if A < 50 and B > 60 and C > 60 and E < 20:
        return 2
    if B > 90 and C < 50:
        return 2
    if A + B > 160 and C < 40 and E < 45:
        return 2
    if B > 80 and 45 < C < 60:
        return 2
    return 1