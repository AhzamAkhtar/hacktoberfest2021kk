def power(x,n):
  if n==0:
    return 1
  smallpower=power(x,n//2)
  if n%2==0:
    return smallpower*smallpower
  else:
    return x*smallpower*smallpower

ans = power(5,2)

print(ans)