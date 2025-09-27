"""
Predictor 19
Generated on: 2025-09-09 23:19:12
Accuracy: 43.35%
"""


# PREDICTOR 19 - Accuracy: 43.35%
# Correct predictions: 4335/10000 (43.35%)

def predict_output(A, B, C, D, E):
    if (B > 70 and not (A > 90 and B > 80)) or (C < 20 and D > 70) or (E > 90) or (A > 80 and B < 10):
        return 4
    elif A > 80 and E < 40 and D > 50:
        return 2
    elif D > 80 and C < 40 and A > 70:
        return 3
    else:
        return 1