"""
Predictor 1372
Generated on: 2025-09-10 02:16:28
Accuracy: 54.83%
"""


# PREDICTOR 1372 - Accuracy: 54.83%
# Correct predictions: 5483/10000 (54.83%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C < 20 and E > 80) or (B > 70 and D < 20) or (A < 20 and C > 75 and D < 30):
        return 4
    elif (B > 85 and C > 80) or (A < 20 and B > 90 and C < 35 and D > 70) or (B > 70 and E > 80 and C > 50) or (A < 50 and B > 70 and D < 20 and E > 40):
        return 2
    elif (A > 50 and C < 50 and D > 70) or (D < 15 and C > 40) or (C < 10 and E < 60) or (A < 10 and B > 80 and C > 80 and D < 5):
        return 3
    else:
        return 1