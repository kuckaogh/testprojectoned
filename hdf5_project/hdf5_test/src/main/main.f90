PROGRAM fortran_call_c
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

CHARACTER(80) OUTPUT_TEXT
INTEGER IN_ARG, int_array(2), OUTPUT_LEN,i
CHARACTER(80) INPUT_TEXT
INTEGER :: size_float_array
PARAMETER (size_float_array = 40)
REAL, DIMENSION(size_float_array) :: float_array


INPUT_TEXT = "Testing..."C ! C suffix adds a null terminator
IN_ARG = 123
int_array(1) = 321
int_array(2) = 678


do i=1,size_float_array
   float_array(i) = 3.1415926*i
enddo
! Call c_routine. It will return text in OUTPUT_TEXT
!
CALL c_routine (in_arg, int_array, input_text, output_text)

! Find the length of the output text, looking
! for the trailing blank
!
OUTPUT_LEN = INDEX(OUTPUT_TEXT," ")
IF (OUTPUT_LEN == 0) OUTPUT_LEN = 80

! Write the string to the console
!
WRITE (*,*) OUTPUT_TEXT(1:OUTPUT_LEN)
pause
CALL testhdf (float_array,size_float_array)

END