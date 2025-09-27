"""
Predictor 1462
Generated on: 2025-09-10 02:31:46
Accuracy: 55.19%
"""


# PREDICTOR 1462 - Accuracy: 55.19%
# Correct predictions: 5519/10000 (55.19%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 80) or (C < 10 and D < 10 and E > 50) or (B > 90 and C < 20 and D > 80) or (A > 50 and B > 90 and C < 20 and D > 80 and E < 20):
        return 4
    elif B > 80 and E < 25 and D > 70 and C > 30:
        return 2
    elif A > 50 and C < 20 and D < 25 and B > 30:
        return 3
    else:
        return 1