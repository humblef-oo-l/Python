#Kids Love Muffins 
#Louis was celebrating his 10th Birthday and his parents have promised to make the best party ever for him. He will be very happy if he can invite all his friends to this party (he has many friends), but unfortunately, his parents can't invite everyone because they have a limited number of muffins, and they want everyone to be happy. As we all know, kids love to eat a lot of muffins of the same type, let's say a kid will be happy only if he can eat at least K muffins of the same type.

n,k=map(int,input().split())
L=list(map(int,input().split()))
rope=L[0]+L[1]-(2*k)
for i in range(2,n):
    rope+=L[i]-(2*k)
print(rope)
