"""
Predictor 866
Generated on: 2025-09-10 00:58:03
Accuracy: 56.47%
"""


# PREDICTOR 866 - Accuracy: 56.47%
# Correct predictions: 5647/10000 (56.47%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (B > 80 and C > 80 and E > 80) or (C > 85 and E < 10 and A > 40) or (C < 25 and E > 60) or (B < 10 and D > 70 and A > 70) or (B > 90 and E > 70):
        return 4
    elif (B > 80 and C > 80 and E < 80) or (B > 70 and D < 20 and E > 40) or (B > 75 and C < 35 and D > 60):
        return 2
    elif (A < 10 and B > 90 and E < 20) or (B > 70 and C < 30 and D > 60) or (C > 80 and A < 10 and E < 10):
        return 3
    else:
        return 1