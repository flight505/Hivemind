"""
Predictor 40
Generated on: 2025-09-09 23:21:45
Accuracy: 51.53%
"""


# PREDICTOR 40 - Accuracy: 51.53%
# Correct predictions: 5153/10000 (51.53%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 75) or (C < 15 and D > 90) or (E < 5 and C > 70):
        return 4
    elif (B < 30 and A > 70 and E > 10) or (C < 10 and D > 60 and E < 40) or (B > 90 and D > 90):
        return 3
    elif B > 80 and E < 10 and A < 50:
        return 2
    else:
        return 1