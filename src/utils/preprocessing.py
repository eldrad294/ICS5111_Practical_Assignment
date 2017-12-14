class Preprocessing():
    #
    def __init__(self):
        pass
    #
    def normalize(self, data):
        """ Takes a dataset (python list/tuple) and normalizes it """
        x_min, x_max = min(data), max(data)
        normalize = lambda x : (x - x_min) / (x_max - x_min)
        normalized_data = []
        [(normalized_data.append(normalize(float(x)))) for x in data]
        return normalized_data
