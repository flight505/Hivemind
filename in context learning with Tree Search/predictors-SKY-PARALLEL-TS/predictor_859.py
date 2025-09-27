"""
Predictor 859
Generated on: 2025-09-10 00:55:50
Accuracy: 52.49%
"""


# PREDICTOR 859 - Accuracy: 52.49%
# Correct predictions: 5249/10000 (52.49%)

def predict_output(A, B, C, D, E):
    if (C < 20 and D > 80) or (A < 10 and B > 70) or (C < 10 and D > 90) or (C < 15 and D > 85 and A > 60):
        return 4
    elif B > 75 and C > 40:
        return 2
    elif (B > 70 and D > 80 and E > 80) or (A > 80 and B < 15 and C < 20):
        return 3
    else:
        return 1