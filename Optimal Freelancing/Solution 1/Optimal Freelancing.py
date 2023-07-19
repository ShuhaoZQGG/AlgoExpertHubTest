import math
def optimalFreelancing(jobs):
    # Write your code here.
    totalPayment = 0
    minimumPayment = math.inf
    days = 1
    sortedJobs = sorted(jobs, key=custom_sort_key)
    print(sortedJobs)
    for job in sortedJobs:
        print(job)
        print(days)
        minimumPayment = min(minimumPayment, job["payment"])
        if job["deadline"] >= days and days <= 7:
            totalPayment += job["payment"]
            print(totalPayment)
            days += 1
        elif job["payment"] >= minimumPayment:
            totalPayment = totalPayment - minimumPayment + job["payment"]
            minimumPayment = job["payment"]
    return totalPayment
def custom_sort_key(obj):
    return (obj["deadline"], -obj["payment"]) 