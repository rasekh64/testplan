(custom-field-function/define
 '(((name density_x_vz) (display " - 1 * density * Vz") (syntax-tree ("*" ("*" -1 "density") "z-velocity")) (code (field-* (field-* -1 (field-load "density")) (field-load "z-velocity"))))
   ))
