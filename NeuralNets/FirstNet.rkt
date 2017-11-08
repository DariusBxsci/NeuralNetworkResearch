#lang racket

;Task: hard-code a simple neual network to either add or subtract two numbers, a and b
; Three input neurons, a, b, and a neuron to indicate which operation is being performed
; One output neuron to represent the result

(define (multiply-list a b) ;multiplies corresponding values of two lists
  (if (empty? a)
      empty
      (cons (* (car a) (car b))
            (multiply-list (cdr a) (cdr b)))))

(define (evaluate inputs weights) ;evaluates result, input and weights are lists
  (apply + (multiply-list (inputs) (weights))))


(define (input) (list 9 5)) ;sample values to test with



   ; ADDITION NET
(define (weight_addition) (list 1 1)) ;weights necessary to perform addition
(evaluate input weight_addition)

   ; SUBTRACTION NET
(define (weight_subtraction) (list 1 -1)) ;weights necessary to perform subtraction
(evaluate input weight_subtraction)



   ; ADDITION/SUBTRACTION NET
(define (weight) (list (* -2 5) 1 1)) ; in this case, the first weight had to be fine-tuned to work for +/- 9 5

(define (input_addition) (list 0 9 5)) ; the first '0' indicates addition
(evaluate input_addition weight)

(define (input_subtraction) (list 1 9 5)) ; the first '1' indicates subtraction
(evaluate input_subtraction weight)

; Conclusion:
;  There is no way, with the current configuration, to configure weights so that both
;  addition and subtraction can be done given any input values. The first weight must
;  be fine-tuned to the values of the two numbers.