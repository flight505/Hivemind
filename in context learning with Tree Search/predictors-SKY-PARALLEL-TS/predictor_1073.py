"""
Predictor 1073
Generated on: 2025-09-10 01:25:44
Accuracy: 51.22%
"""


# PREDICTOR 1073 - Accuracy: 51.22%
# Correct predictions: 5122/10000 (51.22%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C > 80 and D < 20 and E < 20) or (C < 5 and E > 60) or (C > 65 and D < 30 and E > 40) or (A > 60 and B < 20 and E > 50) or (A < 20 and C > 60 and D < 30):
        return 4
    elif (A > 90 and E < 10) or (A < 5 and B > 95):
        return 2
    elif (B < 10 and D > 80) or (A < 5 and C > 70 and D < 10) or (B > 70 and C < 10):
        return 3
    else:
        return 1