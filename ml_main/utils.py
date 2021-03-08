def unique_fid_generator(type_id, fid):
    """Method to handle ID generator."""
    try:
        unique_type_id = '%04d' % type_id
        unique_fid = '%06d' % fid
        checkdigit = calculate_luhn(str(unique_fid))
        final_id = '{}{}{}'.format(
            str(unique_type_id), str(unique_fid), str(checkdigit))
    except Exception:
        return 'XXXXXXXXXXX'
    else:
        return final_id


def luhn_checksum(check_number):
    '''
    http://en.wikipedia.org/wiki/Luhn_algorithm
    '''
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(check_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10


def is_luhn_valid(check_number):
    '''
    http://en.wikipedia.org/wiki/Luhn_algorithm
    '''
    return luhn_checksum(check_number) == 0


def calculate_luhn(partial_check_number):
    '''
    http://en.wikipedia.org/wiki/Luhn_algorithm
    '''
    check_digit = luhn_checksum(int(partial_check_number) * 10)
    return check_digit if check_digit == 0 else 10 - check_digit
