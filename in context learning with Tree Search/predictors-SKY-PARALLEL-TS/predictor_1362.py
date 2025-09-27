"""
Predictor 1362
Generated on: 2025-09-10 02:14:38
Accuracy: 55.18%
"""


# PREDICTOR 1362 - Accuracy: 55.18%
# Correct predictions: 5518/10000 (55.18%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A > 60 and C < 40 and D > 50) or (E > 90 and A > 60) or (C > 90 and A < 15 and D < 40):
        return 4
    elif A > 90 and E < 10 or (B > 85 and C > 90 and E < 25):
        return 2
    elif B < 10 and D > 80 or (C > 90 and D < 5 and E < 25):
        return 3
    else:
        return 1