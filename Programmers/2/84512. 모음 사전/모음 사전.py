def solution(target):
    answer = 0
    chars = ['A', 'E', 'I', 'O', 'U']
    
    # chars를 돌면서 문자를 하나씩 붙이고 answer 값을 증가시키자.
    
    # A -> 1
    # AA -> 2
    # AAA -> 3
    # AAAAA -> 5
    # AAAAE -> 6
    
    def dfs(target, word = ''):
        nonlocal answer
        nonlocal chars
        
        for char in chars:
            word += char
            answer += 1
            if target == word:
                return answer

            if len(word) < 5:
                result = dfs(target, word)
                if result is not None:
                    return result

            # 맨 뒤 문자 잘라내기
            word = word[:len(word)-1]
        
        return None
            
    
    return dfs(target, '')
