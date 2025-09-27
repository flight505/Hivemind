"""
Predictor 1011
Generated on: 2025-09-10 01:15:51
Accuracy: 54.02%
"""


# PREDICTOR 1011 - Accuracy: 54.02%
# Correct predictions: 5402/10000 (54.02%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (B > 80 and E > 90) or (C > 80 and B < 40 and E < 35) or (B > 70 and C < 30 and D > 60) or (C > 80 and B < 20 and E < 10):
        return 4
    elif A > 90 and E < 10:
        return 2
    elif (B < 10 and D > 80 and A < 50) or (C < 5 and B > 50) or (A < 15 and B < 25 and C > 30) or (B > 70 and D > 95 and E > 80):
        return 3
    else:
        return 1