"""
Predictor 1205
Generated on: 2025-09-10 01:46:44
Accuracy: 55.57%
"""


# PREDICTOR 1205 - Accuracy: 55.57%
# Correct predictions: 5557/10000 (55.57%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 90) or (C > 70 and E < 5) or (E > 90 and D < 10) or (A < 30 and D > 45 and C > 40 and E < 20):
        return 4
    elif (B > 80 and D > 80 and E > 80) or (A > 60 and B > 65 and C < 50 and D > 60 and E < 50):
        return 2
    elif (A < 30 and B > 70 and C < 10 and D > 80):
        return 3
    else:
        return 1