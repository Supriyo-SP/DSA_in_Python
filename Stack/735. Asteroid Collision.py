class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        l=len(asteroids)
        st=[]
        for i in range(0,l):
            if asteroids[i] >0:
                st.append(asteroids[i])
            else:
                while len(st)!=0 and st[-1]>0 and st[-1]<abs(asteroids[i]):
                    st.pop()
                if len(st)!=0 and st[-1]==abs(asteroids[i]):
                    st.pop() 
                elif len(st)==0 or st[-1]<0:
                    st.append(asteroids[i])   
        return st                    
        