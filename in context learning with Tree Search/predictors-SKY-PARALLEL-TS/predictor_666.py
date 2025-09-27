"""
Predictor 666
Generated on: 2025-09-10 00:31:36
Accuracy: 58.79%
"""


# PREDICTOR 666 - Accuracy: 58.79%
# Correct predictions: 5879/10000 (58.79%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (E > 50 and C + D < 70) or (B > 70 and D < 20 and E > 90):
        return 4
    elif B > 85 and C > 60 and E < 20:
        return 2
    elif (A > 70 and C < 30 and D > 70) or (D < 10) or (A - C > 40 and D > 70):
        return 3
    else:
        return 1