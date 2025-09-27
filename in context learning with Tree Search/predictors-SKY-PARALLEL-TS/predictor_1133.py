"""
Predictor 1133
Generated on: 2025-09-10 01:35:54
Accuracy: 42.91%
"""


# PREDICTOR 1133 - Accuracy: 42.91%
# Correct predictions: 4291/10000 (42.91%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (D < 20 and E > 70 and A > 30 and C < 50) or (B < 10 and E > 80):
        return 4
    elif max(B, E) > 80:
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (D < 15 and C > 40 and B < 80) or (C < 10 and E < 60) or (A + B < 100 and D > 80 and E < 30):
        return 3
    else:
        return 1