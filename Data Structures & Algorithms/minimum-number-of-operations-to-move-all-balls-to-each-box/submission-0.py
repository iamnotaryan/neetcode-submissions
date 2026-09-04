class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0]*n
        cost = 0
        for i in range(n):
            if boxes[i]=="1":
                cost += i
        ans[0] = cost
        left = 1 if boxes[0] == "1" else 0
        right = boxes.count("1") - left
        for i in range(1,n):
            cost += left - right
            ans[i] = cost
            if boxes[i] == "1":
                left += 1
                right -= 1
        return ans