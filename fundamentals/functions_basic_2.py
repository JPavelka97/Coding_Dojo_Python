# Countdown

# def countdown(a):
#     count = []
#     while a >= 0:
#         count.append(a)
#         a -= 1
#     return count
# print(countdown(6))

# # # Print and Return
# def print_and_return(a):
#     print(a[0])
#     return(a[1])
# print_and_return([1,2])

# # First plus Length
# def first_plus_length(a):
#     return a[0] + len(a)
# print(first_plus_length([1,2,3]))

# # Values Greater than Second
def values_greater_than_second(a):
    i = 0
    values = []
    if len(a) >= 2:
        while i < len(a):
            if a[i] >= a[2]:
                values.append(a[i])
                i += 1
            else:
                i += 1
        print(len(values))
        print(values)
        return values
    else:
        return "False"
values_greater_than_second([5,2,3,2,1,4])

# def values_greater_than_second_Redux(a):
#     values = []
#     for i in a:
#         if len(a) >= 2:
#             if a[i] >= a[2]:
#                 values.append(a[i])
#     print(values)
# values_greater_than_second_Redux([5,2,3,2,1,4])        

#  This Length, That Value
# def length_and_value(a,b):
#     i = 1
#     newlist = []
#     while i <= a:
#         newlist.append(b)
#         i += 1
#     return newlist
# length_and_value(4,7)