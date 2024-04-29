def display_main_menu():
    print("Sub: display_main_menu()")
    print("Enter some numbers separated by commas (e.g. 5,67,32)")


def get_user_input():
    print("Sub: get_user_input()")
    inputstr = input() # Read the number sequence entered by user.
    print("Input string =", inputstr)

    # Separate the numbers sequence in to short strings, using the list's split() function.
    strlist = inputstr.split(',')
    print("After split:", strlist)

    # Convert every element in the strlist from string to float.
    datalist = [float(value) for value in strlist]

    print("Data List:", datalist)
    return datalist


'''
The function below is much shorter than the get_user_input() above.
# It uses one line of code to read the input, split the number sequence,
# and convert them from string into float. The result is the same.
'''
def get_user_input_shorter_codes():
    print("Sub: get_user_input()")
    datalist = [float(x) for x in input().split(',')]
    print("Data List:", datalist)
    return datalist


def calc_average(inputlist):
    print("Sub: calc_average()")
    print(inputlist)
    print("List length=", len(inputlist))
    total = sum(inputlist)
    average = total / len(inputlist)
    print("Average is", average)
    return average


def find_min_max(inputlist):
    print("Sub: find_min_max()")
    print ("Min =",min(inputlist), "Max =", max(inputlist))
    return [min(inputlist), max(inputlist)]



def sort_temperature(inputlist):
    print("Sub: sort_temperature()")
    print("Before sorting", inputlist)
    templist = sorted(inputlist)
    print("After sorting", templist)
    return templist


def calc_median_temperature(inputlist):
    print("Sub: calc_median_temperature()")
    templist = sorted(inputlist)

    listlen = len(templist)
    # If the number of values is even, take the average of two middle values as the median.
    if (listlen % 2 == 0):
        median_index = int(listlen / 2)
        print("Median indices are", (median_index-1), "and", median_index)
        median = (templist[median_index-1] + templist[median_index])/2.0

    # If the number of values is odd, take the middle value as the median.
    else:
        median_index = int((listlen - 1) / 2)
        print("Median index is", median_index)
        median = templist[median_index]

    print("Median is", median)
    return median


def main():
    print("ET0735 Lab 2 Exercise 6")
    print("=======================")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
    calc_median_temperature(num_list)


if __name__ == "__main__":
    main()
