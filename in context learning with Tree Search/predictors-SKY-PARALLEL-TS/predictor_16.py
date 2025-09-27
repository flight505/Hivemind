"""
Predictor 16
Generated on: 2025-09-09 23:19:12
Accuracy: 47.85%
"""


# PREDICTOR 16 - Accuracy: 47.85%
# Correct predictions: 4785/10000 (47.85%)

def predict_output(A, B, C, D, E):
    if (A <= 60 and B > 70) or (C < 10 and D >= 80) or (B < 10 and A > 80) or (D < 20 and E > 90):
        return 4
    elif A > 75 and E < 45 and D > 50:
        return 2
    elif D > 80 and C < 40:
        return 3
    else:
        return 1