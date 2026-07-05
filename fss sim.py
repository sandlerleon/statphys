"""Finite-size scaling of the field-free (h0=0) site-diluted XY transition.
For L in {32,48,64} at fixed T, measure vs killed fraction f:
  order parameter U_chi, Binder cumulant U4, helicity modulus Upsilon.
Nelson-Kosterlitz: transition where Upsilon = 2T/pi. Compare to 1-p_c=0.4073."""
import numpy as np, matplotlib.pyplot as plt, time
from matplotlib import gridspec
T=0.45; NK=2*T/np.pi
fs=np.array([0.0,0.10,0.20,0.28,0.34,0.40,0.46,0.55])
Ls=[32,48,64]; SEEDS=3; EQ=260; MEAS=260; SAMP=5
def checker(L): return (np.add.outer(np.arange(L),np.arange(L)))%2
def sweep(th,g,L,idx,rng):
    for c in (0,1):
        mask=idx==c; prop=th+rng.uniform(-np.pi,np.pi,(L,L))
        e0=np.zeros((L,L)); e1=np.zeros((L,L))
        for sh,ax in [(1,0),(-1,0),(1,1),(-1,1)]:
            J=g*np.roll(g,sh,ax); thj=np.roll(th,sh,ax)
            e0-=J*np.cos(th-thj); e1-=J*np.cos(prop-thj)
        acc=(rng.random((L,L))<np.exp(-(e1-e0)/T))&mask
        th=np.where(acc,prop,th)
    return th
def helicity(th,g,L):
    ups=[]
    for ax in (0,1):
        J=g*np.roll(g,-1,ax); d=th-np.roll(th,-1,ax)
        Hx=np.sum(J*np.cos(d)); Ix=np.sum(J*np.sin(d))
        ups.append((Hx/(L*L))-(Ix*Ix)/(L*L*T))
    return 0.5*(ups[0]+ups[1])
def run(L,f,seed):
    rng=np.random.default_rng(seed); idx=checker(L)
    g=np.ones((L,L)); g[rng.random((L,L))<f]=0.0
    th=rng.normal(0,0.1,(L,L))
    for _ in range(EQ): th=sweep(th,g,L,idx,rng)
    m2=[];m4=[];up=[]; Nocc=max(int(g.sum()),1)
    for t in range(MEAS):
        th=sweep(th,g,L,idx,rng)
        if t%SAMP==0:
            M=np.sum(g*np.exp(1j*th))/Nocc; mm=abs(M)
            m2.append(mm*mm);m4.append(mm**4);up.append(helicity(th,g,L))
    m2=np.mean(m2);m4=np.mean(m4)
    return np.sqrt(m2),1-m4/(3*m2*m2),np.mean(up)
t0=time.time()
res={L:{'U':[],'Ue':[],'B':[],'Y':[],'Ye':[]} for L in Ls}
for L in Ls:
    for f in fs:
        U=[];B=[];Y=[]
        for s in range(SEEDS):
            u,b,y=run(L,f,1000+s+int(f*131)+L);U.append(u);B.append(b);Y.append(y)
        res[L]['U'].append(np.mean(U));res[L]['Ue'].append(np.std(U)/np.sqrt(SEEDS))
        res[L]['B'].append(np.mean(B));res[L]['Y'].append(np.mean(Y));res[L]['Ye'].append(np.std(Y)/np.sqrt(SEEDS))
    print("L=%d done (%.0fs)"%(L,time.time()-t0))
def crossf(x,y,lv):
    y=np.array(y)
    for i in range(len(x)-1):
        if (y[i]-lv)*(y[i+1]-lv)<0: return x[i]+(lv-y[i])*(x[i+1]-x[i])/(y[i+1]-y[i])
    return np.nan
fKT={L:crossf(fs,res[L]['Y'],NK) for L in Ls}
print("f_KT (helicity=2T/pi):",{L:round(float(v),3) for L,v in fKT.items()})
fig=plt.figure(figsize=(13,4.3)); gs=gridspec.GridSpec(1,3,wspace=0.30); grid="#ddd"
cols={32:"#2c7fb8",48:"#e08e0b",64:"#c0392b"}; pc=1-0.5927
axA=fig.add_subplot(gs[0])
for L in Ls: axA.errorbar(fs,res[L]['U'],yerr=res[L]['Ue'],fmt='o-',color=cols[L],lw=1.8,ms=4,capsize=2,label="L=%d"%L)
axA.axvline(pc,color='k',ls=':',lw=1.3); axA.text(pc+0.01,0.9,r"$1-p_c=0.407$",fontsize=8)
axA.set_xlabel("killed fraction f");axA.set_ylabel(r"order $U_\chi$");axA.set_ylim(0,1)
axA.set_title("A. Order parameter (FSS)",fontsize=10,loc="left");axA.legend(fontsize=8);axA.grid(True,color=grid)
axB=fig.add_subplot(gs[1])
for L in Ls: axB.errorbar(fs,res[L]['Y'],yerr=res[L]['Ye'],fmt='o-',color=cols[L],lw=1.8,ms=4,capsize=2,label="L=%d"%L)
axB.axhline(NK,color='k',ls='--',lw=1.2);axB.text(0.02,NK+0.02,r"$2T/\pi$ (Nelson–Kosterlitz)",fontsize=8)
axB.axvline(pc,color='k',ls=':',lw=1.3)
axB.set_xlabel("killed fraction f");axB.set_ylabel(r"helicity modulus $\Upsilon$")
axB.set_title(r"B. Helicity modulus vs $2T/\pi$",fontsize=10,loc="left");axB.legend(fontsize=8);axB.grid(True,color=grid)
axC=fig.add_subplot(gs[2])
for L in Ls: axC.errorbar(fs,res[L]['B'],fmt='o-',color=cols[L],lw=1.8,ms=4,label="L=%d"%L)
axC.axvline(pc,color='k',ls=':',lw=1.3)
axC.set_xlabel("killed fraction f");axC.set_ylabel(r"Binder cumulant $U_4$")
axC.set_title(r"C. Binder cumulant (crossing $=f_c$)",fontsize=10,loc="left");axC.legend(fontsize=8);axC.grid(True,color=grid)
plt.savefig("/home/claude/sp4_fig_fss.png",dpi=150,bbox_inches="tight")
print("FSS fig saved (%.0fs)"%(time.time()-t0))
for L in Ls:
    print(" L=%d U="%L,np.round(res[L]['U'],3)); print("       Y=",np.round(res[L]['Y'],3))
