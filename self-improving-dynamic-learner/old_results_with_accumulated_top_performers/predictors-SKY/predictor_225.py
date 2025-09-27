"""
Predictor 225
Generated on: 2025-09-09 09:06:31
Accuracy: 55.39%
"""


# PREDICTOR 225 - Accuracy: 55.39%
# Correct predictions: 5539/10000 (55.39%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if B > 50:
            if E > 60:
                return 4
            elif E < 20:
                return 1
            else:
                if D > 80:
                    return 4
                if B > 90:
                    return 1
                if E < 50 and D < 30:
                    return 1
                return 3
        else:
            if D > 80 and E > 60 and B < 15:
                return 4
            if D > 80 and E > 60:
                return 2
            elif D > 90 and E < 20:
                return 1
            elif E > 50:
                return 4
            else:
                return 3
    if C >= 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                if D > 90:
                    return 3
                if C > 80:
                    return 4
                if E < 30 and D < 20:
                    return 4
                elif E < 20:
                    return 2
                elif A < 20:
                    return 1
                else:
                    return 2
        else:
            if D < 20:
                if B < 20:
                    if A >= 50:
                        return 4
                    else:
                        return 3
                elif E > 50:
                    if C < 85:
                        return 1
                    else:
                        return 2
                else:
                    if C > 85 and E < 40:
                        return 3
                    else:
                        return 3
            else:
                if E < 40 and B < 30:
                    return 4
                else:
                    return 1
            if C > 80 and A < 30:
                return 4
            elif A > 70:
                return 3
            else:
                return 1
    if C < 40:
        if A > 50 and C < 25 and E > 80 and B > 20:
            return 4
        elif A > 40 and E > 50 and C < 30 and B > 20 and B < 60:
            return 4
        elif C < 25 and E > 70 and B > 20:
            return 4
        elif B > 50 and C < 35 and E > 70 and A > 20:
            return 4
        elif D > 90:
            return 3
        elif E > 70 and B < 40:
            return 4
        elif C < 35 and D < 25 and A < 60 and B < 50:
            return 3
        elif C > 30 and C < 40 and D > 90:
            return 3
        elif D > 60 and E < 10 and B > 50 and C < 15:
            return 4
        elif D < 20 and E < 20:
            return 3
        elif E > 60 and B > 70 and C > 50:
            return 2
        elif B > 50 and E < 40:
            if D > 80:
                return 4
            elif D < 70:
                return 1
            else:
                return 3
        else:
            return 1
    else:
        if D > 90:
            return 3
        elif B > 90:
            return 2
        elif C > 80 and B < 10:
            return 1
        elif C > 80 and E < 5:
            return 1
        elif A > 70:
            return 3
        else:
            return 1