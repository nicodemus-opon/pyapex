from pyapex import Chart

plt = Chart(type="candlestick")
plt.set_series([{
    "data": [
        [1538856000000, 6593.34, 6600, 6582.63, 6600],
        [1538856900000, 6595.16, 6604.76, 6590.73, 6593.86]
    ]
}])

plt.set_xaxis({"type": 'datetime'})
plt.show()
