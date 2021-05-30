class Problem():

    def __init__(self, typed_string) -> None:

        self.typed_string = typed_string

    def key_pad_definition(key_, ind):
        keypad = {
            '1' : [''],
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z'],
            '0' : [' '],
            '*' : [''], #'*'
            '#' : [''] #'#'
        }
        return keypad[key_][ind]

    def evaluation_(self):
        typed_string = self.typed_string
        typed_dict = dict(Counter(typed_string))
        print(typed_dict)
        typed_list = []
        for k, v in typed_dict.items():
            if k in ['2','3','4','5','6','8']:
                typed_list.append(Problem.key_pad_definition(k, (v%3)-1))
            elif k in ['7','9']:
                typed_list.append(Problem.key_pad_definition(k, (v%4)-1))
            elif k in ['1','*','#']:
                typed_list.append(Problem.key_pad_definition(k, 0))
        return ''.join(typed_list)

    def evaluation(self):

        typed_string = self.typed_string
        count = 0
        cur_key = typed_string[0]
        pre_key = typed_string[0]
        result = []
        for i in range(1, len(typed_string)+1):
            s = typed_string[i-1]
            print(i)
            cur_key = s # 2 , 0
            if pre_key != cur_key : # 2 ! 0
                print(pre_key, count-1)
                result.append(Problem.key_pad_definition(pre_key, count-1))
            if s in ['2','3','4','5','6','8']:
                if cur_key == pre_key: # 2 == 2
                    count += 1 # c = 1
                elif count > 3:
                    count = 1
            elif s in ['7', '9']:
                if cur_key == pre_key:
                    count += 1
                elif count > 4 or cur_key != pre_key:
                    count = 1
            elif s in ['1', '*', '#']:
                pass
            elif s == '0':
                count = 1
            pre_key = s #2
        if cur_key:
            result.append(Problem.key_pad_definition(cur_key, count-1))

        return result

if __name__ == '__main__':
    from collections import Counter
    keys = '2022'
    obj = Problem(keys)
    print(obj.evaluation())