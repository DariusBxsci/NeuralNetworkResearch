#lang racket

;(define ns (make-base-namespace)) ;namespace necessary to use eval properly

(define-namespace-anchor a)
(define ns (namespace-anchor->namespace a))

;eval function is explained here: https://docs.racket-lang.org/guide/eval.html
(define (evaluate operation val1 val2) ;evaluate the result of either addition or subtraction of two values
    (define o operation)
    (define x val1)
    (define y val2)
    (eval `(,operation ,x ,y) ns))

(evaluate + 5 4)
