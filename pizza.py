
class PepperonPizza:
    def __init__(self, name, structure)
        self.name = name
        self.strcture = structure

class BBQPizza(Pizza): 
    def __init__(self, extra_topinc: list = None) -> None:   
        toppings = ["Курица", "лук", "Сыр"] 
        self.extra_toppings = ["Барбекю", "Яйцо"] 
 
        super.__init__("Барбекю", "стандартное", "какой-то", topping, "4500тенге") 
 
    def add_topping(self, topping: str) -> None: 
        choice = input(f"Хотите добавить {topping}? (да/нет)") 
        if choice.lower() == "нет":
            return 
        if choice.lower( ) == "да":
            if topping in self.toppings: 
                print(Он уже есть в пицце) 
                return 
            self.topping.append(topping) 
            print("Добавлено") 
            return 
 
    def chage_topping(self, new_topping: list) -> None: 
        self.toppings = new_topping 
        print("Ингредиент удалён") 
 
    def ask_topping(self) -> str: 
        return input( 
            f"Какой ингредиент добавить ? {self.extra_toppings}: "
        )


class Order:

    def __init__(self) -> None:
        self.pizaas: list[Pizza] = []

    def add_pizza(self, pizza: Pizza) -> None:
        """Добавляет пиццу в заказ."""
        self.pizzas.append(pizza)

    def calculate_total(self) -> int:
        """Возращает итоговую стоимость заказа."""
        return sum(pizza.price for pizza in self.pizzas)

class Terminal:
    def __init__(self) -> None:
        self.menu dict[int, Pizza] = {
            1: PepperonPizza(),
            2: BBQPizza(),
            3: SeafoodPizza(),
        }
        self.order: Order | None = None

    def display_menu(self) -> None:
        """Меню, отоборажает меню с пиццами"""
        print("Menu:", "-" * 80, sep="\n")
        fey, pizza in self.menu.items():
        print(f"{key}, {pizza.name} - {pizza.price} тенге")

    def take_order(order) -> None:
        self.order = order
        while True:
            self.display_menu()
            choice = input(
                "=" * 80
                + "\n Введите номер пиццы, которую хотите добавить в заказ"
                +"-" * 80
                +"\n"
            )
            if choice == "0":
                break
            if choice == "2":
                topping = self.menu[int(choice)].ask_topping()
                self.menu[int(choice)].add_topping(opping)
            if int(choice) in self.menu:
                self.order.add_pizza(self.menu[int(choice)])
                print(f"{self.menu[int(choice)].name} добавлен в ваш заказ.")
            else:
                print("Неверный выбор. Пожалуйста, выберите пиццу из меню")
                continue
    def confirm_order(self) -> bool:
        """Подверждает заказ, возращает True, если заказ подтвержден."""
        if self.order:
            print(f"Итого к оплате: {self.order.calculate_total()} тенге")
            confirmation = input("Вы хотите подтвердит ваш заказ? (да/нет): ")
            if confirmation.lower() == "да":
                print("Заказ подтвержден.")
                return True
            else:
                print("Заказ отменен.")
                self.order = 





class Person:

    def __init__(self, name, number, ingredients):
        self.name = name
        self.number = number
        self.ingredients = ingredients

    def prepare(self) -> None:
        """Подготовка пиццы, выводим информацию о готовке"""
        print(
            f"Подготовка пиццы {self.name} с тестом {self.dought}, с соусом{self.sauce}"
        )
    def bake(self) -> None:
        """Жариться в печи"""
        print(f" Пицца {self.name} вышло из духовки")

    def cut(self) -> None:
        """Делим на кусочки пиццу"""
        print(f"Пиццу {self.name} делим на куски")
    def box(self) -> None:
        """Кажется кладем в коробку"""
        print(f"Пицца {self.name} кладется в коробку")

class Pepperoni:
    def  __init__(self, name, number):
        self.name = name

    

pepperoni = Person()

if __name__ == "__main__":


print("Пицца пепперони - 3500тг")
print("Пицца Барбекю - 2500тг")
print("Пицца Дары Моря - 4500тг")

person = int(input("Введите номер пиццы, которую хотите добавить в заказ (0 для завершение): "))