"""
Predictor 881
Generated on: 2025-09-10 00:58:03
Accuracy: 48.60%
"""


# PREDICTOR 881 - Accuracy: 48.60%
# Correct predictions: 4860/10000 (48.60%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (B < 15 and C > 80) or (E < 10 and C > 50) or (B > 80 and E > 90) or (C > 70 and E > 90) or (C > 80 and E < 20):
        return 4
    elif (A > 90 and B > 85) or (B > 95 and E < 10):
        return 2
    elif (A > 70 and D > 50 and B < 40):
        return 3
    else:
        return 1