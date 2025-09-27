"""
Predictor 939
Generated on: 2025-09-10 01:07:55
Accuracy: 43.85%
"""


# PREDICTOR 939 - Accuracy: 43.85%
# Correct predictions: 4385/10000 (43.85%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 75) or (C < 15 and D > 90) or (B > 80 and E > 90) or (A < 15 and B > 80 and E > 75):
        return 4
    elif B > 60 and C > 40 and E > 60:
        return 2
    elif (B < 10 or D < 5) or (C < 15 and E < 15) or (C > 80 and D > 60) or (A < 10 and C < 15):
        return 3
    else:
        return 1