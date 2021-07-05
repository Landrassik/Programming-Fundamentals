import sys
n_line = int(input())

max_snowball = -sys.maxsize
snowball_snow1 = 0
snowball_time2 = 0
snowball_quality3 = 0


for i in range(1,n_line + 1):

    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_volume = (snowball_snow / snowball_time) ** snowball_quality

    if snowball_volume > max_snowball:
        max_snowball = snowball_volume
        snowball_volume = 0
        snowball_snow1 = snowball_snow
        snowball_time2 = snowball_time
        snowball_quality3 = snowball_quality
else:
    print(f"{snowball_snow1} : {snowball_time2} = {int(max_snowball)} ({snowball_quality3})")