def proportion(list):
    try:
        result = 0
        num = 0
        for i in list:
            if (i % 2) == 0:
                num = num + 1

            result = num / len(list)
        return result
    except Exception as e:
        print("Exception in Proportion:",e)
        return 0