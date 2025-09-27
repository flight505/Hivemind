"""
Predictor 34
Generated on: 2025-09-09 19:16:43
Accuracy: 41.73%
"""


# PREDICTOR 34 - Accuracy: 41.73%
# Correct predictions: 4173/10000 (41.73%)

def predict_output(A, B, C, D, E):
    if B >= 75:
        if C < 50:
            if D + E > 60:
                return 4
            else:
                return 1
        else:
            if D > 80 and E > 80:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if D > 50:
                return 1
            else:
                if E > 50:
                    return 2
                else:
                    return 4
        else:
            if E < 20:
                if B > 50:
                    return 4
                else:
                    return 1
            else:
                if D > 80:
                    return 1
                elif C > 30 and D < 20:
                    return 2
                elif D < 30 and E > 60:
                    if B > 55:
                        return 1
                    else:
                        return 2
                else:
                    return 3