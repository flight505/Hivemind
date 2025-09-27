"""
Predictor 530
Generated on: 2025-09-09 17:43:43
Accuracy: 57.53%
"""


# PREDICTOR 530 - Accuracy: 57.53%
# Correct predictions: 5753/10000 (57.53%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B < 50 and E >= 70 and C < 30:
        return 4
    if B < 20 and E >= 70 and C < 50 and D < 20:
        return 4
    if B < 65 and C > 35 and E < 60 and D < 60:
        return 4
    if A > 50 and B > 60 and C > 60:
        return 1
    if A < 50 and B > 60 and C > 60 and (B + E) > 100:
        return 2
    if B > 60 and C > 70 and E > 50:
        return 2
    return 1