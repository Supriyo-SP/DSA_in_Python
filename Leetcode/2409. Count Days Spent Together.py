class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def dayCount(date):
            l = date.split("-")
            month = int(l[0])
            day = int(l[1])
            total_days = 0
            for i in range(month - 1):
                total_days += days_in_months[i]
            total_days += day
            return total_days
        alicearrive = dayCount(arriveAlice)
        bobarrive = dayCount(arriveBob)
        aliceleave = dayCount(leaveAlice)
        bobleave = dayCount(leaveBob)
        latestarrival = max(alicearrive, bobarrive)
        earlyleave = min(aliceleave, bobleave)
        if latestarrival <= earlyleave:
            return earlyleave - latestarrival + 1
        else:
            return 0
        