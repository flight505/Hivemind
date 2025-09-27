"""
Predictor 1174
Generated on: 2025-09-10 01:39:40
Accuracy: 51.35%
"""


# PREDICTOR 1174 - Accuracy: 51.35%
# Correct predictions: 5135/10000 (51.35%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 90 and E > 80) or (B > 70 and E > 80 and A < 50):
        return 4
    elif (B > 80 and C < 60) or (A > 80 and B > 70 and C < 60):
        return 2
    elif (A > 70 and B < 40 and D > 80) or (A < 10 and B > 60 and D < 15 and C < 25) or (C < 20 and E < 10 and B > 30):
        return 3
    else:
        return 1