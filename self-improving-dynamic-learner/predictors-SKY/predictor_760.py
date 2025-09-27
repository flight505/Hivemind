"""
Predictor 760
Generated on: 2025-09-09 20:26:26
Accuracy: 58.37%
"""


# PREDICTOR 760 - Accuracy: 58.37%
# Correct predictions: 5837/10000 (58.37%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    elif B > 60 and C >= 70 and A < 50:
        return 2
    elif E > 90 and C < 25:
        return 4
    else:
        return 1