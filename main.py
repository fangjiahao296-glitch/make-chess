import json,os,urllib.request as u
E=os.environ["MAKEFUN_ENV_URL"]
V={'P':100,'N':320,'B':330,'R':500,'Q':900,'K':0}
S=['eeeeooooggikffgjeeeifdcefggaeeee','46886aee8egh8fhi8ehi8fgh6aef4688','acccceeecefgcffgceggcgggcfeeaccc','eeeefgggdeeedeeedeeedeeedeeeeeef','accdceeeceffdeffeeffcfffcefeaccd','8664866486648664a886caaaiieeikge']
T={p:[(int(c,36)-14)*5 for c in s] for p,s in zip('PNBRQK',S)}
O={'N':(-33,-31,-18,-14,14,18,31,33),'K':(-17,-16,-15,-1,1,15,16,17),'B':(-17,-15,15,17),'R':(-16,-1,1,16)};O['Q']=O['K']
def po(p,y={}):return json.load(u.urlopen(u.Request(E+p,data=json.dumps(y).encode())))
def pf(f):
 b={};a=f.split();r=7;K=J=-1
 for w in a[0].split('/'):
  x=0
  for c in w:
   if c<'A':x+=int(c)
   else:
    b[r*16+x]=c
    if c=='K':K=r*16+x
    elif c=='k':J=r*16+x
    x+=1
  r-=1
 return b,a[1]=='w',a[2],-1 if a[3]=='-' else (int(a[3][1])-1)*16+ord(a[3][0])-97,K,J
def at(b,s,u):
 for o in (15,17):
  if b.get(s-o if u else s+o)=='Pp'[not u]:return 1
 for D,y in ((O['N'],'N'),(O['K'],'K')):
  for d in D:
   if b.get(s+d)==(y if u else y.lower()):return 1
 for d in O['K']:
  t=s+d
  while not(t&0x88):
   z=b.get(t)
   if z:
    if z.upper() in ('BQ' if d in (-17,-15,15,17) else 'RQ') and z.isupper()==u:return 1
    break
   t+=d
 return 0

CR={0:'Q',7:'K',112:'q',119:'k'}
def gn(P):
 b,w,c,e,K,J=P;ms=[]
 def A(f,t):
  if (t>>4)==7*w:
   for p in 'qrbn':ms.append((f,t,p))
  else:ms.append((f,t,''))
 for f,x in b.items():
  if (x.isupper())!=w:continue
  y=x.upper()
  if y=='P':
   d=16 if w else -16;t=f+d
   if not(t&0x88) and t not in b:
    A(f,t)
    if (f>>4)==(1 if w else 6) and f+2*d not in b:ms.append((f,f+2*d,''))
   for t in (f+d-1,f+d+1):
    if t&0x88:continue
    z=b.get(t)
    if (z and (z.isupper())!=w) or t==e:A(f,t)
  else:
   for d in O[y]:
    t=f+d
    while not(t&0x88):
     z=b.get(t)
     if z:
      if (z.isupper())!=w:ms.append((f,t,''))
      break
     ms.append((f,t,''))
     if y in 'NK':break
     t+=d
 k=4 if w else 116;u=1-w;R='KQ' if w else 'kq'
 for i,d,s in ((0,2,(1,2)),(1,-2,(-1,-2,-3))):
  if R[i] in c and all(k+j not in b for j in s) and not any(at(b,k+j,u) for j in (0,)+s[:2]):ms.append((k,k+d,''))
 return ms
def ap(P,m):
 b,w,c,e,K,J=P;f,t,p=m;n=b.copy();x=n.pop(f)
 if x in 'Pp' and t==e and (f&7)!=(t&7):n.pop(t-16 if w else t+16)
 if p:x=p.upper() if w else p
 n[t]=x
 if x in 'Kk' and abs(t-f)==2:
  if t>f:n[f+1]=n.pop(f+3)
  else:n[f-1]=n.pop(f-4)
 if x in 'Kk':c=c.replace(x,'').replace('Q' if x=='K' else 'q','')
 for s in (f,t):
  if s in CR:c=c.replace(CR[s],'')
 e2=(f+t)//2 if x in 'Pp' and abs(t-f)==32 else -1
 if x=='K':K=t
 elif x=='k':J=t
 return (n,not w,c,e2,K,J)
def lg(P):
 b,w,c,e,K,J=P;r=[];k=K if w else J;ck=at(b,k,not w)
 for m in gn(P):
  f,t,p=m;Q=ap(P,m)
  if ck or (f>>4)==(k>>4) or (f&7)==(k&7) or not (f-k)%15 or not (f-k)%17 or t==e:
   if at(Q[0],Q[5-w],Q[1]):continue
  v=b.get(t)
  s=(V[v.upper()]*16-V[b[f].upper()] if v else 1500 if t==e else 0)+(900 if p else 0)
  r.append((-s,m,Q))
 r.sort();return [(m,Q) for _,m,Q in r],ck

def ev(P):
 b,w,c,e,K,J=P;s=0
 for q,x in b.items():
  y=x.upper();r=q>>4;g=min(q&7,7-(q&7));v=V[y]+T[y][((7-r) if x.isupper() else r)*4+g]
  s+=v if x.isupper() else -v
 return s+10 if w else 10-s
M=100000;NB=35000
class AB(Exception):pass
def sr(P,d,a,be,pl):
 global ND;ND+=1
 if ND>NB:raise AB
 b,w,c,e,K,J=P;ms,ck=lg(P)
 if not ms:return -M+pl if ck else 0
 if d<=0 and not ck:
  s=ev(P)
  if s>=be:return be
  if s>a:a=s
 for m,Q in ms:
  t=m[1]
  if d<=0 and not ck and t not in b and t!=e and not m[2]:continue
  v=-sr(Q,d-1,-be,-a,pl+1)
  if v>a:a=v
  if a>=be:break
 return a
def ch(P):
 global ND;ND=0;ms,_=lg(P)
 bm=ms[0][0]
 for d in range(1,99):
  try:
   a=-M-1;bv=None
   for m,Q in ms:
    v=-sr(Q,d-1,-M-1,-a,1)
    if v>a:a=v;bv=m
   bm=bv
  except AB:break
 return bm
while True:
 g=po('/game')
 if g['status']=='done':break
 while g['status']=='your_move':
  P=pf(g['fen']);m=ch(P)
  g=po('/move',{'game':g['game'],'move':chr(97+(m[0]&7))+str(m[0]//16+1)+chr(97+(m[1]&7))+str(m[1]//16+1)+(m[2] or '')})
