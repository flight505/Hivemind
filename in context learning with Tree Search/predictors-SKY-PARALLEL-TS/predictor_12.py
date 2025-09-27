"""
Predictor 12
Generated on: 2025-09-09 23:16:45
Accuracy: 36.27%
"""


# PREDICTOR 12 - Accuracy: 36.27%
# Correct predictions: 3627/10000 (36.27%)

def predict_output(A, B, C, D, E):
    if B > 70 or D > 90:
        return 4
    elif A > 80 and C > 60:
        return 2
    elif E > 90 and D < 20:
        return 3
    else:
        return 1