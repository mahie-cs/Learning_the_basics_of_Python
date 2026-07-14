# I was playing with linked lists. Then I realised, array, which gets compared to linked lists very often, has a lot of built in support in many languages.
# What if I take away those layers that makes Arrays easy? Which I did. No libraries, No [], just barebones array.
# I don't see why I would use this, but atleast its doable.

array_storage = 0

array_storage |= 10 << (0 * 8)
array_storage |= 25 << (1 * 8)
array_storage |= 42 << (2 * 8)
array_storage |= 99 << (3 * 8)
array_storage |= 7 << (4 * 8)

def get_element(array, index):
    return (array >> (index * 8)) & 0xFF

print(get_element(array_storage, 0))
print(get_element(array_storage, 1))
print(get_element(array_storage, 2))
print(get_element(array_storage, 3))
print(get_element(array_storage, 4))
