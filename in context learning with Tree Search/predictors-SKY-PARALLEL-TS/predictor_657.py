"""
Predictor 657
Generated on: 2025-09-10 00:31:36
Accuracy: 57.93%
"""


# PREDICTOR 657 - Accuracy: 57.93%
# Correct predictions: 5793/10000 (57.93%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 25 and D > 85) or (C > 85 and D < 15 and E < 40) or (A > 90 and B < 10 and C > 70 and D < 30 and E < 30):
        return 4
    elif (A < 5 and E > 60 and C < 20) or (B > 70 and A < 50 and C > 30 and D > 40):
        return 2
    elif A > 90 and B < 30 and D > 60:
        return 3
    else:
        return 1