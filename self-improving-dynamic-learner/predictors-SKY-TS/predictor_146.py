"""
Predictor 146
Generated on: 2025-09-09 20:25:36
Accuracy: 61.89%
"""


# PREDICTOR 146 - Accuracy: 61.89%
# Correct predictions: 6189/10000 (61.89%)

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
                        if D > 50:
                            return 4
                        else:
                            return 2
                    else:
                        if A < 20:
                            return 1
                        else:
                            return 4
                elif E > 50 and C < 40:
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
                    if E < 20:
                        return 1
                    else:
                        return 3
                elif E <= 25 or A > 60 or E > 80:
                    return 1
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if B >= 70:
                    return 1
                else:
                    if A > 90 or D > 50:
                        return 1
                    elif D < 20 and E < 10:
                        return 1
                    else:
                        return 4
            else:
                if D < 20:
                    if A < 50:
                        return 2
                    elif E < 30:
                        return 3
                    elif E > 50:
                        return 1
                    else:
                        return 4
                else:
                    if B >= 75:
                        if D > 80 and E > 80:
                            return 1
                        else:
                            return 2
                    else:
                        if D < 30 and E < 30 and C > 70 and B < 75:
                            return 4
                        else:
                            return 1
        else:
            if E < 20:
                if D > 50:
                    if B > 50 or C < 10:
                        if D > 90:
                            return 4
                        else:
                            return 3
                    else:
                        return 1
                else:
                    if C > 40:
                        return 4
                    elif A > 50:
                        return 1
                    else:
                        return 3
            else:
                if B > 50 and C >= 50 and D < 50 and E < 30:
                    return 2
                elif E > 45 and D < 40:
                    if E > 70:
                        return 4
                    elif C < 5:
                        return 4
                    elif B > 40:
                        return 1
                    else:
                        return 2
                elif D > 50:
                    if E <= 40:
                        if B < 50 and C < 20:
                            return 4
                        else:
                            return 1
                    elif B < 40:
                        if A < 10:
                            return 2
                        elif C < 10:
                            return 4
                        else:
                            return 1
                    else:
                        if C < 20:
                            if E < 50:
                                return 4
                            else:
                                return 1
                        elif A > 80 or C < 20:
                            return 3
                        else:
                            return 1
                else:
                    if C > 20:
                        if E > 70:
                            return 2
                        else:
                            if D < 25 and E < 40:
                                return 3
                            elif D < 40 and E < 50:
                                return 4
                            else:
                                return 1
                    else:
                        if E > 70:
                            return 4
                        else:
                            return 3