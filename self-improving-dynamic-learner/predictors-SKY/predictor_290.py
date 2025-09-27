"""
Predictor 290
Generated on: 2025-09-09 15:06:52
Accuracy: 60.29%
"""


# PREDICTOR 290 - Accuracy: 60.29%
# Correct predictions: 6029/10000 (60.29%)

def predict_output(A, B, C, D, E):
    if C < 25:
        if E > 70:
            if B > 30 or D > 50:
                return 4
            else:
                return 1
        elif E > 50 and B < 80 and D < 70:
            return 4
        elif B < 25:
            return 3
        else:
            return 1
    else:
        if E < 10 and C > 50:
            return 4
        elif E > 70 and B > 70 and C < 55:
            return 4
        elif B > 60 and C > 60 and A < 50:
            return 2
        else:
            return 1