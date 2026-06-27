class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnags = defaultdict(list)
        for i in range(len(strs)):
            listS = list(strs[i])
            listS.sort()
            sortedWord = ("").join(listS)
            groupedAnags[sortedWord].append(strs[i])
        return list(groupedAnags.values())