"""
Predictor 13
Generated on: 2025-09-09 12:13:02
Accuracy: 51.85%
"""


# PREDICTOR 13 - Accuracy: 51.85%
# Correct predictions: 5185/10000 (51.85%)

def predict_output(A, B, C, D, E):
    if C < 25 and E > 70 and D < 60:
        return 4
    if B > 70 and C < 45 and E > 70:
        return 4
    if B < 20 and C < 30 and E < 20 and D > 50:
        return 4
    if B < 20 and C < 20:
        return 3
    if 40 < B < 55 and 35 < C < 50 and 35 < E < 50:
        return 3
    if B > 50 and C < 15:
        return 3
    if A > 70 and E > 80 and C > 35:
        return 3
    if C > 80 and B < 20 and E < 25:
        return 3
    if A < 60 and C > 70 and E > 60:
        return 2
    return 1