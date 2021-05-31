#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    from collections import Counter
    mag_dict = dict(Counter(magazine))
    note_dict = dict(Counter(note))
    for k, v in note_dict.items():
        if k not in mag_dict:
            result = 'No'
            break
        if k in mag_dict:
            if v > mag_dict[k]:
                result = 'No'
                break
            if v == mag_dict[k]:
                result = 'Yes'
                
        else:
            result = 'Yes'
    print(result)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

