"""
Predictor 805
Generated on: 2025-09-10 00:50:43
Accuracy: 52.45%
"""


# PREDICTOR 805 - Accuracy: 52.45%
# Correct predictions: 5245/10000 (52.45%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 60 and D < 20) or (A > 80 and B < 10) or (A > 70 and B < 20 and E < 25) or (C > 90 and E < 15) or (B > 95 and C < 40):
        return 4
    elif (B > 95 and C > 70 and D > 90) or (B > 85 and E < 10):
        return 2
    elif (A > 90 and B < 10 and D > 90):
        return 3
    else:
        return 1