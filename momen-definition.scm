(custom-field-function/define
 '(((name momen) (display "density * (axial-velocity) ^ 2") (syntax-tree ("*" "density" ("**" "axial-velocity" 2))) (code (field-* (field-load "density") (field-** (field-load "axial-velocity") 2))))
   ))
