import random
from math import floor
import time

random.seed(0)


class ColorConstants:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_mul_pairs():
    pairs = []
    for i in range(2, 11):
        for j in range(1, floor(100 / i) + 1):
            pairs.append((i, j))
            pairs.append((j, i))
    return pairs


def get_add_pairs():
    pairs = []
    for i in range(101):
        for j in range(101 - i):
            pairs.append((i, j))
            pairs.append((j, i))
    return pairs


def delenie(pairs):
    n1, result = random.choice(pairs)
    delenec = n1 * result
    if random.randint(0, 1):
        print(f"{delenec}:▯={n1}")
    else:
        print(f"{delenec}:{n1}=▯")
    person_result = int(input())
    return person_result == result, result


def nasobenie(pairs):
    n1, n2 = random.choice(pairs)
    result = n1 * n2
    print(f"{n1}·{n2}=▯")
    person_result = int(input())
    return person_result == result, result


def scitanie(pairs):
    n1, n2 = random.choice(pairs)
    result = n1 + n2
    print(f"{n1}+{n2}=▯")
    person_result = int(input())
    return person_result == result, result


def odcitanie(pairs):
    n1, result = random.choice(pairs)
    mensenec = n1 + result
    if random.randint(0, 1):
        print(f"{mensenec}-▯={n1}")
    else:
        print(f"{mensenec}-{n1}=▯")
    person_result = int(input())
    return person_result == result, result


def evaluator(score, result, count, correct, priklad_time, average_time, total_time, print_accuracy: bool = True,
              print_time: bool = True,
              accuracy_threshold=0.9):
    if score:
        print(ColorConstants.OK_GREEN + "Vyborne, si hviezda!" + ColorConstants.END_C)
    else:
        print(
            ColorConstants.FAIL + f"Odpoved bola {ColorConstants.BOLD}{result}{ColorConstants.END_C}{ColorConstants.FAIL}, nevadi nabuduce to bude lepsie" + ColorConstants.END_C)
    if print_accuracy:
        accuracy = correct / count
        fail_or_not = ColorConstants.FAIL if accuracy < accuracy_threshold else ColorConstants.OK_GREEN
        print(
            fail_or_not + f"Tvoja uspesnost je {ColorConstants.BOLD}{round(accuracy * 100, 2)}%{ColorConstants.END_C}{fail_or_not}" + ColorConstants.END_C)
    if print_time:
        print(
            ColorConstants.OK_CYAN + f"Tento priklad ti trval {ColorConstants.BOLD}{round(priklad_time, 2)}s{ColorConstants.END_C}{ColorConstants.OK_CYAN}. Priemerny priklad ti trva  {ColorConstants.BOLD}{round(average_time, 2)}s{ColorConstants.END_C}{ColorConstants.OK_CYAN}{ColorConstants.END_C}")


def main():
    mul_pairs = get_mul_pairs()
    add_pairs = get_add_pairs()
    correct_count = 0
    total_time = 0
    count = 0
    while True:
        priklad_start_time = time.time()
        game_mode = random.randint(0, 3)
        if game_mode == 0:
            score, result = delenie(mul_pairs)
        elif game_mode == 1:
            score, result = nasobenie(mul_pairs)
        elif game_mode == 2:
            score, result = scitanie(add_pairs)
        elif game_mode == 3:
            score, result = odcitanie(add_pairs)
        else:
            raise NotImplementedError
        correct_count += score
        count += 1

        priklad_end_time = time.time()
        priklad_time_spent = priklad_end_time - priklad_start_time
        total_time += priklad_time_spent
        average_time = total_time / count
        evaluator(score, result, count, correct_count, priklad_time_spent, average_time, total_time)


if __name__ == '__main__':
    main()
