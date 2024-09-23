class single:
    
    def get_data_name(self, json: list) -> list:

        lst = []

        for ele in json:
            lst.append(ele["name"])

        return lst