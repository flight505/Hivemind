"""
Predictor 1473
Generated on: 2025-09-10 02:31:46
Accuracy: 45.84%
"""


# PREDICTOR 1473 - Accuracy: 45.84%
# Correct predictions: 4584/10000 (45.84%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C > 20) or (C < 10 and D > 80) or (A >= 70 and C < 30 and D > 50) or (C > 85 and E < 10):
        return 4
    elif A > 90 or (B > 60 and E > 50):
        return 2
    elif (B < 10 and D > 80) or (A < 10 and B < 10 and C > 70):
        return 3
    else:
        return 1