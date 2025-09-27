"""
Predictor 16
Generated on: 2025-09-09 19:03:14
Accuracy: 37.64%
"""


# PREDICTOR 16 - Accuracy: 37.64%
# Correct predictions: 3764/10000 (37.64%)

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
                    if A > 90:
                        return 1
                    else:
                        return 4
                else:
                    if C > 80:
                        if D >= 70 and E >= 70:
                            return 1
                        else:
                            return 4
                    elif D >= 70 and E >= 70:
                        return 3
                    elif B >= 75:
                        return 2
                    else:
                        return 4
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                if E > 45 and D < 40:
                    if A < 50:
                        return 2
                    else:
                        return 1
                elif D > 50:
                    if B < 30:
                        return 1
                    else:
                        return 3
                else:
                    if C > 20:
                        return 1
                    else:
                        return 3