"""
Predictor 667
Generated on: 2025-09-10 00:31:36
Accuracy: 56.86%
"""


# PREDICTOR 667 - Accuracy: 56.86%
# Correct predictions: 5686/10000 (56.86%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (E > 60 and C < 35 and D < 40) or (B > 70 and D < 20 and E > 90):
        return 4
    elif B > 85 and E < 20:
        return 2
    elif (A > 70 and C < 30 and D > 70) or (D < 5 and E < 25):
        return 3
    else:
        return 1