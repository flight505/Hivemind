"""
Predictor 25
Generated on: 2025-09-09 19:11:25
Accuracy: 56.25%
"""


# PREDICTOR 25 - Accuracy: 56.25%
# Correct predictions: 5625/10000 (56.25%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if A < 30:
                    return 3
                else:
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
                        if D > 80 or E > 80:
                            return 1
                        else:
                            return 2
                    else:
                        if D < 40 and E < 30:
                            return 4
                        else:
                            return 1
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
                if E > 45 and D < 40 and C < 40:
                    return 4
                elif D > 50:
                    if E <= 40:
                        return 1
                    elif B < 40:
                        if A < 20:
                            return 2
                        else:
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