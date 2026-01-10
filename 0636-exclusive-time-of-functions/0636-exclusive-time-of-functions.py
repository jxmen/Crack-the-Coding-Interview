class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * 101
        stack = []
        pv = 0

        for log in logs:
            fn, cmd, time = log.split(':')
            fn, time = int(fn), int(time)
            if len(stack) == 0:
                stack.append( (fn, time))
            # start일 경우, 이전 함수 실행시간을 저장하고 stack에 새 함수를 쌓는다.
            elif cmd == 'start':
                top_fn = stack[-1][0]

                result[top_fn] += (time - pv)
                stack.append( (fn, time) )
                pv = time
            else:
                last = stack.pop()
                result[fn] += (time - pv) + 1
                pv = time + 1

        return result[:n]