from utils import read, write

# параметры для двух хеш-функций
base1 = 27
mod1 = 10**9 + 1
base2 = 113
mod2 = 10**16 + 3

# предварительное вычисление степеней баз
max_power = 10**5 + 5
pre_base1 = [1] * (max_power + 1)
pre_base2 = [1] * (max_power + 1)

for i in range(1, max_power + 1):
    pre_base1[i] = (pre_base1[i-1] * base1) % mod1
    pre_base2[i] = (pre_base2[i-1] * base2) % mod2


# вычисление хеш-значений для символов строки
def compute_hashes(s, base, mod):
    n = len(s)
    hashes = [0] * (n + 1)
    for i in range(n):
        hashes[i+1] = (base * hashes[i] + ord(s[i])) % mod
    return hashes


# основная функция
def longest_common_substring(data):
    s, t = data
    len_s, len_t = len(s), len(t)
    best_len, best_i, best_j = 0, 0, 0

    # для обеих строк вычисляем хеши по двум базам
    s_h1 = compute_hashes(s, base1, mod1)
    s_h2 = compute_hashes(s, base2, mod2)
    t_h1 = compute_hashes(t, base1, mod1)
    t_h2 = compute_hashes(t, base2, mod2)

    # бинарный поиск
    left, right = 0, min(len_s, len_t)
    while left <= right:
        mid = (left + right) // 2   # текущая проверяемая длина
        found = False
        current_i = 0
        current_j = 0

        if mid == 0:    # подстрока длины 0: существует всегда, поэтому идем дальше
            best_len = 0
            left = mid + 1
            continue

        # собираем хеши подстрок
        hashes = {}
        # для подстрок s длины mid находим хеши
        for i in range(len_s - mid + 1):
            h1 = (s_h1[i+mid] - s_h1[i] * pre_base1[mid]) % mod1
            if h1 < 0:  # если хеш отрицательный, добавляем к нему соответствующее значение mod
                h1 += mod1
            h2 = (s_h2[i + mid] - s_h2[i] * pre_base2[mid]) % mod2
            if h2 < 0:
                h2 += mod2
            
            # сохраняем хеши
            key = (h1, h2)
            if key not in hashes:
                hashes[key] = i

        # ищем совпадения с t
        for j in range(len_t - mid + 1):
            # вычисляем хеши
            h1_t = (t_h1[j + mid] - t_h1[j] * pre_base1[mid]) % mod1
            if h1_t < 0:
                h1_t += mod1
            h2_t = (t_h2[j + mid] - t_h2[j] * pre_base2[mid]) % mod2
            if h2_t < 0:
                h2_t += mod2
                
            # проверяем наличие хеша в таблице hashes
            key_t = (h1_t, h2_t)
            if key_t in hashes:
                # проверим на коллизии, явно сравнивая подстроки
                i_candidate = hashes[key_t]
                if s[i_candidate:i_candidate + mid] == t[j:j + mid]:
                    found = True
                    current_i = i_candidate
                    current_j = j
                    break

        # формируем результат
        if found:
            best_len = mid
            best_i = current_i
            best_j = current_j
            left = mid + 1
        else:
            right = mid - 1

    return [best_i, best_j, best_len]


def main():
    data = [list(line) for line in read(type_convert=str)]
    write(end='')
    result = []
    for line in data:
        result.append(longest_common_substring(line))
    for line in result:
        write(*line, to_end=True)


if __name__ == "__main__":
    main()
