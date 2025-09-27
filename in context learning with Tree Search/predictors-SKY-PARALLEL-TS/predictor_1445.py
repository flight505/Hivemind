"""
Predictor 1445
Generated on: 2025-09-10 02:27:48
Accuracy: 48.37%
"""


# PREDICTOR 1445 - Accuracy: 48.37%
# Correct predictions: 4837/10000 (48.37%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (D > 90 and C < 10) or (C > 90 and E < 5) or (B > 70 and C < 20 and A > 50):
        return 4
    elif B < 30 and (C > 90 or D > 70):
        return 3
    elif E > 70 and (B > 80 or C < 15):
        return 2
    else:
        return 1