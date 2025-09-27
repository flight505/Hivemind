"""
Predictor 268
Generated on: 2025-09-09 23:43:38
Accuracy: 56.02%
"""


# PREDICTOR 268 - Accuracy: 56.02%
# Correct predictions: 5602/10000 (56.02%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (B > 80 and C < 30 and E > 90) or (C > 90 and D < 25):
        return 4
    elif (B > 75 and C > 90) or (B > 90 and C > 75) or (B > 90 and E < 25) or (A > 90 and E < 10):
        return 2
    elif (A > 50 and C < 50 and D > 65 and B > 40) or (A < 15 and C > 80 and D < 15) or (A < 40 and B > 70 and C < 50 and D > 75) or (C <= 10 and E < 60):
        return 3
    else:
        return 1