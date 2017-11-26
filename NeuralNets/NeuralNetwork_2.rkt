#| Copyright 2017 Darius Barbano

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. |#

#lang racket
(require math/matrix) ; -> https://docs.racket-lang.org/math/matrices.html

(define (generate_matrix size) 0) ;how can i do this in racket?

(define (transform_input input matrix) ;perform matrix multiplication to apply the permutation
    (matrix* matrix input))

(define test_matrix (matrix ( ;this test matrix was defined in the section titled 'Addition/Subtraction network with input permutations'
    [0 0 0 0 0 1 0]
    [0 0 0 1 0 0 0]
    [0 1 0 0 0 0 0]
    [1 0 0 0 0 0 0]
    [0 0 1 0 0 0 0]
    [0 0 0 0 1 0 0]
    [0 0 0 0 0 0 1]
)))

; since we use racket's matrix library, we need to represent + as '-1' and - as '-2'
(transform_input (col-matrix [1 -1 2 -1 3 -2 4]) test_matrix) ; transform the expression 1 + 2 + 3 - 4
; result is '-2 -1 -1 1 2 3 4', which represents - + + 1 2 3 4
