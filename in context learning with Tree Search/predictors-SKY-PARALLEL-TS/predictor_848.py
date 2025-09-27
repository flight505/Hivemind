"""
Predictor 848
Generated on: 2025-09-10 00:55:50
Accuracy: 50.42%
"""


# PREDICTOR 848 - Accuracy: 50.42%
# Correct predictions: 5042/10000 (50.42%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 90) or (E > 90 and D < 30) or (B < 5 and C > 60) or (C > 90 and D < 25) or (C < 20 and D < 20 and E > 80) or (A > 80 and C < 20 and D > 70):
        return 4
    elif (A < 10 and E > 90) or (B > 85 and C > 80):
        return 2
    elif (A > 70 and B < 30 and C > 70 and D < 10):
        return 3
    else:
        return 1