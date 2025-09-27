"""
Predictor 39
Generated on: 2025-09-09 19:22:19
Accuracy: 31.46%
"""


# PREDICTOR 39 - Accuracy: 31.46%
# Correct predictions: 3146/10000 (31.46%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            if E > 75:
                return 1
            else:
                return 2
        else:
            if D < 40:
                return 1
            else:
                if C < 10:
                    return 1
                else:
                    return 4
    else:
        if C > 50:
            if D + E > 150:
                return 1
            else:
                return 4
        else:
            if E < 20:
                if D < 50:
                    return 3
                else:
                    if B > 60:
                        return 3
                    else:
                        return 1
            else:
                if B > 70:
                    if D < 10:
                        return 4
                    else:
                        return 1
                else:
                    if (D < 20 and E > 45) or (C > 32 and D > 80):
                        return 1
                    else:
                        return 3