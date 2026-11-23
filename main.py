import json,os,urllib.request as u
E=os.environ["MAKEFUN_ENV_URL"]
V=[0,100,320,330,500,900,0]
S=['eeeeooooggikffgjeeeifdcefggaeeee','46886aee8egh8fhi8ehi8fgh6aef4688','acccceeecefgcffgceggcgggcfeeaccc','eeeefgggdeeedeeedeeedeeedeeeeeef','accdceeeceffdeffeeffcfffcefeaccd','8664866486648664a886caaaiieeikge']
T=[[(int(c,36)-14)*5 for c in s] for s in S]
N=(-33,-31,-18,-14,14,18,31,33)
K=(-17,-16,-15,-1,1,15,16,17)
D=(-17,-15,15,17)
O=(0,0,N,D,(-16,-1,1,16),K,K)
CR={0:2,7:1,112:8,119:4,4:3,116:12}
M=9999
class AB(Exception):pass
def po(p,y={}):return json.load(u.urlopen(u.Request(E+p,data=json.dumps(y).encode())))
def pf(f):
 b=[0]*128;a=f.split();r=7;x=0;K=J=-1
 for c in a[0]:
  if c=='/':r-=1;x=0
  elif c<'A':x+=int(c)
  else:
   t='PNBRQK'.index(c.upper())+1
   if c>'Z':t+=8
   b[r*16+x]=t
   if t==6:K=r*16+x
   elif t==14:J=r*16+x
   x+=1
 return b,a[1]=='b',sum(1<<'KQkq'.index(ch) for ch in a[2] if ch!='-'),-1 if a[3]=='-' else (int(a[3][1])-1)*16+ord(a[3][0])-97,K,J
def at(b,s,u):
 o=u<<3
 for d in (15,17) if u else (-15,-17):
  t=s+d
  if not t&0x88 and b[t]==1|o:return 1
 for d in N:
  t=s+d
  if not t&0x88 and b[t]==2|o:return 1
 for d in K:
  t=s+d
  if t&0x88:continue
  if b[t]==6|o:return 1
  while not t&0x88:
   p=b[t]
   if p:
    if p>>3==u and ((p&7)==5 or (p&7)==(3 if d in D else 4)):return 1
    break
   t+=d
 return 0
def gn(P):
 b,w,c,e,K,J=P;ms=[]
 def A(f,t):
  if (t>>4)==7-7*w:
   for p in (5,4,3,2):ms.append((f,t,p))
  else:ms.append((f,t,0))
 for f in range(128):
  if f&0x88:continue
  x=b[f]
  if not x or x>>3!=w:continue
  y=x&7
  if y==1:
   d=16-32*w;t=f+d
   if not t&0x88 and not b[t]:
    A(f,t)
    if (f>>4)==1+5*w and not b[f+2*d]:ms.append((f,f+2*d,0))
   for t in (f+d-1,f+d+1):
    if not t&0x88 and ((b[t] and b[t]>>3!=w) or t==e):A(f,t)
  else:
   for d in O[y]:
    t=f+d
    while not t&0x88:
     z=b[t]
     if z:
      if z>>3!=w:ms.append((f,t,0))
      break
     ms.append((f,t,0))
     if y%4==2:break
     t+=d
 k=4+112*w;u=1-w
 for d,bit in ((2,1<<(w*2)),(-2,2<<(w*2))):
  h=d//2
  if c&bit and not (b[k+h] or b[k+d]) and (d==2 or not b[k+d+h]) and not any(at(b,k+j,u) for j in (0,h,d)):ms.append((k,k+d,0))
 return ms
def ap(P,m):
 b,w,c,e,K,J=P;f,t,p=m;n=b[:];x=n[f];n[f]=0
 if (x==1 or x==9) and t==e and (f&7)!=(t&7):n[t-16+32*w]=0
 n[t]=(p+8*w) if p else x
 if (x&7)==6 and abs(t-f)==2:
  r=f+3 if t>f else f-4;q=f+1 if t>f else f-1;n[q]=n[r];n[r]=0
 for s in (f,t):c&=~CR.get(s,0)
 e2=(f+t)//2 if (x==1 or x==9) and abs(t-f)==32 else -1
 if x==6:K=t
 elif x==14:J=t
 return (n,1-w,c,e2,K,J)
def lg(P):
 b,w,c,e,K,J=P;r=[];k=(K,J)[w];ck=at(b,k,1-w)
 for m in gn(P):
  f,t,p=m;Q=ap(P,m)
  if ck or (f>>4)==(k>>4) or (f&7)==(k&7) or (f-k)%15==0 or (f-k)%17==0 or t==e:
   if at(Q[0],Q[4+w],1-w):continue
  v=b[t];x=b[f]
  s=(V[v&7]*16-V[x&7] if v else 1500 if t==e else 0)+(900 if p else 0)
  r.append((-s,m,Q))
 r.sort();return [(m,Q) for _,m,Q in r],ck
def ev(P):
 b,w,c,e,K,J=P;s=0
 for q,x in enumerate(b):
  if not x:continue
  t=x&7;r=q>>4;g=q&7
  if g>3:g=7-g
  i=((7-r) if x<8 else r)*4+g
  v=V[t]+T[t-1][i]
  s+=v if x<8 else -v
 return s+10 if w==0 else 10-s
def sr(P,d,a,be,pl):
 global ND;ND+=1
 if ND>50000:raise AB
 b,w,c,e,K,J=P
 ms,ck=lg(P)
 if not ms:return -M+pl if ck else 0
 if d<=0 and not ck:
  s=ev(P)
  if s>=be:return be
  if s>a:a=s
 bv=0
 for m,Q in ms:
  t=m[1]
  if d<=0 and not ck and not b[t] and t!=e and not m[2]:continue
  v=-sr(Q,d-1,-be,-a,pl+1)
  if v>a:a=v;bv=m
  if a>=be:break
 return a
def ch(P):
 global ND;ND=0;ms,_=lg(P);bm=ms[0][0]
 for d in range(1,99):
  try:
   a=-M-1;bv=None;ns=[]
   for m,Q in ms:
    v=-sr(Q,d-1,-M-1,-a,1)
    ns.append((-v,m,Q))
    if v>a:a=v;bv=m
   ns.sort();ms=[(m,Q) for _,m,Q in ns];bm=bv
  except AB:break
 return bm
while True:
 g=po('/game')
 if g['status']=='done':break
 while g['status']=='your_move':
  P=pf(g['fen']);m=ch(P)
  g=po('/move',{'game':g['game'],'move':chr(97+(m[0]&7))+str(m[0]//16+1)+chr(97+(m[1]&7))+str(m[1]//16+1)+('nbrq'[m[2]-2] if m[2] else '')})
