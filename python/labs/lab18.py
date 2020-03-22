"""
peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

# """
# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# noindex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# POI = [' ',' ',' ',' ',' ',' ','P',' ',' ','V',' ',' ',' ',' ','P',' ',' ','V',' ',' ',' ',]

# def peaks():
#     length = len(data)
#     middle_index = length//2

#     first_half = data[:middle_index]
#     second_half = data[middle_index:]
#     # peak = first_half.index('P')

#     peak = data.index(max(first_half))
#     peak_2 = data.index(max(second_half))

    # if peak_2 == data[0] or peak_2 == data[20]:


    # print(f"The index of the peak on the left is {peak}")
    # print(f"The index of the peak on the right is {peak_2}")
    
# peaks()

# def valleys():
#     length = len(data)
#     middle_index = length//2

#     first_half = data[:middle_index]
#     second_half = data[middle_index:]

#     print (first_half)
#     print(second_half)
    # valley = data.index(min(first_half))
    # valley_2 = data.index(min(second_half))

    # print(f"The index of the valley on the left is {valley}")
    # print(f"The index of the valley on the right is {valley_2}")

# valleys()


# def peaks_and_valleys():
#     peaks()
#     valleys()
    # length = len(data)
    # middle_index = length//2

    # first_half = data[:middle_index]
    # second_half = data[middle_index:]
    # # peak = first_half.index('P')

    # peak = data.index(max(first_half))
    # peak_2 = data.index(max(second_half))

    # print(f"The index of the peak on the left is {peak}")
    # print(f"The index of the peak on the right is {peak_2}")


    # length = len(data)
    # middle_index = length//2

    # first_half = data[:middle_index]
    # second_half = data[middle_index:]

    # valley = data.index(min(first_half))
    # valley_2 = data.index(min(second_half))

    # print(f"The index of the valley on the left is {valley}")
    # print(f"The index of the valley on the right is {valley_2}")

# peaks_and_valleys()


def get_data():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    return data

def get_valleys(data):
    valleys = []
    index_list = list(range(len(data)))
    
    for i in index_list:
        if (i-1) in index_list and (i+1) in index_list: # makes the index start at 1 so the indexing is not out of range?
            if data[i] <= data[i-1] and data[i] <= data[i+1]:
                valleys.append(i)
    return valleys

def get_peaks(data):
    peaks = []
    index_list = list(range(len(data)))

    for i in index_list:
        if (i-1) in index_list and (i+1) in index_list:
            if data[i] >= data [i-1] and data [i] >= data [i+1]:
                peaks.append(i)
    return peaks 

def peaks_and_valleys():
    print(get_peaks())
    print(get_valleys())