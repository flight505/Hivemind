"""
Predictor 937
Generated on: 2025-09-10 01:07:55
Accuracy: 47.73%
"""


# PREDICTOR 937 - Accuracy: 47.73%
# Correct predictions: 4773/10000 (47.73%)

def predict_output(A, B, C, D, E):
    if (A <= 10 and B > 70) or (C < 15 and D > 90) or (B > 80 and E > 90) or (A < 20 and B > 90):
        return 4
    elif A < 50 and B > 60 and C > 40 and E > 60 and D > 50:
        return 2
    elif (B < 5 or D < 5) or (C < 10 and E < 10) or (C < 15 and E < 15) or (A < 10 and C < 15) or (C > 80 and D > 60) or (A > 50 and B < 10 and D < 5):
        return 3
    else:
        return 1