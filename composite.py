from abc import ABC, abstractmethod


class MenuComponent(ABC):
    def add(self, menu_component):
        raise NotImplementedError()

    def remove(self, menu_component):
        raise NotImplementedError()

    def get_child(self, i):
        raise NotImplementedError()

    def get_name(self):
        raise NotImplementedError()

    def get_description(self):
        raise NotImplementedError()

    def get_price(self):
        raise NotImplementedError()

    def is_vegetarian(self):
        raise NotImplementedError()

    def print(self):
        raise NotImplementedError()


class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian

    def print(self):
        print(f" {self.get_name()}")
        if self.is_vegetarian():
            print("(v)")
        print(f", {self.get_price()}")
        print(f"     -- {self.get_description()}")


class Menu(MenuComponent):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menu_components = []

    def add(self, menu_component):
        self.menu_components.append(menu_component)

    def remove(self, menu_component):
        self.menu_components.remove(menu_component)

    def get_child(self, i):
        return self.menu_components[i]

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def print(self):
        print(f"\n{self.get_name()}")
        print(f", {self.get_description()}")
        print("---------------------")
        for menu_component in self.menu_components:
            menu_component.print()


class Waitress:
    def __init__(self, all_menus):
        self.all_menus = all_menus

    def print_menu(self):
        self.all_menus.print()


pancake_house_menu = Menu("PANCAKE HOUSE MENU", "Breakfast")
diner_menu = Menu("DINER MENU", "Lunch")
cafe_menu = Menu("CAFE MENU", "Dinner")
dessert_menu = Menu("DESSERT MENU", "Dessert of course!")

all_menus = Menu("ALL MENUS", "All menus combined")

all_menus.add(pancake_house_menu)
all_menus.add(diner_menu)
all_menus.add(cafe_menu)

pancake_house_menu.add(
    MenuItem(
        "K&B's Pancake Breakfast", "Pancakes with scrambled eggs, and toast", True, 2.99
    )
)
pancake_house_menu.add(
    MenuItem(
        "Regular Pancake Breakfast",
        "Pancakes with fried eggs, sausage",
        False,
        2.99,
    )
)
pancake_house_menu.add(
    MenuItem("Blueberry Pancakes", "Pancakes made with fresh blueberries", True, 3.49)
)


diner_menu.add(
    MenuItem(
        "Pasta",
        "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
        True,
        3.89,
    )
)
diner_menu.add(MenuItem("Hamburger", "Hamburger with cheese", False, 2.99))
diner_menu.add(
    MenuItem(
        "Hotdog",
        "A hot dog with saurkraut, relish, onions, topped with cheese",
        False,
        3.05,
    )
)

diner_menu.add(dessert_menu)

dessert_menu.add(
    MenuItem(
        "Apple Pie",
        "Apple pie with a flakey crust, topped with vanilla icecream",
        True,
        1.59,
    )
)
dessert_menu.add(
    MenuItem(
        "Cheesecake",
        "Creamy New York cheesecake, with a chocolate graham crust",
        True,
        1.99,
    )
)
dessert_menu.add(
    MenuItem("Sorbet", "A scoop of raspberry and a scoop of lime", True, 1.89)
)

cafe_menu.add(
    MenuItem(
        "Veggie Burger and Air Fries",
        "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
        True,
        3.99,
    )
)
cafe_menu.add(
    MenuItem(
        "Soup of the day",
        "A cup of the soup of the day, with a side salad",
        False,
        3.69,
    )
)
cafe_menu.add(
    MenuItem(
        "Burrito",
        "A large burrito, with whole pinto beans, salsa, guacamole",
        True,
        4.29,
    )
)

waitress = Waitress(all_menus)
waitress.print_menu()
