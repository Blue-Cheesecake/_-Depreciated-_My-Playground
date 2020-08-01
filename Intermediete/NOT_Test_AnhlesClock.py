# output must not exceed 180


def Solution(hour=int, minutes=int):
    minDegrees = minutes * 6
    houDegrees = hour * 30
    yPer = (minutes * 100) / 60
    houDegrees += (yPer * 30) / 100
    minDegrees = min(minDegrees, 360 - minDegrees)
    if hour != 12:
        houDegrees = min(houDegrees, 360 - houDegrees)
    else:
        houDegrees = min(houDegrees, 390 - houDegrees)
    return max(minDegrees, houDegrees) - min(minDegrees, houDegrees)


print(Solution(12, 30))
print(Solution(4, 45))
