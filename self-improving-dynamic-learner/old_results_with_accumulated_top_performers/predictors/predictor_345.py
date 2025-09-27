"""
Predictor 345
Generated on: 2025-09-09 08:58:35
Accuracy: 31.77%
"""


# PREDICTOR 345 - Accuracy: 31.77%
# Correct predictions: 3177/10000 (31.77%)

def predict_output(A, B, C, D, E):
    if A > B and A > C and A > D and A > E:
        return 3
    elif B > A and B > C and B > D and B > E:
        return 2
    elif C > A and C > B and C > D and C > E:
        return 1
    elif D > A and D > B and D > C and D > E:
        return 4
    else:
        return 1