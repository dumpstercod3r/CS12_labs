# pyright: strict

# basic recursion: works as intended
# def cs12_string_count(n: int) -> int:
#     if n < 4:
#         return 0
#     elif n == 4:
#         return 1
#     elif n < 8:
#         return (n-3)*(36**(n-4))
#     else:
#         return 72*cs12_string_count(n-1) - 1296*cs12_string_count(n-2) - 3*cs12_string_count(n-4) + 108*cs12_string_count(n-5) - 2*cs12_string_count(n-8)

# memoization: works as intended
def cs12_string_count(n: int) -> int:
    memory: dict[int, int] = {}
    
    def _cs12_string_count(num: int) -> int:
        if num in memory:
            return memory[num]
        else:
            if num < 4:
                memory[num] = 0
            elif num == 4:
                memory[num] = 1
            elif num < 8:
                memory[num] = (num-3)*(36**(num-4))
            else:
                memory[num] = 72*_cs12_string_count(num-1) - 1296*_cs12_string_count(num-2) - 3*_cs12_string_count(num-4) + 108*_cs12_string_count(num-5) - 2*_cs12_string_count(num-8)

            return memory[num]


    return _cs12_string_count(n)

# Note, memoization makes recursion faster