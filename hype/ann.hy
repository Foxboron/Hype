(import [annotation.typed [typechecked]])
(import [annotation.typed [*]])


(defn AddAnnotations [ann]
  (defn _ [fn]
    (def fn-args fn.--code--.co-varnames)
    (def ret-ann (if (in :-> ann) (first (slice ann (+ 1 (.index ann :->))))))
    (def ann-args (dict (zip fn-args (slice ann 0 (len fn-args)))))
    (if ret-ann (assoc ann-args "return" ret-ann))
    (setv fn.--annotations-- ann-args)
    (typechecked fn))
  _)


(defmacro ann [sym args]
  "Define function annotations over a function"
  `(defmacro defn [name lambda-list &rest body]
     (import hy.models.list)
     (def a (hy.models.list.HyList '~args))
     (if (= '~sym name)
       `(do (import [hype.ann [AddAnnotations]])  
          (with-decorator (AddAnnotations ~a) (setv ~name (fn ~lambda-list ~@body))))  
       `(setv ~name (fn ~lambda-list ~@body))))
)


