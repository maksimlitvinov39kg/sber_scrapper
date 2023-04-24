import json
import yaml

def json_read(filename, format="json"):
        dict = {}
        if (format == "json"):
            with open(filename) as f:
                dict = json.load(f)
        elif (format == "yaml"):
            with open(filename) as f:
                dict = yaml.safe_load(f)
        else:
            raise ValueError("Неверный ввод :(")
        return dict

class Data:
    def __init__(self, dict):
        self.dict = dict

    def dict_rewrite(self,_dict):
        to_print = []
        _dict = dict(sorted(_dict.items(), key=lambda x: x[1]))
        for key, value in _dict.items():
            to_print.append(f"Модель: {key} Цена: {value}")
        return(to_print)


    def grouping_cheap(self):
        print("Модели в ценовой категории до 50000:")
        cheap = {}
        for key, value in self.dict.items():
            if (value <= 50000):
                cheap[key] = value
        return('\n'.join(self.dict_rewrite(cheap)))

    def grouping_average(self):
        print("\nМодели в ценовой категории от 50000 до 80000:")
        average = {}
        for key, value in self.dict.items():
            if (value > 50000) and (value <= 80000):
                average[key] = value
        return('\n'.join(self.dict_rewrite(average)))

    def grouping_expensive(self):
        print("\nМодели в ценовой категории свыше 80000:")
        expensive = {}
        for key, value in self.dict.items():
            if (value > 80000):
                expensive[key] = value
        return('\n'.join(self.dict_rewrite(expensive)))

    def find_by_color(self, color):
        print(f"\nМодели цвета {color}:")
        names = []
        color = color[0].upper() + color[1:]
        for key in self.dict.keys():
            if key.find(color) != -1:
                names.append(f"Модель: {key} Цена: {self.dict[key]}")
        if len(names) == 0:
            return ("Такого цвета нет")
        else:
            return " \n".join(names)
