"""
Predictor 228
Generated on: 2025-09-09 21:06:49
Accuracy: 55.99%
"""


# PREDICTOR 228 - Accuracy: 55.99%
# Correct predictions: 5599/10000 (55.99%)

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
                    if C > 40:
                        return 2
                    else:
                        if E < 5:
                            return 2
                        elif A < 20:
                            return 4
                        else:
                            return 1
                elif E > 50:
                    return 4
                else:
                    if E < 40:
                        return 1
                    else:
                        return 2
        else:
            if D < 50:
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
                    if A > 80 or D > 50:
                        return 1
                    else:
                        if D < 10:
                            return 3
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
                    if B > 50:
                        if B > 70:
                            return 1
                        else:
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
                        if E > 60:
                            return 1
                        else:
                            return 3
                elif E > 45 and D < 40:
                    return 4
                else:
                    if C > 20:
                        if E > 70:
                            if B < 50:
                                return 1
                            else:
                                return 2
                        elif D < 25 and E < 40 and B < 50:
                            return 3
                        else:
                            return 1
                    else:
                        return 3