class SelectiveOddSeries:
    def generate_series(self, a):
        x = a // 2 if a % 2 == 0 else (a + 1) // 2  # Determine count based on even/odd input
        series = [2 * i + 1 for i in range(x)]  # Generate selective odd number series
        return ",".join(map(str, series))  # Return as comma-separated string

# Taking user input
a = int(input("Enter an integer: "))

# Create instance and generate the selective odd number series
selective_series = SelectiveOddSeries()
print(selective_series.generate_series(a))
