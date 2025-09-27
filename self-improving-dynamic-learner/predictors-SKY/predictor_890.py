"""
Predictor 890
Generated on: 2025-09-09 21:46:40
Accuracy: 53.35%
"""


# PREDICTOR 890 - Accuracy: 53.35%
# Correct predictions: 5335/10000 (53.35%)

def predict_output(A, B, C, D, E):
    if B < 20 and E > 70:
        return 4
    if B + E < 70 and C > 50:
        return 4
    if E > 90 and C < 40:
        return 4
    if B > 80 and C < 30:
        return 4
    if D > 90 and B > 80 and C >= 10:
        return 3
    if D > 90 and C < 10:
        return 3
    if B < 40 and C > 50 and E < 50 and D < 20:
        return 3
    if B < 25 and E < 15:
        return 3
    if B < 10 and C < 10:
        return 3
    if A < 50 and B > 60 and C > 70:
        return 2
    if A < 50 and B > 60 and C < 50 and E > 50 and D < 30:
        return 2
    if B > 90 and 30 <= C < 50:
        return 2
    if D > 80 and C < 20:
        return 3
    if B < 30 and C < 25 and E < 40:
        return 3
    return 1