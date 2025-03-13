def solution(n, times):
    times.sort()
    time_max = n * times[-1]
    time_min = times[0]
    while time_min < time_max:
        new_time_avg = (time_min + time_max) // 2
        cnt = 0
        for i in times:
            cnt += new_time_avg //i

        if cnt >= n:
            time_max = new_time_avg
        else:
            time_min = new_time_avg+1


    return time_min


print(solution(6,[7,10]))
print(solution(8,[3,7,5,4,2,10]))