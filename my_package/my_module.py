def top_n(items, n):
    #doc string
    """
        Return the top n items in an array, in desc order.

        Args:
            items (array): list or array-like object
            n (int): num of items to return

        Return:
            array: tip n items in desc order
        
        Egs:
            >>> top_n([2,7,3,6], 3)
            [7,3,6]
    """

    # arrange last n items
    for i in range(n):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j+1], items[j] = items[j], items[j+1]

    #get last n items
    top_n = items[-n:]

    # return items ins descending order
    return top_n[::-1]