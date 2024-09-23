from concurrent.futures import ThreadPoolExecutor
import threading

class multiple:

    def x(self, lst: list, string: str):
        lst.append(string)


    def get_data_name(self, json: list) -> list:

        lst = []

        with ThreadPoolExecutor(max_workers=len(json)) as executor:
            mutex = threading.Lock()
            for ele in json:
                mutex.acquire()
                executor.submit(self.x, lst, ele["name"])
                mutex.release()

        return lst
