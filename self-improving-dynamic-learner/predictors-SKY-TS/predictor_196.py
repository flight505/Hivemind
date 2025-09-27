"""
Predictor 196
Generated on: 2025-09-09 20:54:12
Accuracy: 44.13%
"""


# PREDICTOR 196 - Accuracy: 44.13%
# Correct predictions: 4413/10000 (44.13%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            if E < 60:
                return 1
            else:
                return 2
        else:
            if E < 20:
                if D < 30:
                    return 1
                else:
                    return 4
            else:
                if D + E > 140:
                    return 1
                else:
                    return 4
    else:
        if C > 50:
            if D > 50:
                return 1
            else:
                return 4
        else:
            if E < 25:
                return 1
            elif D < 20 and E > 80:
                return 4
            elif D < 15 and E > 60:
                return 2
            elif D < 30 and A > 70:
                return 1
            elif E > 90:
                return 1
            else:
                return 3