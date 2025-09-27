"""
Predictor 421
Generated on: 2025-09-10 00:02:23
Accuracy: 46.67%
"""


# PREDICTOR 421 - Accuracy: 46.67%
# Correct predictions: 4667/10000 (46.67%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90 and E > 80) or (C > 80 and D < 20 and E > 80) or (B < 20 and C > 40) or (D < 10 and E > 50):
        return 4
    elif (C < 15 and D > 70 and E < 60) or (B > 80 and C > 70) or (A > 90 and E < 10):
        return 2
    elif (C < 30 and D > 80 and E > 90) or (A > 80 and C < 30 and D > 80) or (C > 70 and D < 15 and E < 10) or (D > 90 and E > 70):
        return 3
    else:
        return 1