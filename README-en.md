# contents 
This repository contains some algorithms that are for the defined cases:

<br><br>
* tape : Suppose there is n audio files that should be placed on a tape. Each file with index of i has time duration of length[i] and it is granted that total time of all files is equal to capacity of tape. If sort[i] be the number of file that is placed in index i, the access time of this file is defined as following:
```math
\left( \sum_{k=1}^i L[s(k)]\right)
```
The purpose is to find sort[ ] (the order of audio files on tape) in a way that the mathematical expectation of accessing each file be minimum. Also suppose accessing each file has probability of
```math
\frac{1}{n} 
```

<br><br><br>

* max-task : Suppose there is n tasks, each has a start time and a terminate time. The purpose is to choose as many task as possible so that no two tasks overlap.


<br><br><br>


