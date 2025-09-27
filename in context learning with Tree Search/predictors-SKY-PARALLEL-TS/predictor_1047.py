"""
Predictor 1047
Generated on: 2025-09-10 01:23:11
Accuracy: 50.42%
"""


# PREDICTOR 1047 - Accuracy: 50.42%
# Correct predictions: 5042/10000 (50.42%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (C > 95 and D < 25) or (A > 70 and B < 35 and C < 15):
        return 4
    elif (B > 65 and C > 80) or (A < 15 and C < 15 and D > 70):
        return 2
    elif (C < 15 and D > 70 and B < 50) or (A > 45 and B > 30 and C < 30 and D < 35) or (A > 90 and B < 20) or (C > 80 and D < 10):
        return 3
    else:
        return 1