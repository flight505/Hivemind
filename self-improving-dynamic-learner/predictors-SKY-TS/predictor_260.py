"""
Predictor 260
Generated on: 2025-09-09 21:22:33
Accuracy: 50.03%
"""


# PREDICTOR 260 - Accuracy: 50.03%
# Correct predictions: 5003/10000 (50.03%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if E < 20:
                if D > 50:
                    return 4
                else:
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
            elif E > 80:
                return 4
            else:
                if A > 70 and D < 30:
                    return 1
                else:
                    return 3