def toh(n, f_rod, to_rod, aux_rod):
  if n==1:
    print("1 from",f_rod,'to rod', to_rod)
    return

  toh(n-1, f_rod, aux_rod, to_rod)
  print(n,'from', f_rod,'to rod', to_rod)
  toh(n-1, aux_rod, to_rod, f_rod)

n=5
toh(n, 'a','b','c')