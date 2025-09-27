"""
Predictor 8
Generated on: 2025-09-09 18:58:34
Accuracy: 47.28%
"""


# PREDICTOR 8 - Accuracy: 47.28%
# Correct predictions: 4728/10000 (47.28%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if B >= 90 and C >= 20 and E >= 10:
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
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                if A < 20:
                    return 3
                else:
                    return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                if E > 80:
                    return 4
                elif D < 40 and E < 30:
                    return 1
                else:
                    return 3