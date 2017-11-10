#lang racket

;string manipulation
(substring "Hello World!" 0)
(substring "Hello World!" 1)
(substring "Hello World!" 1 10)
(substring "Hello World!" 6 11)
(substring "Hello World!" 0 5)

;functions
(define (allButFirst str)
  (substring str 1))
(allButFirst "mmy string")

;user input
(define (getInputForFunction)
  (allButFirst (read-line (current-input-port))))
;(getInputForFunction)

;evaluation
(define (eval)
  string-append "eval" "uation")
(eval) ;only the result of the final expression "uation" is used since there are no parenteses around the string-append call

; are invalid within identifiers  ( ) [ ] { } " , ' ` ; # | \
; but many other symbols are fine
(define (d?u!m+m-y*)
  "hi")
(d?u!m+m-y*)

;useful functions
(string-append "rope" "twine" "yarn")  ; append strings
(substring "corduroys" 0 4)            ; extract a substring
(string-length "shoelace")             ; get a string's length
(string? "Is this a string?") ; recognize strings
(sqrt 16)                              ; find a square root
(sqrt -16)                             ; works with imaginary nums
(+ 1 2)                                ; add numbers (prefix notation)
(< 2 1)                                ; compare numbers (prefix notation)
(number? "Is this a number?")           ; recognize numbers
(equal? 6 "half dozen")                ; compare anything

;conditionals
(define (getLarger a b)
  (if (>= a b)
      a
      b))
(getLarger 4 3)

(define (reply s)
  (if (if (string? s)
          (equal? "hello" (substring s 0 5))
          #f)
      "hi!"
      "huh?"))
(reply "hello world!")
(reply "2342341")

(define (HelloOrWorld str)
  (if (or (equal? str "Hello") (equal? str "World"))
      "Hi!"
      "What?"))
(HelloOrWorld "Hello")
(HelloOrWorld "World")
(HelloOrWorld "Bye!")

;vectors
(vector 1 2 3)
(equal? (vector 1 2 3) (vector 1 2 4))
(equal? (vector 1 2 3) (vector 1 2 3))