"""
Predictor 1292
Generated on: 2025-09-10 02:02:09
Accuracy: 49.00%
"""


# PREDICTOR 1292 - Accuracy: 49.00%
# Correct predictions: 4900/10000 (49.00%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A < 15 and B < 15 and C > 50) or (B < 15 and C > 60) or (C > 85 and A < 15):
        return 4
    elif (A > 90 and E < 10) or (B > 65 and C > 70) or (C > 80 and D < 10) or (B > 85 and C > 80):
        return 2
    elif (B < 10 and D > 80 and C > 30) or (B > 70 and D > 70 and C < 45) or (C < 15 and D > 70) or (A > 50 and C < 50 and D > 70):
        return 3
    else:
        return 1