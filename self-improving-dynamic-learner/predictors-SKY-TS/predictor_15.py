"""
Predictor 15
Generated on: 2025-09-09 19:03:14
Accuracy: 44.01%
"""


# PREDICTOR 15 - Accuracy: 44.01%
# Correct predictions: 4401/10000 (44.01%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E < 20 or E > 50:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 1
            else:
                if E < 20:
                    return 1
                elif D > 90:
                    return 3
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if A > 90 or D > 50:
                    return 1
                else:
                    return 4
            else:
                if D < 40:
                    if B > 60 and E > 70:
                        return 1
                    else:
                        return 4
                else:
                    if C >= 70:
                        return 1
                    else:
                        return 3
        else:
            if D < 20 and C > 40:
                return 2
            elif B < 25:
                if D > 50 or E > 60:
                    return 1
                else:
                    return 3
            else:
                return 3