"""
Predictor 934
Generated on: 2025-09-10 01:07:55
Accuracy: 59.92%
"""


# PREDICTOR 934 - Accuracy: 59.92%
# Correct predictions: 5992/10000 (59.92%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (C < 35 and E > 60):
        return 4
    elif (B > 85 and E > 70) or (B > 95):
        return 2
    elif (A > 40 and B > 50 and C < 35 and D > 75) or (A < 15 and B > 40 and C < 15 and D > 40) or (A > 50 and B < 30 and C < 40 and D < 20):
        return 3
    else:
        return 1