class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for sen in sentences:
            count1 = len(sen.split())
            count = max(count1, count)
        return count
