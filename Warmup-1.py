def sleep_in(weekday, vacation):
    if(not weekday or vacation):
        return "Sleep tight."
    else:
        return "You can't sleep Jia Rani!"


def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2

