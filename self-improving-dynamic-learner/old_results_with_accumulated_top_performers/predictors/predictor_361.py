"""
Predictor 361
Generated on: 2025-09-09 09:44:41
Accuracy: 37.70%
"""


# PREDICTOR 361 - Accuracy: 37.70%
# Correct predictions: 3770/10000 (37.70%)

def predict_output(A, B, C, D, E):
    if B < 20:
        return 3
    elif E > 80:
        return 4
    elif C > 60:
        if A > 70:
            return 1
        else:
            return 2
    else:
        return 1