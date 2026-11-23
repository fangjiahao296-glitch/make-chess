import json,os,urllib.request as u
E=os.environ["MAKEFUN_ENV_URL"]
V=[0,100,320,330,500,900,0]
S=['aaaakkkkccegbbcfaaaeb98abcc6aaaa','024426aa4acd4bde4ade4bcd26ab0244','68888aaa8abc8bbc8acc8ccc8baa6888','422042204220422064428666eeaaegca']
T=[[(int(c,36)-10)*5 for c in s] for s in S]
N=(-33,-31,-18,-14,14,18,31,33)
G=(-17,-16,-15,-1,1,15,16,17)
D=(-17,-15,15,17)
O=(0,0,N,D,(-16,-1,1,16),G,G)
C={0:2,7:1,112:8,119:4,4:3,116:12}
M=9999
class X(Exception):pass
def rq(p,y={}):
 return json.load(u.urlopen(u.Request(E+p,data=json.dumps(y).encode())))
def fp(f):
 bd=[0]*128;pt=f.split();rk=7;fl=0;wk=bk=-1
 for c in pt[0]:
  if c=='/':rk-=1;fl=0
  elif c<'A':fl+=int(c)
  else:
   v='PNBRQK'.index(c.upper())+1
   if c>'Z':v+=8
   sq=rk*16+fl;bd[sq]=v
   if v==6:wk=sq
   elif v==14:bk=sq
   fl+=1
 cr=sum(1<<'KQkq'.index(ch) for ch in pt[2] if ch!='-')
 ep=(int(pt[3][1])-1)*16+ord(pt[3][0])-97 if pt[3]!='-' else -1
 return bd,pt[1]=='b',cr,ep,wk,bk
def ak(bd,sq,foe):
 fo=foe<<3
 for d in ((15,17) if foe else (-15,-17)):
  t=sq+d
  if not t&136 and bd[t]==1|fo:return 1
 for d in N:
  t=sq+d
  if not t&136 and bd[t]==2|fo:return 1
 for d in G:
  t=sq+d
  if t&136:continue
  if bd[t]==6|fo:return 1
  while not t&136:
   p=bd[t]
   if p:
    if p>>3==foe and p&7 in (5,3 if d in D else 4):return 1
    break
   t+=d
 return 0
def gm(st):
 bd,wt,cr,ep,wk,bk=st;ms=[]
 def pr(a,b):ms.extend((a,b,q) for q in ((5,4,3,2) if b>>4==7-7*wt else (0,)))
 for a in range(128):
  if a&136:continue
  x=bd[a]
  if not x or x>>3!=wt:continue
  y=x&7
  if y==1:
   d=16-32*wt;t=a+d
   if not t&136 and not bd[t]:
    pr(a,t)
    if a>>4==1+5*wt and not bd[a+2*d]:ms.append((a,a+2*d,0))
   for t in (a+d-1,a+d+1):
    if not t&136 and ((bd[t] and bd[t]>>3!=wt) or t==ep):pr(a,t)
  else:
   for d in O[y]:
    t=a+d
    while not t&136:
     z=bd[t]
     if z:
      if z>>3!=wt:ms.append((a,t,0))
      break
     ms.append((a,t,0))
     if y in (2,6):break
     t+=d
 ks=4+112*wt;fo=1-wt
 for d,bt in ((2,1<<(wt*2)),(-2,2<<(wt*2))):
  h=d//2
  if cr&bt and not (bd[ks+h] or bd[ks+d] or (d<0 and bd[ks-3])) and not any(ak(bd,ks+j,fo) for j in (0,h,d)):ms.append((ks,ks+d,0))
 return ms
def am(st,mv):
 bd,wt,cr,ep,wk,bk=st;a,b,q=mv;nb=bd[:];x=nb[a];nb[a]=0
 if x&7==1 and b==ep and (a&7)!=(b&7):nb[b-16+32*wt]=0
 nb[b]=(q+8*wt) if q else x
 if (x&7)==6 and abs(b-a)==2:
  r=a+3-7*(b<a);s=a+1-2*(b<a);nb[s]=nb[r];nb[r]=0
 for s in (a,b):cr&=~C.get(s,0)
 e2=(a+b)//2 if x&7==1 and abs(b-a)==32 else -1
 if x==6:wk=b
 elif x==14:bk=b
 return (nb,1-wt,cr,e2,wk,bk)
def lm(st):
 bd,wt,cr,ep,wk,bk=st;r=[];kk=st[4+wt];ck=ak(bd,kk,1-wt)
 for mv in gm(st):
  a,b,q=mv;ns=am(st,mv);z=a-kk
  if ck or a>>4==kk>>4 or a&7==kk&7 or z%15==0 or z%17==0 or b==ep:
   if ak(ns[0],ns[4+wt],1-wt):continue
  s=(V[bd[b]&7]*16-V[bd[a]&7] if bd[b] else 1500 if b==ep else 0)+(V[q]*2 if q else 0)
  r.append((-s,mv,ns))
 r.sort();return [x[1:] for x in r],ck
def sc(st):
 bd=st[0];wt=st[1];s=0
 for sq,x in enumerate(bd):
  if not x:continue
  t=x&7;rk=sq>>4;fl=sq&7;fl=7-fl if fl>3 else fl
  i=(rk if x>7 else 7-rk)*4+fl
  v=V[t]+(T[min(t-1,3)][i] if t not in (4,5) else 0)
  s+=v if x<8 else -v
 return s+12 if wt==0 else 12-s
def ab(st,d,a,be,pl):
 global NC;NC+=1
 if NC>40000:raise X
 bd=st[0];ep=st[3]
 ms,ck=lm(st)
 if not ms:return -M+pl if ck else 0
 if d<=0 and not ck:
  s=sc(st)
  if s>=be:return be
  if s>a:a=s
 for mv,ns in ms:
  b=mv[1]
  if d<=0 and not ck and not bd[b] and b!=ep and not mv[2]:continue
  v=-ab(ns,d-1,-be,-a,pl+1)
  if v>a:a=v
  if a>=be:break
 return a
def rt(st):
 global NC;NC=0;ms,_=lm(st);bm=ms[0][0]
 for d in range(1,99):
  try:
   a=-M-1;bv=None;ns=[]
   for mv,nx in ms:
    v=-ab(nx,d-1,-M-1,-a,1)
    ns.append((-v,mv,nx))
    if v>a:a=v;bv=mv
   ns.sort();ms=[x[1:] for x in ns];bm=bv
  except X:break
 return bm
while True:
 g=rq('/game')
 if g['status']=='done':break
 while g['status']=='your_move':
  st=fp(g['fen']);a,b,q=rt(st)
  g=rq('/move',{'game':g['game'],'move':"%c%d%c%d"%(97+(a&7),a//16+1,97+(b&7),b//16+1)+('nbrq'[q-2] if q else '')})
