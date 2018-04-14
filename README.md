# Google Code Jam

My solutions to [Google Code Jam](https://code.google.com/codejam)  
Mainly solved the [problems](https://code.google.com/codejam/past-contests) with *Python* and *C++*.


## Contents


### Code Jam

* 2018
   * [Practice Round](https://codejam.withgoogle.com/2018/challenges/0000000000000130/dashboard) - Solved A
   * [Qualification Round](https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard) - Solved A/B/C/D
   * [Round 1A](https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard) - Solved A/B


### Kickstart

* 2017
   * [Practice Round](https://code.google.com/codejam/contest/6304486/dashboard) - Solved A/B/C
   * [Round B](https://code.google.com/codejam/contest/11304486/dashboard) - Solved A
   * [Practice Round 2](https://code.google.com/codejam/contest/12254486/dashboard) - Solved A

* 2018
   * [Practice Round](https://code.google.com/codejam/contest/4374486/dashboard) - Solved A/B/C/D
   * [Round A](https://code.google.com/codejam/contest/9234486/dashboard) - Solved A/B/C


## Tips


### Templates for Competative Programming

Some useful templates for competative programming: see [here](https://github.com/elvisyjlin/google-code-jam/tree/master/Templates).


### To Run Your Code in One Line

On Linux or macOS

```bash
python3 A.py < A-sample.in > A-sample.out
g++ A.cpp -std=c++11 && ./a < A-sample.in > A-sample.out
```

On Windows

```bash
python3 A.py < A-sample.in > A-sample.out
g++ A.cpp -std=c++11 && a < A-sample.in > A-sample.out
```

If you're system doesn't have `<bits/stdc++.h>` (e.g. macOS), you can download one 
[here](https://gist.github.com/elvisyjlin/06b8125d81dc213a2c37e5cdebc18bf3). 
Then include it as `#include "[YOUR PATH]/stdc++.h"` at the beginning of your code.