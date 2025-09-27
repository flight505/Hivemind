"""
Predictor 1124
Generated on: 2025-09-10 01:35:54
Accuracy: 48.82%
"""


# PREDICTOR 1124 - Accuracy: 48.82%
# Correct predictions: 4882/10000 (48.82%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (A > 60 and B < 20 and C < 15):
        return 4
    elif (D < 10 and E > 80) or (B > 70 and D < 15 and C > 40):
        return 2
    elif (D > 90 and C > 40) or (A > 60 and C < 5 and D > 70) or (E < 15 and C < 20 and A < 30) or (A > 50 and C < 25 and E < 40):
        return 3
    else:
        return 1