import json

# with open('menu_data.json', "r") as json_file:
#     data = json.load(json_file)
#     for x in data.values():
#         for y in x.values():
#             print(y["items"])
#     print(data["menu"]["breakfast"]["items"])

# with open("menu_data.json", "w") as json_file:

class MenuManager:
    def __init__(self, file_path):
        self.menu_data = self.load_menu(file_path)

    def load_menu(self, file_path):
        with open(file_path, 'r') as file:
            menu_data = json.load(file)
        return menu_data

    def display_meal_items(self, meal_time):
        try:
            items = []
            for x in self.menu_data.values():
                for y in x.values():
                    items.append(y)
            print(items)
            print(f"\n{meal_time.capitalize()} Menu:")
            for item in items:
                print(f"{item['name']}: ${item['price']:.2f}")
        except KeyError:
            print(f"\nNo menu found for {meal_time.capitalize()}.")

if __name__ == "__main__":
    file_path = "menu_data.json"
    menu_manager = MenuManager(file_path)

    user_input = input("Enter the meal time (breakfast, lunch, or dinner): ")
    menu_manager.display_meal_items(user_input)