class json_formatter():
    #
    def __init__(self, path):
        self.path = path
    #
    def suggested_businesses_to_json(self, sql_cursor):
        """ Takes the sq; cursor and formats it into a json string and saves it """
        print(sql_cursor)
        json_string = "{\"businesses\":["
        for i, tuple in enumerate(sql_cursor):
            for json in tuple:
                if i == 0:
                    json_string += json
                else:
                    json_string += ',' + json
        json_string += ']}'
        self.save_json_to_path(json_string, self.path)
    #
    def save_json_to_path(self, json_string, path):
        """ Takes the json string and saves it to file """
        with open(path, 'w') as f:
            f.write(json_string)