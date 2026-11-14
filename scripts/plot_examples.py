"""Reproducible math plots; use --out PATH. Matplotlib backend: Agg."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from math import comb

def save(fig, out, name):
    fig.savefig(out / (name+'.pdf'), bbox_inches='tight')
    fig.savefig(out / (name+'.png'), dpi=180, bbox_inches='tight')
    plt.close(fig)

def main(out):
    out.mkdir(parents=True, exist_ok=True)
    # Exact parabola and derivative-based tangent at x=1.
    x=np.linspace(-2,4,600); f=x*x-4*x+7
    fig,ax=plt.subplots(figsize=(6.6,4.4))
    ax.plot(x,f,label=r'$f(x)=x^2-4x+7$')
    # f'(x)=2x-4, so at x=1 the tangent is y=-2x+6.
    assert 1**2 - 4*1 + 7 == -2*1 + 6
    ax.plot(x,-2*x+6,'--',label=r'tangent at $x=1$: $y=-2x+6$')
    ax.scatter([1,2],[4,3],zorder=5)
    ax.annotate('(1,4)',(1,4),xytext=(8,12),textcoords='offset points')
    ax.annotate('vertex (2,3)',(2,3),xytext=(12,18),textcoords='offset points')
    ax.set(xlabel='x',ylabel='y',title='Quadratic function and tangent');ax.grid(alpha=.25);ax.legend();save(fig,out,'parabola_tangent')
    # Rational function split around x=1; no false connecting line.
    fig,ax=plt.subplots(figsize=(6.6,4.4))
    for a,b in [(-4,.98),(1.02,6)]:
        xx=np.linspace(a,b,1000);ax.plot(xx,1/(xx-1),color='C0')
    ax.axvline(1,color='C1',linestyle='--',label='x=1 asymptote')
    ax.axhline(0,color='gray',linestyle=':');ax.set(xlim=(-4,6),ylim=(-8,8),xlabel='x',ylabel='y',title=r'$y=1/(x-1)$');ax.legend();ax.grid(alpha=.2);save(fig,out,'rational_asymptote')
    # Unit circle exact geometry.
    theta=np.linspace(0,2*np.pi,500);a=np.pi/6
    fig,ax=plt.subplots(figsize=(5.2,5.2));ax.plot(np.cos(theta),np.sin(theta));ax.plot([0,np.cos(a)],[0,np.sin(a)],'C1-');ax.scatter([np.cos(a)],[np.sin(a)],color='C1');ax.annotate(r'$(\sqrt{3}/2,1/2)$',xy=(np.cos(a),np.sin(a)),xytext=(-110,65),textcoords='offset points',arrowprops={'arrowstyle':'->','color':'0.35'});ax.axhline(0,color='gray',lw=.8);ax.axvline(0,color='gray',lw=.8);ax.set(aspect='equal',xlim=(-1.25,1.25),ylim=(-1.25,1.25),title='Unit circle, angle 30 degrees');ax.grid(alpha=.15);save(fig,out,'unit_circle')
    # Binomial PMF, explicitly a theoretical model, not observed data.
    n,p=10,.3;k=np.arange(n+1);pmf=np.array([comb(n,int(i))*p**i*(1-p)**(n-i) for i in k]);assert abs(pmf.sum()-1)<1e-12
    fig,ax=plt.subplots(figsize=(6.6,4.4));ax.bar(k,pmf);ax.set(xlabel='k successes',ylabel='P(X=k)',title='Theoretical Binomial(n=10, p=0.3)');ax.set_xticks(k);save(fig,out,'binomial_pmf')
    print(f'Generated four plots (PDF and PNG) in {out}')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=Path('examples/figures'));args=parser.parse_args();main(args.out)
