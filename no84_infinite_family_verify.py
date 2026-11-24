"""No84 infinite-family algebraic construction test (standard-library only)."""
def construct(p):
    assert p>=3
    t=1<<(p-2); n=(1<<p)-1
    W=list(range(1,t))
    H_tail=list(range(t,2*t))
    v=1<<(p-1)
    middle=[x for x in range(1,1<<p) if x not in set(W+[v]+H_tail)]
    cols=W+[v]+middle+H_tail
    b=(1<<(p-1)) | (1<<(p-2))
    assert len(cols)==n and sorted(cols)==list(range(1,n+1))
    return cols,b,n-t

def dot(x,y): return (x&y).bit_count()%2

def algebra(p):
    cols,b,s=construct(p); n=len(cols);t=n-s
    A=1<<(p-1);B=1<<(p-2)
    for i in range(t+1):
        outside=cols[:i]+cols[i+s:]
        witness=A if i<t else B
        assert all(dot(witness,x)==0 for x in outside),(p,i)
        assert dot(witness,b)==1,(p,i)
    assert __import__('functools').reduce(lambda a,x:a^x,cols,0)==0
    print(f'p={p} n={n} s={s} HYPERPLANE_CERTIFICATE PASS ({t+1} blocks)')
    if n<=15:
        code=[x for x in range(1<<n) if __import__('functools').reduce(lambda a,j:a^cols[j] if x>>j&1 else a,range(n),0)==b]
        assert len(code)==(1<<n)//(n+1)
        for x in code:
            assert not any(((x>>i)&((1<<s)-1))==((1<<s)-1) for i in range(n-s+1))
        covered=bytearray(1<<n)
        for x in code:
            for y in [x]+[x^(1<<j) for j in range(n)]:
                assert not covered[y];covered[y]=1
        assert all(covered)
        print(f'  EXHAUSTIVE PASS: codewords={len(code)}, covered={sum(covered)}')
for p in range(3,11): algebra(p)
