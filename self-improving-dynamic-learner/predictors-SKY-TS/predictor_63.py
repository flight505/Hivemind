"""
Predictor 63
Generated on: 2025-09-09 19:38:58
Accuracy: 46.66%
"""


# PREDICTOR 63 - Accuracy: 46.66%
# Correct predictions: 4666/10000 (46.66%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40 and E < 20:
                return 1
            elif D > 90 and E > 50:
                return 2
            else:
                return 4
        else:
            if D < 50:
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
                if D > 60:
                    return 1
                else:
                    return 4
            else:
                if B >= 60:
                    return 4
                else:
                    return 3