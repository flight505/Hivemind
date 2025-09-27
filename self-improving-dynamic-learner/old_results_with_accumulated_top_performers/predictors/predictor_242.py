"""
Predictor 242
Generated on: 2025-09-09 06:03:36
Accuracy: 38.96%
"""


# PREDICTOR 242 - Accuracy: 38.96%
# Correct predictions: 3896/10000 (38.96%)

def predict_output(A, B, C, D, E):
    if B + C < 30:
        return 3
    elif E > 80:
        return 4
    elif A > 70 and B < 25 and 25 <= C <= 50:
        return 3
    elif A < 30 and B > 70:
        if 25 <= C <= 50:
            return 4
        elif C < 25 and D < 30:
            return 3
    elif C > 60:
        if A > 70:
            return 1
        else:
            return 2
    else:
        return 1