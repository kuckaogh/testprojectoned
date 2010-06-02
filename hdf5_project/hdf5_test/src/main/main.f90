PROGRAM fortran_call_c

use hdf5_C_interface


implicit none
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