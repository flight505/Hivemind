"""
Predictor 319
Generated on: 2025-09-09 21:48:45
Accuracy: 54.07%
"""


# PREDICTOR 319 - Accuracy: 54.07%
# Correct predictions: 5407/10000 (54.07%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                return 4
        else:
            return 2
    else:
        if C > 50:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                return 1
        elif C > 40:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    if A > 80:
                        return 1
                    else:
                        return 3
            else:
                if E < 30:
                    return 3
                elif D > 50:
                    return 1
                else:
                    return 4
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    if A > 80:
                        return 1
                    else:
                        return 3
            else:
                if B > 60:
                    if C < 10:
                        return 4
                    elif E < 30:
                        return 3
                    else:
                        return 1
                else:
                    if E > 70:
                        return 4
                    else:
                        return 3