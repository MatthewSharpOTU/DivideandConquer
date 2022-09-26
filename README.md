# DivideandConquer
Practice Assignment From CSCI3070U

Part 1) Implement the merge sort using a programming language (python is favourable). Report the runtime for arrays with different sizes 

Elements Checked: <br />
Array Size n = 1,000      ==> Sorting Time 0.0020015 Seconds <br />
Array Size n = 10,000     ==> Sorting Time 0.0370011 Seconds <br />
Array Size n = 100,000    ==> Sorting Time 0.3799986 Seconds <br />
Array Size n = 1,000,000  ==> Sorting Time 4.6810364 Seconds 

Part 2) Solve the following recurrent equations using the master theorem:

T(n) = 8 T(n/3) + n2            ==> T(n) = Θ(n<sup>2</sup>)

T(n) = 10 T(n/3) + n2           ==> T(n) =  Θ(n<sup>log</sup><sub>3</sub><sup>10</sup>)

T (n) = 16 T (n/4) + n2 log3 n  ==> T(n) =  Θ(n<sup>2</sup>log<sub>2</sub><sup>4</sup>(n))

T (n) = 9 T (n/3) + n3          ==> T(n) =  Θ(n<sup>3</sup>)
