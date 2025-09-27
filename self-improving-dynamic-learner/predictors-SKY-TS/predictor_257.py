"""
Predictor 257
Generated on: 2025-09-09 21:22:33
Accuracy: 51.65%
"""


# PREDICTOR 257 - Accuracy: 51.65%
# Correct predictions: 5165/10000 (51.65%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if E < 20:
                if D < 50:
                    return 1
                else:
                    return 4
            else:
                return 4
        else:
            if E < 30:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if D > 30 or B > 50 or A > 70 or E > 40:
                return 1
            else:
                return 4
        else:
            if E < 20:
                return 1
            elif E > 80:
                return 4
            elif A >= 70 and D < 30 and E < 50:
                return 1
            else:
                return 3