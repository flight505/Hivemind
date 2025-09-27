"""
Predictor 69
Generated on: 2025-09-09 19:43:32
Accuracy: 54.70%
"""


# PREDICTOR 69 - Accuracy: 54.70%
# Correct predictions: 5470/10000 (54.70%)

def predict_output(A, B, C, D, E):
    if B >= 70:
        if C >= 50:
            if D > 80:
                return 3
            elif A > 50:
                return 1
            else:
                return 2
        else:
            if D < 40:
                return 1
            else:
                if E > 80 and C > 40:
                    return 3
                else:
                    return 4
    else:
        if C >= 50:
            if D < 30:
                return 4
            else:
                return 1
        else:
            if E >= 60:
                if A > 90 and C > 25:
                    return 3
                elif D > 50:
                    return 4
                elif B > 60:
                    return 1
                else:
                    return 4
            else:
                if E < 20:
                    return 1
                else:
                    return 3