def kbig(nums, k):
    for i in nums:
        count_more = 0          #кол-во элементов которые больше элемента i
        for j in nums:
            if i < j:
                count_more += 1
        if count_more == k-1:   #если кол-во элементов равно k-1, то мы нашли нужное число и выводим i 
            return i


while True:
    print("Вход (введите значения списка через пробел): ")
    nums = [int(i) for i in input('nums = ').split()]
    k = int(input('Введите k = '))
    print("Вывод: ", kbig(nums, k))
