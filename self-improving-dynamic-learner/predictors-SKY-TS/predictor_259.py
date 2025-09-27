"""
Predictor 259
Generated on: 2025-09-09 21:22:33
Accuracy: 50.66%
"""


# PREDICTOR 259 - Accuracy: 50.66%
# Correct predictions: 5066/10000 (50.66%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if E < 20 and D < 50:
                return 1
            else:
                return 4
        else:
            if E < 30:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                return 4
            else:
                return 1
        else:
            if E < 20:
                return 1
            else:
                if E > 70:
                    return 4
                elif C < 30 and B > 40 and D < 30:
                    return 1
                else:
                    return 3