"""
Predictor 169
Generated on: 2025-09-09 20:39:19
Accuracy: 57.16%
"""


# PREDICTOR 169 - Accuracy: 57.16%
# Correct predictions: 5716/10000 (57.16%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if E > 80:
                    return 4
                else:
                    return 1
            else:
                if D > 70 and 40 <= E <= 55:
                    return 1
                elif D > 90 and E > 70:
                    return 1
                elif E < 20 or E > 50:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 2
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
                    if A > 80:
                        return 1
                    else:
                        return 4
                else:
                    return 1
        else:
            if E < 20:
                if D > 50:
                    if B > 50:
                        return 3
                    else:
                        if E < 5:
                            return 4
                        else:
                            return 1
                else:
                    if A > 50:
                        return 1
                    else:
                        if E < 10:
                            return 4
                        else:
                            return 3
            else:
                if E > 45 and D < 40:
                    return 4
                elif D > 50:
                    if E <= 40:
                        if C < 10:
                            return 3
                        else:
                            return 1
                    elif B < 40:
                        if C > 10 and A > 80 and E > 50:
                            return 3
                        else:
                            return 1
                    else:
                        if C < 5 and E > 50:
                            return 4
                        else:
                            return 3
                else:
                    if E > 70:
                        if C >= 20:
                            if B > 40:
                                if A > 70:
                                    return 1
                                else:
                                    return 4
                            else:
                                return 2
                        else:
                            return 4
                    elif C > 20:
                        return 1
                    else:
                        return 3