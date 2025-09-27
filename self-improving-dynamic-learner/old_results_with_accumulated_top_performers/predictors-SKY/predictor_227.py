"""
Predictor 227
Generated on: 2025-09-09 09:09:49
Accuracy: 60.23%
"""


# PREDICTOR 227 - Accuracy: 60.23%
# Correct predictions: 6023/10000 (60.23%)

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
                if D > 80 and E > 60 and B < 15:
                    return 4
                else:
                    return 3
        else:
            if D > 80 and E > 60 and B < 15:
                return 4
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
                        return 4
                    else:
                        return 3
            else:
                if E < 40 and B < 30:
                    return 4
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
        elif A > 80 and C < 25 and D > 90 and E < 20:
            return 4
        elif E < 40 and C < 20 and (A > 50 or B < 20):
            return 3
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
        elif E > 80 and C < 30 and B > 30:
            return 4
        else:
            return 1
    else:
        if E < 15 and A > 40 and C < 30:
            return 4
        if C < 50 and D > 70 and E > 10 and B > 40:
            return 3
        if B > 60:
            if E > 80:
                if D < 30:
                    return 4
                else:
                    return 2
            if E < 20:
                if A > 80:
                    return 2
                else:
                    return 1
            if A > 70 and C < 50:
                return 2
            elif C > 60:
                if A < 50:
                    if D < 10:
                        return 1
                    else:
                        return 2
                else:
                    return 1
            else:
                if D < 30 and E > 70 and C > 55:
                    return 4
                elif D < 20:
                    return 1
                elif C < 60 and E < 50:
                    return 1
                else:
                    return 3
        elif B < 20:
            if C > 50 and A < 50 and D < 50:
                return 4
            else:
                return 1
        elif D >= 90 and (B > 60 or C > 50):
            return 3
        elif A > 70 and B < 40 and E > 70:
            return 3
        else:
            return 1