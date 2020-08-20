stocks = {
    'GOOG': 520.45,
    'FB': 79.98,
    'AMZN': 306.89,
    'AAPL': 99.74,
    'YHOO': 39.28
}

mini = min(zip(stocks.values(), stocks.keys()))
maxi = max(zip(stocks.values(), stocks.keys()))
sort = sorted(zip(stocks.values(), stocks.keys()))

print(mini,'\n',maxi,'\n',sort)


def zipping():
    listone = ['Edward', 'Kim', 'Chelsea']
    listtwo = ['Snowden', 'Dot Com', 'Manning']
    zipping_names = zip(listone, listtwo)
    for a, b in zipping_names:
        print(a, b)


zipping()
