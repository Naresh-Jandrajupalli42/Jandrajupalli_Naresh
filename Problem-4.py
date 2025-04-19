class MultipleCounter:
    def count_multiples(self, num_list):
        multiple_dict = {i: 0 for i in range(1, 10)}  # Initialize dictionary with keys 1 to 9
        
        for num in num_list:  # Iterate through the input list
            for i in range(1, 10):  # Check multiples from 1 to 9
                if num % i == 0:
                    multiple_dict[i] += 1  # Increment count if it's a multiple
        
        return multiple_dict

# Taking user input
num_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Create instance and count multiples
counter = MultipleCounter()
result = counter.count_multiples(num_list)

print(result)  # Output the dictionary

