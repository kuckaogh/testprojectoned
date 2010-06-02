MODULE hdf5_C_interface
IMPLICIT NONE
! Declare the interface for the C routine we'll call
!
INTERFACE
    ! The BIND(C) tells the compiler that this is an "interoperable"
    ! procedure.  The compiler adjusts the naming conventions as
    ! appropriate for the companion C processor.
    SUBROUTINE c_routine (int_arg, int_array, str_in, str_out) BIND(C)
       USE,INTRINSIC :: ISO_C_BINDING  ! Declares C kinds

       ! First argument is a C "int", passed by value
       INTEGER(C_INT), VALUE,INTENT(IN) :: int_arg
       INTEGER(C_INT), INTENT(IN) :: int_array(1:2)
       ! Second and third arguments are C "char *", represented
       ! in Fortran by an array of single characters of kind C_CHAR.
       ! Note that the language allows passing a regular CHARACTER
       ! variable to such an argument.
       CHARACTER(KIND=C_CHAR),DIMENSION(*) :: str_in,str_out
    END SUBROUTINE c_routine

    SUBROUTINE testhdf( float_array, size_float_array ) BIND(C)
       USE,INTRINSIC :: ISO_C_BINDING  ! Declares C kinds
       REAL(C_FLOAT), DIMENSION(*), INTENT(IN) :: float_array
       INTEGER(C_INT), VALUE,INTENT(IN) :: size_float_array
    END SUBROUTINE testhdf

END INTERFACE

END MODULE

