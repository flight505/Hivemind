"""
Predictor 1132
Generated on: 2025-09-10 01:35:54
Accuracy: 47.04%
"""


# PREDICTOR 1132 - Accuracy: 47.04%
# Correct predictions: 4704/10000 (47.04%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (D < 20 and E > 70 and A > 30 and C < 50) or (B < 10 and E > 80):
        return 4
    elif B > 80 or E > 80:
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (D < 15 and C > 40 and B < 80) or (C < 10 and E < 60):
        return 3
    else:
        return 1