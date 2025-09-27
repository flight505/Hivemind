"""
Predictor 81
Generated on: 2025-09-09 19:50:47
Accuracy: 57.13%
"""


# PREDICTOR 81 - Accuracy: 57.13%
# Correct predictions: 5713/10000 (57.13%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if E > 60:
                    return 4
                else:
                    return 1
            else:
                if E < 20:
                    if A < 20:
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
                if D > 90:
                    return 3
                elif E <= 35 or A > 60 or E > 80:
                    return 1
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if A > 90 or D > 50:
                    return 1
                else:
                    if D < 20:
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
                        if D > 80 and E > 80:
                            return 1
                        elif D > 80 and E < 70:
                            return 3
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
                    if B > 70:
                        return 3
                    else:
                        return 1
                else:
                    return 3
            else:
                if E > 45 and D < 40:
                    if C < 5:
                        return 4
                    elif E > 80:
                        return 2
                    else:
                        return 1
                elif D > 50:
                    if E <= 40:
                        return 1
                    elif B < 40:
                        if E > 70:
                            return 4
                        elif A < 10:
                            return 2
                        elif C < 10:
                            return 4
                        else:
                            return 1
                    else:
                        if A > 80 or C < 20 or E > 80:
                            return 3
                        else:
                            return 1
                else:
                    if C > 20:
                        if E > 70:
                            return 2
                        else:
                            return 1
                    else:
                        if E > 70:
                            return 4
                        else:
                            return 3