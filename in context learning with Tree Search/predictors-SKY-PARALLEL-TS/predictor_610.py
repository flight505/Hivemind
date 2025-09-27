"""
Predictor 610
Generated on: 2025-09-10 00:24:42
Accuracy: 54.14%
"""


# PREDICTOR 610 - Accuracy: 54.14%
# Correct predictions: 5414/10000 (54.14%)

def predict_output(A, B, C, D, E):
    if (B - A > 60) or (D - C > 70 and E > 80) or (D < 10 and E > 50) or (B > 80 and C < 35 and E > 50) or (A > 70 and B < 5) or (C > 65 and D < 30 and A < 15) or (A > 40 and B > 50 and C < 40 and D < 10 and E > 50) or (A < 45 and B > 80 and C < 35 and E > 55) or (A < 20 and B < 35 and C > 65 and D < 30 and E < 45):
        return 4
    elif (A > 80 and B > 80 and C < 50 and D > 60 and E < 20) or (B > 85 and C > 80):
        return 2
    elif (D - C > 70 and E < 50) or (C > 60 and D < 10 and E < 20) or (C < 5 and D > 45 and E > 45 and A < 10) or (C < 15 and D > 50 and E < 50 and B < 30) or (A < 50 and B < 45 and C < 15 and D > 95 and E < 50) or (A > 35 and B < 30 and C < 15 and D > 50 and E < 50):
        return 3
    else:
        return 1