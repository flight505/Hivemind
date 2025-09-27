"""
Predictor 956
Generated on: 2025-09-10 01:09:35
Accuracy: 57.11%
"""


# PREDICTOR 956 - Accuracy: 57.11%
# Correct predictions: 5711/10000 (57.11%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 50) or \
       (C < 15 and D > 70) or \
       (B > 90 and E > 90) or \
       (C > 80 and B < 40 and D < 50) or \
       (C > 55 and D < 30 and B < 60) or \
       (C < 30 and D < 10 and E > 50 and A < 60):
        return 4
    elif (B > 85 and C > 80):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1