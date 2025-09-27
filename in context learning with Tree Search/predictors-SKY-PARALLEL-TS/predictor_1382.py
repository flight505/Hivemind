"""
Predictor 1382
Generated on: 2025-09-10 02:16:28
Accuracy: 57.62%
"""


# PREDICTOR 1382 - Accuracy: 57.62%
# Correct predictions: 5762/10000 (57.62%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (B < 20 and E > 90) or (C < 20 and B > 80) or (E < 5 and D > 50) or (C < 30 and E > 65) or (A < 30 and C > 75 and D < 30 and B < 60) or (A > 80 and B < 10 and D > 70 and E < 10) or (A > 60 and B > 80 and C < 10 and D > 70) or (A < 15 and C > 60 and E < 5) or (B > 70 and D < 20 and E > 90) or (A > 70 and B < 20 and C > 70 and D < 10) or (C < 15 and D > 80):
        return 4
    elif (B > 90) or (B > 85 and C > 80) or (B > 70 and D < 20 and A < 50 and E > 40) or (D < 5 and C > 50 and B < 50 and E > 50) or (A < 40 and D < 25 and E > 50 and C > 40) or (A < 30 and B > 80 and C > 70):
        return 2
    elif (A > 50 and C < 50 and D > 65 and B > 40) or (A < 50 and D < 25 and E < 40 and B < 80) or (D < 15 and C > 40 and B < 80 and A < 70) or (C <= 10 and E < 60 and B < 50) or (A > 75 and B < 25 and C < 45 and D > 60) or (B > 80 and C > 85 and D > 80 and A < 50) or (A < 40 and B > 90 and D > 90) or (A > 60 and B < 15 and C < 15 and D > 70) or (A < 5 and B < 30 and C < 30 and D > 30 and E < 25) or (D > 70 and C < 35) or (A > 80 and E > 75):
        return 3
    else:
        return 1