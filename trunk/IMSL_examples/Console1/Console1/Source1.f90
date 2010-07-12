! ================ Program start ============== 
    program fnl
! Include the necessary header file:
! For the dynamic library:
!    INCLUDE 'link_f90_dll.h'
! For the static library:
    INCLUDE 'link_fnl_static.h'
!DEC$ OBJCOMMENT lib:"libguide.lib"
!
! Declare which IMSL functions will be used
    USE LSARG_INT
    USE WRRRN_INT
! Declare variables
    PARAMETER (LDA=3, N=3)
    REAL A(LDA,LDA), B(N), X(N)
!
!               Set values for A and B
!
!               A = (33.0 16.0 72.0)
!                   (-24.0 -10.0 -57.0)
!                   (18.0 -11.0 7.0)
!
!               B = (129.0 -96.0 8.5)
!
    DATA A/33.0, -24.0, 18.0, 16.0, -10.0, -11.0, 72.0, -57.0, 7.0/
    DATA B/129.0, -96.0, 8.5/
!
! The main IMSL function call to solve for x in Ax=B.
! This is the floating point version, to use  
! double-precision arguments, call DLSARG.
!
    CALL LSARG(A,B,X)
! 
! Now print the solution x using WRRRN, a printing utility
! 
    CALL WRRRN('X',X,1,N,1)
    pause
    END PROGRAM fnl
! ================ Program End ==============
