"""
Predictor 1327
Generated on: 2025-09-10 02:07:02
Accuracy: 50.00%
"""


# PREDICTOR 1327 - Accuracy: 50.00%
# Correct predictions: 5000/10000 (50.00%)

def predict_output(A, B, C, D, E):
    if B > 70 and C < 25 and E < 25:
        return 3
    if B > 80 or (B + D > 150):
        return 2
    if (A < 15 and B > 65 and C < 75 and E < 75) or (C < 30 and E > 75) or (C < 20 and D > 85):
        return 4
    else:
        return 1