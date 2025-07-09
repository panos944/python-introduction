from collections import Counter

my_list = ["apples", "bananas", "kiwi", "orange", "watermelon", "cucumba"]

print(set(my_list))

def count_dict_comprehension(my_list):
    frequency_dict = {item: my_list.count(item) for item in set(my_list)}
    print(frequency_dict)

def count_with_manual_loop(my_list):
    frequency_dict = {}
    for item in my_list:
        if item in frequency_dict.keys():
            frequency_dict[item] +=1
        else:
            frequency_dict[item] = 1
    print(frequency_dict)

def count_with_get_method(my_list):
    frequency_dict = {}
    for item in my_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1
    print(frequency_dict)


def count_with_counter(my_list):
    frequency_dict = Counter(my_list)
    sorted_freq_dict = frequency_dict.most_common()
    print(sorted_freq_dict)


def main():
    my_list = ["apples", "bananas", "kiwi", "orange", "watermelon", "cucumba"]

    count_dict_comprehension(my_list)
    count_with_get_method(my_list)
    count_with_manual_loop(my_list)
    count_with_counter(my_list)


if __name__ == "__main__":
    main()