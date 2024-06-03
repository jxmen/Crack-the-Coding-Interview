class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            sortedS = ''.join(sorted(str))
            if sortedS in dict:
                dict[sortedS].append(str)
            else:
                dict[sortedS] = [str]
        
        answers = []
        for key in dict:
            answer = []
            for str in dict[key]:
                answer.append(str)
            
            answers.append(answer)
        
        return answers
        