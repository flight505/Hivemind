"""
Predictor 1223
Generated on: 2025-09-10 01:46:44
Accuracy: 50.00%
"""


# PREDICTOR 1223 - Accuracy: 50.00%
# Correct predictions: 5000/10000 (50.00%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 10 and D > 90) or (B > 60 and D < 50 and C < 80) or (B > 70 and D < 20 and E > 90):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80 and A > 20) or (B > 70 and D < 20 and A < 50 and E > 40):
        return 2
    elif A > 80 and D > 90 or (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1