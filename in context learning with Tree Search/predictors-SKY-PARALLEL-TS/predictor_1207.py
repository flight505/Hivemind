"""
Predictor 1207
Generated on: 2025-09-10 01:46:44
Accuracy: 58.20%
"""


# PREDICTOR 1207 - Accuracy: 58.20%
# Correct predictions: 5820/10000 (58.20%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 90) or (D > 40 and E < 20) or (D < 10 and E > 90) or (A < 30 and C > 70 and E < 5) or (C < 25 and E > 65):
        return 4
    if (B > 60 and D > 60 and E > 45 and C < 50) or (B > 85 and C > 80 and A < 80 and D > 40):
        return 2
    if (C < 10 and D > 80 and B > 70) or (A > 45 and C > 15 and C < 50 and D > 55 and B > 35):
        return 3
    else:
        return 1