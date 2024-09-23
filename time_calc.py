from single_threading import single
from multi_threading import multiple
import requests
import json
from collections import Counter
import datetime

if __name__ == "__main__":
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
        "cache-control" : "no-cache",
        "accept-encoding" : "gzip, deflate, br, zstd",
        "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    url = "https://api.spacexdata.com/v4/ships"

    res = requests.get(url=url, headers=headers, verify=True)

    json_lst = json.loads(res.text)

    t1 = single()
    t2 = multiple()

    time1 = datetime.datetime.now()
    lst1 = t1.get_data_name(json_lst)
    time2 = datetime.datetime.now()

    time_length_1 = time2 - time1

    time3 = datetime.datetime.now()
    lst2 = t2.get_data_name(json_lst)
    time4 = datetime.datetime.now()

    time_length_2 = time4 - time3

    print(Counter(lst1))
    print(Counter(lst2))
    print(Counter(lst1) == Counter(lst2))

    print(time_length_1)
    print(time_length_2)
    '''在python中使用多线程反而慢
    在Python中使用多线程反而慢的情况通常发生在I/O密集型任务中,
    因为Python的全局解释器锁(GIL)限制了线程的并行执行。当线程在执行I/O操作时,
    GIL会被释放,从而允许其他线程执行。但是,当线程在执行计算密集型操作时,
    GIL不会被释放,导致线程无法并行执行。'''