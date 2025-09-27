"""
Predictor 218
Generated on: 2025-09-09 21:03:09
Accuracy: 37.08%
"""


# PREDICTOR 218 - Accuracy: 37.08%
# Correct predictions: 3708/10000 (37.08%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D > 40:
                return 4
            else:
                return 1
        else:
            if D < 50:
                if A < 10:
                    return 1
                else:
                    return 4
            else:
                return 2
    else:
        if C >= 50:
            if B < 40:
                return 4
            else:
                return 1
        else:
            if E < 20:
                if B >= 60:
                    return 4
                elif A > 50:
                    return 1
                else:
                    return 3
            else:
                if B >= 70 or C > 40:
                    return 4
                else:
                    if A < 20:
                        return 1
                    else:
                        return 3