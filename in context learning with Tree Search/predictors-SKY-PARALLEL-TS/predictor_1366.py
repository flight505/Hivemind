"""
Predictor 1366
Generated on: 2025-09-10 02:16:28
Accuracy: 51.94%
"""


# PREDICTOR 1366 - Accuracy: 51.94%
# Correct predictions: 5194/10000 (51.94%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 70 and D < 30 and E > 70):
        return 4
    elif (C > 90 and B < 20 and A < 50) or (B > 90 and C > 70) or (B > 80 and E > 80) or (B > 90 and A > 80):
        return 2
    elif (A > 60 and D < 20 and E < 20) or (C > 80 and B < 10) or (D < 10 and A < 20):
        return 3
    else:
        return 1