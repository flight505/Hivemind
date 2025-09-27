"""
Predictor 80
Generated on: 2025-09-09 19:47:41
Accuracy: 57.84%
"""


# PREDICTOR 80 - Accuracy: 57.84%
# Correct predictions: 5784/10000 (57.84%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if E > 30:
                    return 4
                else:
                    return 1
            else:
                if D + E > 100:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                if E > 70:
                    return 4
                else:
                    return 1
            else:
                if E <= 25 or A > 60 or E > 80:
                    return 1
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if D >= 45:
                    return 1
                else:
                    return 4
            else:
                if D < 20:
                    if B > 50:
                        return 2
                    else:
                        return 3
                else:
                    return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                elif A > 50:
                    return 1
                else:
                    return 3
            else:
                if E > 80:
                    return 4
                elif E < 30:
                    return 3
                else:
                    if B < 30:
                        if D < 50:
                            if E > 60:
                                return 4
                            else:
                                return 3
                        else:
                            return 1
                    else:
                        if D > 50:
                            if B >= 70:
                                return 2
                            else:
                                return 3
                        else:
                            if E > 70:
                                return 4
                            else:
                                return 1