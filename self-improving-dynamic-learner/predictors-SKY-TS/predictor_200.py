"""
Predictor 200
Generated on: 2025-09-09 20:55:47
Accuracy: 47.36%
"""


# PREDICTOR 200 - Accuracy: 47.36%
# Correct predictions: 4736/10000 (47.36%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                return 4
        else:
            if E < 40:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                if A > 50:
                    return 1
                else:
                    return 4
            else:
                return 1
        else:
            if E < 20:
                if B < 20:
                    return 1
                elif B > 50:
                    return 3
                else:
                    return 4
            else:
                if E > 90:
                    return 2
                elif D > 70 and E < 50:
                    return 4
                else:
                    return 3