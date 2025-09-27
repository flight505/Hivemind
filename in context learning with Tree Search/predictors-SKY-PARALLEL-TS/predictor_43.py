"""
Predictor 43
Generated on: 2025-09-09 23:21:45
Accuracy: 51.43%
"""


# PREDICTOR 43 - Accuracy: 51.43%
# Correct predictions: 5143/10000 (51.43%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (E < 10 and C > 70):
        return 4
    elif (B < 30 and A > 70 and E > 10) or (C < 10 and D > 60 and E < 40) or (B > 90 and D > 90):
        return 3
    elif B > 80 and E < 10 and A < 50:
        return 2
    else:
        return 1