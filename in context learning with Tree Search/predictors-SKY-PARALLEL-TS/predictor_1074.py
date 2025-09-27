"""
Predictor 1074
Generated on: 2025-09-10 01:25:44
Accuracy: 50.29%
"""


# PREDICTOR 1074 - Accuracy: 50.29%
# Correct predictions: 5029/10000 (50.29%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 60 and E > 50) or (C > 80 and D < 25 and A > 10) or (C > 60 and D < 30) or (B < 20 and E > 50):
        return 4
    elif B > 95 and D > 80:
        return 2
    elif (C > 70 and D < 10 and A < 5) or (C < 10 and D < 20 and B > 70):
        return 3
    else:
        return 1