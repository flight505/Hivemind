"""
Predictor 261
Generated on: 2025-09-09 23:43:38
Accuracy: 57.33%
"""


# PREDICTOR 261 - Accuracy: 57.33%
# Correct predictions: 5733/10000 (57.33%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (C < 25 and E > 70):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80 and A < 80 and D > 20) or (A < 5 and E > 90) or (A > 70 and B > 70 and E < 25) or (B > 80 and E < 10) or (C > 80 and D < 10 and B < 50):
        return 2
    elif (B < 10 and D > 80) or (A > 50 and C < 50 and D > 70 and B > 40) or (A < 5 and B < 5 and E < 5):
        return 3
    else:
        return 1