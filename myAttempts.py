temp: list[float] = [-20.34, -14.33, -14.1, -10, -5, -1, 0, 0, 1]


def hottest_and_coldest(temperatures: list[float]):
    hottest: float = temp[0]
    coldest: float = temp[-1]
    for i,v in enumerate(temperatures):
        if (i > hottest):
            hottest = v
            index_hottest = i
        if i < coldest:
            coldest = v
            index_coldest = i
    return f'''
{hottest = } and is at index {index_hottest} in the variable {temp =}
{coldest = } and is at index {index_coldest} in the variable {temp =}'''

def main():
    print(hottest_and_coldest(temp))

if __name__ == "__main__":
    main()
