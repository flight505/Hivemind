"""
Predictor 603
Generated on: 2025-09-10 00:24:42
Accuracy: 49.80%
"""


# PREDICTOR 603 - Accuracy: 49.80%
# Correct predictions: 4980/10000 (49.80%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 70 and D < 30) or (E < 5 and D > 45) or (A < 35 and C > 70 and D < 30):
        return 4
    elif (A > 90 and B > 80) or (B > 95 and C > 70) or (A > 90 and E < 10):
        return 2
    elif (B < 10 and D > 80) or (B < 5 and D < 15) or (A > 80 and E > 90 and B < 30) or (A > 90 and B < 20 and D > 95) or (B > 70 and D > 75 and C > 50):
        return 3
    else:
        return 1