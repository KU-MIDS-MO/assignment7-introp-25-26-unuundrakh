def build_pipeline(operation_names):
    operations = {"double": lambda x: x * 2,
                  "triple": lambda x: x * 3,
                  "square": lambda x: x ** 2,}
    for name in operation_names:
        if name not in operations:
            raise KeyError(name)
            
    def pipeline(value):
        result = value
        for name in operation_names:
            result = operations[name](result)
        return result

    return pipeline


## Task 3 — Operation pipeline

# Write a function:

# build_pipeline(operation_names)


# where operation_names is a list of strings.

# The function must return a new function that applies a sequence of operations to a single input value,in the given order.

# Each string in operation_names represents an operation



# If an unknown operation name is encountered, an error must be raised.

# Calling the returned function should apply all operations sequentially and return the final result.