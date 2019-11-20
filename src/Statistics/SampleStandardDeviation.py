import math

def sample_mean #for sample mean
l= len(a)
randm = 0
for i in range(l);
randm = randm + a[i]
ans = randm /l
return ans

def sample_std(b) # for sample standard deviation
t= len(b)
s_randm = 0
x = sample_mean(b)
for j in range (t):
s_randm= s_randm + (b[j] - x)**2
s_ans = math.sqrt(1/(t-1)*s_randm)
return s_ans


sample = [1,2,3,4,5]
std = sample_std(sample)
print(std)