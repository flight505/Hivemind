"""
Predictor 867
Generated on: 2025-09-10 00:58:03
Accuracy: 56.16%
"""


# PREDICTOR 867 - Accuracy: 56.16%
# Correct predictions: 5616/10000 (56.16%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10) or (B > 80 and E > 70) or (C > 85 and E < 10 and D > 10) or (C < 15 and D > 90) or (C < 5 and E > 50) or (B > 80 and C > 50 and E > 70) or (C > 80 and D < 20 and E > 90) or (A > 60 and B > 80 and C < 30) or (A > 50 and C > 80 and E < 10) or (A > 40 and B < 30 and C < 5 and E > 55) or (B > 80 and E > 90):
        return 4
    elif (B > 80 and C > 89) or (B > 75 and D > 60 and C < 40) or (A < 25 and B > 80 and C > 90) or (D < 5 and C > 50 and B < 50 and E > 50 and A < 70) or (B > 75 and C < 35 and D > 60):
        return 2
    elif (A < 10 and B > 90 and E < 20) or (A < 5 and C > 80 and D < 10 and E < 10) or (B > 90 and C < 30 and E < 20) or (A < 5 and C > 85 and E < 10) or (A < 10 and B > 80 and C < 30):
        return 3
    else:
        return 1