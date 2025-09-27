"""
Predictor 656
Generated on: 2025-09-10 00:31:36
Accuracy: 48.10%
"""


# PREDICTOR 656 - Accuracy: 48.10%
# Correct predictions: 4810/10000 (48.10%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 70) or (C < 25 and D > 85) or (C > 85) or (A > 90 and B < 10 and C > 70):
        return 4
    elif (A < 5 and E > 60) or (B > 70 and A < 50 and C > 30 and D > 40):
        return 2
    elif A > 90 and B < 30 and D > 60:
        return 3
    else:
        return 1