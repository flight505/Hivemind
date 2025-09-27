"""
Predictor 202
Generated on: 2025-09-09 05:16:06
Accuracy: 34.83%
"""


# PREDICTOR 202 - Accuracy: 34.83%
# Correct predictions: 3483/10000 (34.83%)

def predict_output(A, B, C, D, E):
    if B < 25 and C < 25:
        return 3
    elif C > 60:
        if B > 70:
            if D < 20:
                return 1
            else:
                return 2
        else:
            return 2
    elif E > 80:
        return 4
    else:
        return 1