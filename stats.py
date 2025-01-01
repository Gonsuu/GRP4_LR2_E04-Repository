def mode(listX):
    
    listX.sort()

    current_number = listX[0]
    current_count = 1
    max_count = 1
    modes = [current_number]

    for i in range(1, len(listX)):
        if listX[i] == current_number:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                modes = [current_number]
            elif current_count == max_count:
                modes.append(current_number)
            
            current_number = listX[i]
            current_count = 1
    
    if len(modes) == len(listX):
        return ("No mode, all numbers appear with the same frequency.")

    if current_count > max_count:
        modes = [current_number]
    elif current_count == max_count:
        modes.append(current_number)

    return modes

def mean(listX):

    x = listX[0:len(listX)]
    y = sum(x)
    avg = y / len(listX)
    return avg

def median(listX):

    listX.sort()
    if len(listX) % 2 == 0:
        mid = len(listX) // 2
        med = (listX[mid - 1] + listX[mid]) / 2
        return med

    elif len(listX) % 2 == 1:
        mid = len(listX) // 2
        med = listX[mid]
        return med

def main():
    listX = input("Input the set of numbers separated by a space: ")

    if not listX.strip():
        print("The list is empty.")
        print("Mean returned    :   0") 
        print("Median returned  :   0") 
        print("Mode returned    :   0") 
        return 0

    listX = listX.split()
    try:
        listX = [int(num) for num in listX]

    except ValueError:
        print("Invalid input.")
        print("The program requires a set of numbers separated by a space.")
        return 0
    
    print(f"The list is",listX)
    print(f"The mean is     :", mean(listX))
    print(f"The median is   :", median(listX))
    print(f"The mode is     :", mode(listX))

if __name__ == "__main__":
    main()
