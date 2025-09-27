"""
Predictor 330
Generated on: 2025-09-09 08:35:49
Accuracy: 32.62%
"""


# PREDICTOR 330 - Accuracy: 32.62%
# Correct predictions: 3262/10000 (32.62%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    elif E > 90:
        return 4
    elif C > 60 and A > 50:
        return 1
    elif B > 60 and C > 60:
        return 2
    else:
        return 3