"""
Predictor 14
Generated on: 2025-09-09 19:03:14
Accuracy: 49.45%
"""


# PREDICTOR 14 - Accuracy: 49.45%
# Correct predictions: 4945/10000 (49.45%)

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
                if D < 20:
                    if B > 50:
                        return 1
                    else:
                        return 4
                else:
                    if B >= 75:
                        return 2
                    elif C > 60 and E < 40:
                        return 4
                    elif C < 70 and D > 70 and E > 70:
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
                if E > 45 and D < 40:
                    if D < 15:
                        return 2
                    elif E > 65:
                        return 1
                    else:
                        return 4
                elif D > 50:
                    if E > 70:
                        return 1
                    else:
                        return 3
                else:
                    if C > 20:
                        return 1
                    else:
                        return 3