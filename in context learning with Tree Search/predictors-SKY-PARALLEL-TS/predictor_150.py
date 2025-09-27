"""
Predictor 150
Generated on: 2025-09-09 23:32:27
Accuracy: 56.26%
"""


# PREDICTOR 150 - Accuracy: 56.26%
# Correct predictions: 5626/10000 (56.26%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (D < 10 and E > 90) or (A > 85 and E > 95):
        return 4
    elif (B > 80 and C > 70 and A < 40):
        return 2
    elif (D > 90 and E < 10) or (A > 90 and D > 90):
        return 3
    else:
        return 1