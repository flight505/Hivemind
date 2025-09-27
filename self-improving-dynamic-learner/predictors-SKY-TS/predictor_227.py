"""
Predictor 227
Generated on: 2025-09-09 21:06:49
Accuracy: 52.49%
"""


# PREDICTOR 227 - Accuracy: 52.49%
# Correct predictions: 5249/10000 (52.49%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if E > 50:
                    return 4
                else:
                    return 1
            else:
                if E < 20:
                    if C < 20:
                        return 4
                    elif A < 10:
                        return 4
                    else:
                        return 2
                elif E > 50:
                    return 4
                else:
                    if E < 40:
                        return 1
                    else:
                        return 2
        else:
            if D < 50:
                if E > 80:
                    return 4
                else:
                    return 1
            else:
                if D > 90:
                    return 3
                elif E <= 25 or A > 60 or E > 80:
                    return 1
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if B >= 70:
                    return 2
                else:
                    if D < 5:
                        return 3
                    elif A > 80 and D < 40:
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
                        return 2
                    else:
                        return 1
        else:
            if E < 20:
                if D > 50:
                    if B > 50 and C > 20:
                        return 3
                    else:
                        return 1
                else:
                    return 3
            else:
                if D > 50:
                    if E <= 40:
                        return 1
                    elif B < 40:
                        return 3
                    else:
                        if C < 50 and E > 65:
                            return 1
                        else:
                            return 3
                elif E > 45 and D < 40 and B > 40:
                    return 4
                else:
                    if C <= 20:
                        if E < 50:
                            return 3
                        else:
                            return 2
                    else:
                        if E > 70 and (C >= 50 or B >= 40):
                            return 2
                        elif D < 25 and E < 40 and B < 20:
                            return 3
                        else:
                            return 1