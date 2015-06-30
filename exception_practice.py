__author__ = 'Oliver'
# class OllieException(Exception):
#     pass
#
# class SillyPants(Exception):
#     pass

def sequential(array):
    if len(array) < 1 or type(array) != list:
        print "length or type error!"
    elif sorted(array) == range(min(array), len(array) + min(array)):
        return True
    else:
        raise OllieException("Not a sequential list!")

# assert sequential([1, 2, 3, 4]) is True
# assert sequential([2, 3, 4]) is True
# assert sequential([4, 6, 5, 2, 3]) is True
# try:
#     print sequential([1, 4, 7])
# except OllieException:
#     pass
# else:
#     raise AssertionError("You done f'ed up")
#
