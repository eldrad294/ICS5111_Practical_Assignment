class json_formatter():
    #
    def __init__(self):
        pass
    #
    def suggested_businesses_to_json(self, sql_cursor, path):
        """ Takes the sql cursor and formats it into a json string and saves it """
        json_string = "{\"businesses\":["
        for i, tuple in enumerate(sql_cursor):
            for json in tuple:
                if i == 0:
                    json_string += json
                else:
                    json_string += ',' + json
        json_string += ']}'
        self.save_json_to_path(json_string, path)
    #
    def business_cluster_to_json(self, sql_cursor, path):
        """ Takes the sql cursor and formats it into a json string and saves it """
        json_string = "{"
        for i, tuple in enumerate(sql_cursor):
            for json in tuple:
                if i == 0:
                    json_string += "\"" + str(i) + "\":" + json
                else:
                    json_string += ",\"" + str(i) + "\":" + json
        json_string += "}"
        self.save_json_to_path(json_string, path)
    #
    def save_json_to_path(self, json_string, path):
        """ Takes the json string and saves it to file """
        with open(path, 'w') as f:
            f.write(json_string)