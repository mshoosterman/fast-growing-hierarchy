# fast-growing-hierarchy
An attempt at a python implementation of the Wainer fast growing hierarchy

An explanation of what a fast-growing hierarchy is can be found here: 
https://en.wikipedia.org/wiki/Fast-growing_hierarchy#:~:text=In%20computability%20theory%2C%20computational%20complexity,to%20some%20large%20countable%20ordinal).

This is an ordinal indexed family of computable functions that follow a fairly simple recusrive algorithm to produce a hierarchy of very fast growing functions. Given the fact that this family is supposedly computable, I wanted to write some code that should in theory be able to compute it. Of course for almost all impute values this function will never return any value as the runetime will be far too long. 

The current implementation should be completely functional, but lacks all possible luxuries to make it nice to actually play around with. Partly because of that the code is stil untested. An easy test to preform is that for any ordinal input, if the number 2 is input, the result should be 4. 

Somethings that are left to be done include: 

Finishing defining __contains__ in the Ordinal class. Because this class is meant to represent ordinals, I want to use contains instead of inequalities. (Inequalities may be defined later interms of containment). 

Finish the initializer for the Ordinal class. The current initializer is functional, but does no error prevention or checking. It will happily accept invalid ordinals. This requires finishing the definition of __contains__ to fix, since one thing the initializer needs to check for is that the list given as an argument is actually in decending order. 

Add Constant functions to easily specify some particular ordinals. 

Add a helper function to easily specify finite ordinals. (An integer to Ordinal function). 

Add 3 other versions of the fast growing hierarchy. The way the fast function works is that fast(0, n) = n+1, fast(1, n) = n+n, fast(2, n) = n*n, fast(3, n) = n^n etc. 
Despite the fact that n+n, n*n, and n^n is something python is happily able to compute in a relatively efficient way, fast() does not care, and does this in the least efficient way possible. There is no real good reason to make fast more efficient, since no matter what, almost all inputs will have prohibitively long runtimes, but at the same time there is no reason to be so lazy and not implement these simple optimizations. Although for the sake of a aesthetics, the originall definition should stay for fast(), so a new function, or perhaps several should be defined which do the same thing, but apply the optimizations. 

Either modify the Ordinal class, or define a new class to be able to represent the ordinal epsilon_0.

Possibly define a new Ordinal class that goes far beyond epsilon_0. Likely only done after everything else has been addressed. 

Clean code, improve documentation. 
