"""
Predictor 23
Generated on: 2025-09-09 19:09:45
Accuracy: 47.40%
"""


# PREDICTOR 23 - Accuracy: 47.40%
# Correct predictions: 4740/10000 (47.40%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if E < 50:
                    return 1
                else:
                    return 4
            else:
                if E < 20 or E > 50:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                if C > 60:
                    return 2
                else:
                    return 1
            else:
                if E <= 25:
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
                    if A < 50:
                        return 2
                    else:
                        return 4
                else:
                    if B >= 75:
                        return 2
                    else:
                        if C >= 70:
                            return 1
                        else:
                            return 3
        else:
            if E < 20:
                if D > 50:
                    if B > 50:
                        return 3
                    else:
                        return 1
                else:
                    return 3
            else:
                if E > 50 and D < 40:
                    return 4
                elif D > 50:
                    if E <= 40:
                        return 1
                    elif B < 40:
                        return 1
                    else:
                        return 3
                else:
                    if C > 20:
                        if E > 70:
                            return 2
                        else:
                            return 1
                    else:
                        return 3