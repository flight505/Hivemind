"""
Predictor 1487
Generated on: 2025-09-10 02:35:36
Accuracy: 49.64%
"""


# PREDICTOR 1487 - Accuracy: 49.64%
# Correct predictions: 4964/10000 (49.64%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C > 20) or (C < 10 and D > 90) or (A < 10 and C > 70):
        return 4
    elif A < 10 and B > 60 and C < 20 and E < 50:
        return 3
    elif B > 80 or (A < 20 and E > 60 and B > 50):
        return 2
    else:
        return 1