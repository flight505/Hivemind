"""
Predictor 17
Generated on: 2025-09-09 19:07:34
Accuracy: 56.25%
"""


# PREDICTOR 17 - Accuracy: 56.25%
# Correct predictions: 5625/10000 (56.25%)

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
            elif E < 25:
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
                    if A > 50:
                        return 4
                    else:
                        return 2
                else:
                    if B >= 75:
                        return 2
                    else:
                        return 1
        else:
            if E < 20:
                if D > 50:
                    if B > 60:
                        return 3
                    else:
                        return 1
                else:
                    return 3
            else:
                if E > 45 and D < 40:
                    return 4
                elif D > 50:
                    if B + E > 95:
                        return 3
                    else:
                        return 1
                else:
                    if E > 70 and B > 50 and D > 40:
                        return 2
                    elif C > 20:
                        return 1
                    else:
                        return 3