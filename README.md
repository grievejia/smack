SMACK is a tool for statically checking properties of programs written in
C/C++. For a given input program, SMACK checks for violations of user-provided
assertions. The tool is open-source and integrates into the well-known LLVM
compiler infrastructure. Therefore, SMACK can (at least in theory) check any
program that can be compiled with LLVM. It should also be relatively easy to
implement and try out different extensions on top of SMACK.


## SMACK Dependencies

* [LLVM 3.2](www.llvm.org)
* [clang](http://clang.llvm.org)
* [Boogie](http://boogie.codeplex.com)
* [Python](http://www.python.org)


## Installing SMACK

1. Checkout SMACK:

   ```
   cd where-you-want-smack-source-to-live  
   git clone git@github.com:smackers/smack.git
   ```

2. Configure SMACK:

   ```
   cd where-you-want-to-build-smack
   mkdir build (for building without polluting the source dir)
   cd build
   ../smack/configure --with-llvmsrc=<directory> --with-llvmobj=<directory> --prefix=<directory>
   ```

   Options for configure are:
   * --with-llvmsrc=<directory>  : Tell SMACK where the LLVM source tree is located [required].
   * --with-llvmobj=<directory>  : Tell SMACK where the LLVM object tree is located [required].
   * --prefix=<directory>        : Specify full pathname of where you want SMACK installed [required].
   * --enable-optimized          : Compile with optimizations enabled [default is NO].
   * --enable-assertions         : Compile with assertion checks enabled [default is YES].

3. Build SMACK:

   ```
   make
   ```

   If everything goes well, you should now have lib/libsmack.a and lib/smack.so in
   the SMACK installation directory.

4. Copy SMACK's bin scripts to the installation directory:

   ```
   cp -r smack-source-dir/bin smack-install-dir
   ```
   Then add smack-install-dir/bin to your path.

**NOTE:**
Boogie, clang, and llvm binaries (e.g. llvm-link, opt, etc.) should be in
your path, as well as smack-install-dir/bin directory!  
In particular, for smack.py to work correctly, one should be able to
invoke Boogie on your system just by typing 'boogie' in the command line.
Creating an alias as suggested in the Boogie installation manual will not
work with smack.py. Instead, a simple solution on a Unix-like system is
putting the following script in your path and naming it 'boogie':
```
#!/bin/bash
mono <path_to_Boogie.exe> $1 $2 $3 $4 $5 $6 $7 $8 $9
```


## Running Regression Tests

To make sure SMACK has been installed properly, run its regression tests.

First, go to the smack/headers directory and compile smack.c (used for
defining SMACK-specific functions) using the provided Makefile by running
`make llvm`.

Then, go to smack/test directory and compile the regression tests by running
`make`. You should get a number of LLVM bitcode files, one per test.

Execute the regression test script with `./regtest.py`. All tests should pass.


## Running SMACK

Try SMACK on a simple example in the smack/examples/simple directory.

First, go to the smack/headers directory and compile smack.c (used for
defining SMACK-specific functions) using the provided Makefile by running
`make llvm`.

Then, go to smack/examples/simple directory and compile the examples by running
`make llvm`. You should get a number of LLVM's bc files, one per example.

Run SMACK on examples, for instance:
```
smack.py simple
smack.py simple_fail
```
