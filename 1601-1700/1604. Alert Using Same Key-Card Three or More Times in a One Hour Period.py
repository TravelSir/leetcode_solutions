"""
解题思路：
这题有点小坑，不把题意说明。给的数据全是一天内的打开记录且无时间顺序这个是重点,所以先分组排序再做
的基础判断逻辑为：就是一小时内记录名字出现的频率。那么如何判断一小时呢，其实很简单。
假设一个员工打卡时间为a,b,c,d
那么b-a, c-b 两个时间间隔加起来小于一小时则说明一小时内出现了三次。那其实就是一个滑动窗口


"""
import datetime
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_times = dict()
        result = list()
        for i in range(len(keyTime)):
            _time = datetime.datetime.strptime(keyTime[i], '%H:%M')
            if keyName[i] in name_times:
                name_times[keyName[i]].append(_time)
            else:
                name_times[keyName[i]] = [_time]

        for k in name_times:
            if len(name_times[k]) < 3:
                continue
            name_times[k].sort()
            left = name_times[k][1] - name_times[k][0]
            for i in range(2, len(name_times[k])):
                right = name_times[k][i] - name_times[k][i-1]
                if left + right <= datetime.timedelta(hours=1):
                    result.append(k)
                    break
                left = right
        result.sort()
        return result


if __name__ == '__main__':
    key_name = ["a", "a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c"]
    key_time = ["00:37", "11:24", "14:35", "21:25", "15:48", "20:28", "07:30", "09:26", "10:32", "20:10", "19:26", "08:13",
     "01:08", "15:49", "02:34", "06:48", "04:33", "07:18", "00:05", "06:44", "13:33", "04:12", "03:54"]
    print(Solution().alertNames(key_name, key_time))
