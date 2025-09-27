"""
Predictor 38
Generated on: 2025-09-09 19:22:19
Accuracy: 57.20%
"""


# PREDICTOR 38 - Accuracy: 57.20%
# Correct predictions: 5720/10000 (57.20%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if A < 20 and E < 25:
                    return 3
                else:
                    return 1
            else:
                if E < 20:
                    if E < 10:
                        return 4
                    else:
                        return 1
                elif E > 50:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 1
            else:
                if E <= 25 or A > 60 or (C > 70 and E > 75):
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
                        if D > 80 and E > 80:
                            return 1
                        else:
                            return 2
                    else:
                        if D < 30 and E < 30 and C > 70:
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
                if E > 45 and D < 40:
                    if C < 5:
                        return 4
                    else:
                        return 1
                elif D > 50:
                    if E <= 40:
                        return 1
                    elif B < 40:
                        return 1
                    else:
                        if E > 60:
                            return 3
                        elif C > 30:
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