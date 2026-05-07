class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a=asteroids
        st=[]
        for i in range(len(asteroids)):
            if a[i]>0:
                st.append(a[i])
            else:
                while st and st[-1]<abs(a[i]) and st[-1]>0:
                    st.pop()
                if st and st[-1]==abs(a[i]):
                    st.pop()
                elif len(st)==0 or st[-1]<0:
                    st.append(a[i])
        return st
