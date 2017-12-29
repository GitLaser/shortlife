def series_sum(n):
    # Happy Coding ^_^
    if n==0:
        return "%.2f" % 0
    sum=0.00

    for i in range(1,n):
        sum+=1/(i*3+1)
        print(sum)
    s=sum + 1
    return "%.2f" % s