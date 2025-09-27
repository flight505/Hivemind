"""
Predictor 244
Generated on: 2025-09-09 11:04:19
Accuracy: 55.16%
"""


# PREDICTOR 244 - Accuracy: 55.16%
# Correct predictions: 5516/10000 (55.16%)

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
                else:
                    return 3
        else:
            if D > 80 and E > 60 and B < 25:
                return 4
            elif D > 90:
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
    if 40 <= C < 70:
        if D > 80:
            return 3
        elif A < 10 and C > 50:
            return 3
        elif B < 5 and C > 60:
            return 4
        elif B > 60 and C > 40:
            return 2 if A < 70 else 1
        else:
            return 1
    if C < 40:
        if A > 80 and E > 70:
            return 1
        if A < 10 and B < 10:
            return 2
        if B < 20 and C < 25 and A > 60:
            return 3
        if B > 50 and C < 25 and D < 5 and E > 45:
            return 3
        if B > 80 and D > 90 and E > 70:
            return 3
        if A > 80 and E > 80:
            return 4
        if C < 25 and D > 50 and E > 70:
            return 4
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
            else:
                return 3
        elif E > 80 and C < 30 and B > 30:
            return 4
        else:
            return 1
    else:
        if C >= 70:
            if B > 60:
                if A >= 50:
                    return 1
                else:
                    if C > 90 and D > 90:
                        return 3
                    if C > 80 and D < 20 and E > 90:
                        return 4
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
        return 1