# An Explicit Hamming-Coset Construction for Perfect Codes in Generalized Fibonacci Cubes

**Research No.84 | Ryutaro Yonezu | Independent Researcher**  
**Preprint candidate, version 1.0 | 24 November 2026**  
**Not human peer-reviewed. Independent AI-assisted mathematical audit: PASS (reported scope). Windows reproduction: PASS (author-provided transcript).**  
**Novelty: INCONCLUSIVE. References: PARTIAL. All rights reserved.**

## Abstract
For every integer p >= 3, we explicitly construct a binary 1-perfect code in the generalized Fibonacci cube Q_n(1^s), where n = 2^p - 1 and s = 3*2^(p-2) - 1. The same code works for each larger forbidden run length s'. The construction selects a coset of the classical binary Hamming code and orders its parity-check columns so that the syndrome of any word containing a forbidden run lies in one of two proper hyperplanes, while the chosen target syndrome belongs to neither. The sufficient condition is one below the bound s >= 3*2^(p-2) established in Mollard (2018). The p=3 case is explicitly known in that work; potential novelty for p>=4 remains unconfirmed. No minimality of s is claimed.

## 1. Definitions and theorem
Let Q_n denote the n-dimensional binary hypercube. Write Q_n(1^s) for the subgraph induced on length-n binary words containing no run of s consecutive ones. A subset C of the vertex set is a 1-perfect code if the closed graph-distance-one neighborhoods of its codewords form a partition of the vertices.

**Theorem.** For every integer p >= 3, set n = 2^p - 1 and s = 3*2^(p-2) - 1. Then Q_n(1^s) admits a 1-perfect code. The same code is a 1-perfect code in Q_n(1^{s'}) for every s' >= s (with the usual interpretation when s' > n).

## 2. Explicit construction
Identify F_2^p with p-bit integer masks, with bit positions counted from 0. Put t = 2^(p-2), W = {0,...,t-1}, H = {0,...,2t-1}, v = 2t and b = 3t. The space W is a codimension-two linear subspace; H is the hyperplane of vectors with top bit zero.

Take a p-by-n binary parity-check matrix M whose ordered columns are:

1. All elements of W except zero, in any order (t-1 columns).
2. The single vector v (one column).
3. All vectors having top bit one except v, in any order (2t-1 columns).
4. All elements of H outside W, in any order (t columns).

Thus every nonzero member of F_2^p occurs exactly once. Define C = {x in F_2^n : Mx = b}, with matrix operations over F_2.

## 3. Proof
Because the columns of M are exactly the distinct nonzero p-bit vectors, for each word y the n+1 syndromes My and M(y+e_j), j=1,...,n, cover all 2^p possible syndromes without repetition. Hence exactly one element of the closed Hamming-radius-one ball about y belongs to C. The set C is an ambient binary 1-perfect code and has 2^(n-p) codewords.

Now s = n-t. Any consecutive forbidden block of s ones starts after i initial positions, where 0 <= i <= t. Its complementary positions consist of the first i and final t-i columns. When i < t, all these outside columns lie in H: the first i come from W and the last t-i come from H outside W. When i = t, the outside columns are the first t columns, lying in H' = span(W,v), another hyperplane.

The XOR of all nonzero vectors in F_2^p equals zero for p >= 2. Therefore the XOR of all columns inside the forbidden block equals that of all columns outside it. If a word x has ones at all forbidden block positions, Mx is consequently a sum of some of the outside columns and belongs to H (if i < t) or H' (if i = t).

But b = 3t has both top two bits equal to one. In particular, b is outside H (top bit zero) and outside H' (second-top bit zero). Thus no x in C contains the forbidden block. Every codeword belongs to Q_n(1^s).

For every allowed vertex y, its unique ambient codeword c at Hamming distance at most one is allowed, as C contains no forbidden word. If y and c differ by one bit, the hypercube edge between them remains in the induced subgraph. Thus the closed neighborhoods of C partition the vertices of Q_n(1^s), establishing the theorem. If s' >= s, every word avoiding a run of s ones also avoids a run of s' ones; the same ambient perfect code C stays inside the smaller allowable vertex set. QED.

## 4. Verification and limits
The accompanying standard-library Python script checks all hyperplane witness conditions for p=3,...,10, and enumerates all ambient vertices for p=3,4, checking exclusive coverage. An author-provided Windows PowerShell transcript records these checks passing with Python 3.12. The independent AI auditor separately rederived the proof; for p=3,4 it exhaustively checked 30 internal permutations of each column group, and for p=5 it reported three enumerations of all 2^31 binary words, finding no forbidden codewords among 67,108,864 syndrome-b words. This is AI-assisted verification, not human peer review. The general assertion follows from Section 3, not induction from finite runs.

The auditor also reported that for its p=4 construction, reducing s from 11 to 10 yields four codewords containing an all-one run of length 10. This only limits that particular construction, and does not prove nonexistence of other codes at shorter run lengths.

## 5. Prior art and novelty limitation
Mollard (2018), Theorem 2.2 and Corollary 2.3, establishes an existence condition s >= 3*2^(p-2). Its concluding remarks already describe a code for n=7, s=5 and mention possible translations of Hamming codes. The present explicit construction establishes existence at s = 3*2^(p-2)-1, outside that stated general sufficient condition. An exhaustive search for equivalent results and a proof of a globally minimal s have not been completed. Consequently the claim is a mathematical construction with novelty INCONCLUSIVE; no assertion of priority or optimality is made.

## Reference
Michel Mollard, *The existence of perfect codes in a family of generalized Fibonacci cubes*, Information Processing Letters 140 (2018), 1-3. DOI: 10.1016/j.ipl.2018.07.010. Preprint: https://arxiv.org/abs/1801.04106.

## Reproducibility and rights
Audit report: NO84_INDEPENDENT_AUDIT_REPORT_JA_20261124.md. Author Windows transcript: WINDOWS_VERIFICATION_AUTHOR_TRANSCRIPT.txt. The included script and all files have SHA256 hashes in SHA256SUMS.txt. All rights reserved; no open-source license is granted by publication. This manuscript is a non-peer-reviewed preprint candidate and is not yet publicly released.
