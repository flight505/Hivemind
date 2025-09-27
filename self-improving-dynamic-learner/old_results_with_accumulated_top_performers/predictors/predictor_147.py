"""
Predictor 147
Generated on: 2025-09-09 04:31:39
Accuracy: 53.89%
"""


# PREDICTOR 147 - Accuracy: 53.89%
# Correct predictions: 5389/10000 (53.89%)

def predict_output(A, B, C, D, E):
    if B < 25 and C < 25:
        return 3
    elif E > 90:
        return 4
    elif B > 60 and C > 60 and A < 35:
        return 2
    else:
        return 1