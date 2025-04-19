class OddNumberSeries:
    def generate_series(self, a):
        series = []
        for i in range(a):
            series.append(2 * i + 1)
        return ",".join(map(str, series))

# Taking user input
a = int(input("Enter an integer: "))

# Create instance and generate series
odd_series = OddNumberSeries()
print(odd_series.generate_series(a))
