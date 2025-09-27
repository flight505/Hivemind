"""
Predictor 1206
Generated on: 2025-09-10 01:46:44
Accuracy: 56.78%
"""


# PREDICTOR 1206 - Accuracy: 56.78%
# Correct predictions: 5678/10000 (56.78%)

def predict_output(A, B, C, D, E):
    if (C > 70 and E < 5) or (C < 20 and D > 80) or (D < 10 and E > 90) or (C < 20 and D > 95) or (A > 65 and D < 10 and E > 90):
        return 4
    elif (B > 80 and E > 80) or (B > 60 and C < 50 and D > 60 and E < 50 and A > 60):
        return 2
    elif (B > 70 and C < 10 and D > 80) or (A < 30 and B > 90 and D > 90) or (A > 40 and B > 70 and C < 25 and D > 95):
        return 3
    else:
        return 1