"""
Predictor 48
Generated on: 2025-09-09 19:27:24
Accuracy: 55.80%
"""


# PREDICTOR 48 - Accuracy: 55.80%
# Correct predictions: 5580/10000 (55.80%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E < 20:
                    if B > 80 and C > 40:
                        return 2
                    elif A < 20:
                        return 1
                    else:
                        return 4
                elif E > 50:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 1
            else:
                if E <= 25 or A > 60 or E > 80:
                    return 1
                elif D > 90:
                    return 3
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if B >= 75:
                    return 2
                elif A > 90 or D > 50:
                    return 1
                else:
                    return 4
            else:
                if D < 20:
                    if A < 50:
                        return 2
                    elif E < 30:
                        return 3
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
                        return 2
                elif D > 50:
                    if E <= 40:
                        if C < 20 and D > 60:
                            return 4
                        else:
                            return 1
                    elif B < 40:
                        if E > 70:
                            return 2
                        else:
                            return 1
                    else:
                        if A > 80 or C < 20:
                            return 3
                        else:
                            return 1
                else:
                    if C > 20:
                        if D < 25 and E < 40:
                            return 3
                        elif E > 70:
                            return 2
                        else:
                            return 1
                    else:
                        if E > 70:
                            return 4
                        else:
                            return 3