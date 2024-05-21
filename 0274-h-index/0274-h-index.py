class Solution:

    """
    test case

    [3,0,6,1,5] -> 3
    [5,5,5,5,6] -> 5
    [5,5,5,5,3] -> 4
    [5,5,5,5,2] -> 4
    [5,5,5,3,3] -> 3
    [15,15,15,10,10] -> 5
    """
    def hIndex(self, citations: List[int]) -> int:
        # 1. len(citations + 1) 만큼의 값 누계를 저장하는 배열을 초기화한다.
        n = len(citations)
        counts = [0 for i in range(n + 1)]

        # 2. 누계 배열에 저장한다. 단, n보다 큰 값은 그냥 마지막 값에 저장한다.
        for citation in citations:
            if (citation >= n):
                counts[n] += 1
            else:
                counts[citation] += 1
        
        # 3. n -> 0까지 순회하면서 h-index를 찾을 경우 바로 리턴한다. 이때 h-index는 index와 h의 값이 크거나 같을 경우이다.
        total = 0
        for i in range(n, -1, -1):
            total += counts[i]
            if total >= i:
                return i
        
        return 0
        

    # 연구자가 적어도 h번 이상 인용된 적어도 h개의 논문을 출판했을 때의 h의 최대값으로 정의됩니다.
    def hIndex2(self, citations: List[int]) -> int:
        # [3,0,6,1,5]

        n = len(citations) # 발표한 논문의 숫자
        # TODO: h편의 논문을 구해야 함
        # h편의 논문은 h번 이상 발표되었다면, 그 외에 나머지의 논문이 h번 이하일 경우 이의 최대값이 h-index가 된다.

        # 후보가 될 수 있는 h의 값들을 모두 구하고 이의 최대값을 리턴?
        h_list = [] # [0,1,2,3]
        h_index = 0
        for h in range(0, max(citations)):
            # TODO: h의 후보가 되는지 확인하고, 해당된다면 h_list에 추가한다. <- (어떻게?)
            
            # citations에서 h보다 큰 값들을 찾는다.
            bigger_citations = []
            for citation in citations:
                if h >= citation:
                    bigger_citations.append(citation)
            
            # 나머지 논문들의 개수
            # h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었을 시 h의 최대값
            asdf = len(citations) - len(bigger_citations)
            if len(bigger_citations) >= h and asdf <= h:
                h_list.append(h)
                # h_index 세팅

        return max(h_list) # 리턴