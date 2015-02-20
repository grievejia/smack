//
// This file is distributed under the MIT License. See LICENSE for details.
//
#ifndef SMACK_H_
#define SMACK_H_

/**
 * The SMACK "prelude" declarations
 */

#ifdef __cplusplus
extern "C" {
#endif

void __SMACK_code(const char *fmt, ...);
void __SMACK_mod(const char *fmt, ...);
void __SMACK_decl(const char *fmt, ...);
void __SMACK_top_decl(const char *fmt, ...);

// We need this to enforce that assert/assume are function calls
// with an integer argument (DSA gets confused otherwise)
__attribute__((always_inline)) void __SMACK_dummy(int v);

#ifdef BITVECTOR
#define assert(EX) __SMACK_dummy(EX); __SMACK_code("assert @ != 0bv32;", EX)
#define assume(EX) __SMACK_dummy(EX); __SMACK_code("assume @ != 0bv32;", EX)
#else
#define assert(EX) __SMACK_dummy(EX); __SMACK_code("assert @ != 0;", EX)
#define assume(EX) __SMACK_dummy(EX); __SMACK_code("assume @ != 0;", EX)
#endif

int __SMACK_nondet();

void __SMACK_decls();

#ifdef __cplusplus
}
#endif

#endif /*SMACK_H_*/
