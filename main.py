import time
import random

class Roulette:
    def _get_quantity_for_x_probability(*win_numbers, probability_for_lose):
        numerator = 8*probability_for_lose
        denumerator = 1-probability_for_lose
        num = numerator/denumerator
        print(num)
        return round(num)
    def __init__(self, case_price=10, win_numbers=[2, 16, 32, 43, 58, 74, 88, 100]):
        self.case_price = case_price
        self.win_numbers = win_numbers

    def spin_roulette(self):
        print("Рулетка крутится...")
        nums_that_are_bigger_that_case_price = [ num  for num in self.win_numbers if num>self.case_price]
        num_thats_smaller_that_case_price = [ num  for num in self.win_numbers if num<self.case_price][0]
      
        list_for_winning_number = [num_thats_smaller_that_case_price for i in range(self._get_quantity_for_x_probability(self.win_numbers, probability_for_lose=0.9))]+nums_that_are_bigger_that_case_price
        print(list_for_winning_number)
        
        start_time = time.time()

        while time.time() - start_time < 5:
            current_number = random.choice(nums_that_are_bigger_that_case_price + [num_thats_smaller_that_case_price for _ in range(3)])
    
            print(f"\rТекущее число: {current_number}")
            time.sleep(0.1)
        winning_number = random.choice(list_for_winning_number)
        print(f'Последнее число {winning_number}')
        print("\nОстановка рулетки!")

        # Определение выигрышного числа
       

        # Проверка условий выигрыша
        if (
            winning_number > self.case_price
        ):
            print(f"Поздравляем! Вы выиграли {winning_number}!")
            return winning_number
        else:
            print("К сожалению, вы проиграли.")
            return 0

if __name__ == "__main__":
    roulette = Roulette()

    total_winnings = 0
    total_cases = 0

    while True:
        input("Для открытия кейса нажмите Enter...")
        total_cases += 1
        winnings = roulette.spin_roulette()
        total_winnings += winnings

        print(f"\nОбщий выигрыш: {total_winnings}")
        print(f"Общее количество открытых кейсов: {total_cases}")
        average_winning = total_winnings / total_cases if total_cases > 0 else 0
        print(f"Средний выигрыш за кейс: {average_winning:.2f}\n")
