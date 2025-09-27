"""
Predictor 20
Generated on: 2025-09-09 19:07:34
Accuracy: 54.76%
"""


# PREDICTOR 20 - Accuracy: 54.76%
# Correct predictions: 5476/10000 (54.76%)

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
                if D > 90:
                    if E < 25:
                        return 1
                    else:
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
                    if C > 70:
                        return 2
                    else:
                        return 4
                else:
                    if B >= 75:
                        return 2
                    else:
                        return 1
        else:
            if E < 20:
                if D > 50:
                    if C > 30:
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
                    if E > 60 and B < 60:
                        return 2
                    elif C > 20:
                        return 1
                    else:
                        return 3