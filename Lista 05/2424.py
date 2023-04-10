Xandytxtsplit = input()
Xtxt, Ytxt = Xandytxtsplit.split()
XN = int(Xtxt)
YN = int(Ytxt)
if -500 <= XN <= 500 and -500 <= YN <= 500:
  if 0 > XN or XN > 432 or 0 > YN or YN > 468:
    print("fora")
  else:
    print("dentro")
