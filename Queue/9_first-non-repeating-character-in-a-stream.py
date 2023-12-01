# https://www.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1

#User function Template for python3

class Solution:
    def FirstNonRepeating(self, A):
        # Code here
        queue=[]
        map={}
        ans=""
        for ch in A:
            # update frequency
            map[ch] = map.get(ch, 0)+1

            # push to queue
            queue.append(ch)

            while(len(queue)!=0):
                front_element = queue[0]

                # check in frequency table and pop if frequency is greater than 1, implies it's a repeating elemenet
                if map[front_element]>1:
                    queue.pop(0)
                else:
                    # frequency is equal to 1, non repeating element
                    ans+=front_element
                    break
            # if queue is empty, implies no repeating element is found
            if len(queue)==0:
                ans+='#'

        return ans







#{
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends