"""
Predictor 1458
Generated on: 2025-09-10 02:31:46
Accuracy: 42.98%
"""


# PREDICTOR 1458 - Accuracy: 42.98%
# Correct predictions: 4298/10000 (42.98%)

def predict_output(A, B, C, D, E):
    if (B > 70 and E < 20) or (A > 60 and C < 20 and E > 50) or (C < 15 and D > 60) or (D > 70 and C < 30) or (C < 25 and E > 65) or (B > 65 and C > 70 and E < 5):
        return 4
    elif B > 80 or (C > 80 and E > 80):
        return 2
    elif (A > 50 and B < 20) or (D > 60 and E > 60):
        return 3
    else:
        return 1