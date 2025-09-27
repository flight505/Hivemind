"""
Predictor 1375
Generated on: 2025-09-10 02:16:28
Accuracy: 55.31%
"""


# PREDICTOR 1375 - Accuracy: 55.31%
# Correct predictions: 5531/10000 (55.31%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C > 80 and E < 5) or (B < 25 and C < 35 and E > 65) or (A > 65 and B < 25 and C < 35 and E > 55) or (A > 35 and C > 85 and D < 35 and E < 5):
        return 4
    elif (B > 90 and D > 70) or (B > 70 and E > 80 and C > 50) or (A < 20 and B > 90 and C < 35 and D > 70) or (A < 45 and B > 70 and C > 50 and D > 60):
        return 2
    elif (B > 80 and D < 5) or (A > 50 and C < 15 and D < 20) or (A > 50 and B < 30 and C < 15 and D < 15):
        return 3
    else:
        return 1