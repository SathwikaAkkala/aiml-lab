class Main:
    # Set 1 when one character is assigned previously
    use = [0] * 10  
    
    class Node:
        def __init__(self):
            self.letter = ''
            self.value = 0

    def isValid(self, nodeList, count, s1, s2, s3):
        val1 = 0
        val2 = 0
        val3 = 0
        m = 1
        j = 0
        i = 0
        # find number for first string
        for i in range(len(s1) - 1, -1, -1):  
            ch = s1[i]
            for j in range(count):
                # when ch is present, break the loop
                if nodeList[j].letter == ch:  
                    break
            val1 += m * nodeList[j].value
            m *= 10

        m = 1
        # find number for the second string
        for i in range(len(s2) - 1, -1, -1):  
            ch = s2[i]
            for j in range(count):
                if nodeList[j].letter == ch:
                    break
            val2 += m * nodeList[j].value
            m *= 10

        m = 1
        # find number for the third string
        for i in range(len(s3) - 1, -1, -1):  
            ch = s3[i]
            for j in range(count):
                if nodeList[j].letter == ch:
                    break
            val3 += m * nodeList[j].value
            m *= 10
        # check whether the sum is the same as the 3rd string or not
        if val3 == (val1 + val2):  
            return 1
        return 0

    def permutation(self, count, nodeList, n, s1, s2, s3):
        # when values are assigned
        if n == count - 1:  
            for i in range(10):
                # for those numbers, which are not used
                if self.use[i] == 0:  
                    # assign value i
                    nodeList[n].value = i  
                    if self.isValid(nodeList, count, s1, s2, s3) == 1:
                        print("Solution found:", end='')
                        # print code, which is assigned
                        for j in range(count): 
                            print(f" {nodeList[j].letter} = {nodeList[j].value}", end='')
                        return 1
            return 0

        for i in range(10):
            # for those numbers, which are not used
            if self.use[i] == 0:  
                # assign value i and mark as not available for future use
                nodeList[n].value = i  
                self.use[i] = 1
                if self.permutation(count, nodeList, n + 1, s1, s2, s3) == 1:  
                    # go for the next characters
                    return 1
                # when backtracking, make available again    
                self.use[i] = 0 
        return 0

    def solvePuzzle(self, s1, s2, s3):
        # Number of unique characters
        uniqueChar = 0  
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        # There are 26 different characters
        freq = [0] * 26  

        for i in range(len1):
            freq[ord(s1[i]) - ord('A')] += 1

        for i in range(len2):
            freq[ord(s2[i]) - ord('A')] += 1

        for i in range(len3):
            freq[ord(s3[i]) - ord('A')] += 1

        for i in range(26):
            # whose frequency is > 0, they are present
            if freq[i] > 0:  
                uniqueChar += 1
        # as there are 10 digits in the decimal system
        if uniqueChar > 10:  
            print("Invalid strings")
            return 0

        nodeList = [self.Node() for _ in range(uniqueChar)]
        j = 0

        for i in range(26):
            # assign all characters found in three strings
            if freq[i] > 0:  
                nodeList[j].letter = chr(i + ord('A'))
                j += 1

        return self.permutation(uniqueChar, nodeList, 0, s1, s2, s3)

if __name__ == "__main__":
    main = Main()
    print("Enter the first string:")
    s1 = input().strip()
    print("Enter the second string:")
    s2 = input().strip()
    print("Enter the third string:")
    s3 = input().strip()
    
    if main.solvePuzzle(s1, s2, s3) == 0:
        print("No solution")
