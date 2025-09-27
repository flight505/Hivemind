"""
Predictor 1367
Generated on: 2025-09-10 02:16:28
Accuracy: 51.24%
"""


# PREDICTOR 1367 - Accuracy: 51.24%
# Correct predictions: 5124/10000 (51.24%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90 and E > 80) or (A < 10 and B > 90 and C > 70 and E > 70):
        return 4
    elif B > 80 or (C > 90 and B < 20 and A < 50):
        return 2
    elif (A > 50 and C < 50 and D > 65 and B > 40) or (60 < A < 80 and D < 20 and E < 20) or (A < 20 and C > 80 and D < 10 and E < 30):
        return 3
    else:
        return 1