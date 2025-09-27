"""
Predictor 4
Generated on: 2025-09-09 12:04:30
Accuracy: 55.56%
"""


# PREDICTOR 4 - Accuracy: 55.56%
# Correct predictions: 5556/10000 (55.56%)

def predict_output(A, B, C, D, E):
    if (B < 20 and C > 70 and E < 50) or (C < 32 and E > 60) or (B > 80 and E > 80):
        return 4
    if B <= 20 and C <= 70 and E < 50:
        return 3
    if C < 35 and E > 80 and A > 80:
        return 3
    if C > 60 and E < 50 and A < 60:
        return 3
    if B >= 40 and C > 65 and A < 50 and E > 65:
        return 2
    return 1