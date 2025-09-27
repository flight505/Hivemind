"""
Predictor 46
Generated on: 2025-09-09 19:27:24
Accuracy: 54.25%
"""


# PREDICTOR 46 - Accuracy: 54.25%
# Correct predictions: 5425/10000 (54.25%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E < 20:
                    if A < 20:
                        return 1
                    elif D < 70:
                        return 2
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
                    if E < 30:
                        return 3
                    elif A < 50:
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
                    elif B > 40:
                        return 2
                    else:
                        return 1
                elif D > 50:
                    if E <= 40:
                        if C < 20:
                            return 4
                        else:
                            return 1
                    elif B < 40:
                        if A > 20:
                            return 4
                        else:
                            return 2
                    else:
                        if A > 80 or C < 20:
                            return 3
                        else:
                            return 1
                else:
                    if C > 20:
                        if E > 70:
                            return 2
                        elif B > 20 and E > 50:
                            return 2
                        elif D < 25:
                            return 3
                        else:
                            return 1
                    else:
                        if A > 80:
                            return 4
                        elif B > 40:
                            return 2
                        else:
                            return 3