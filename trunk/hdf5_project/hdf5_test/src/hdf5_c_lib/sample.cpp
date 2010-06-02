#include <stdio.h>
#include "hdf5.h"
#include "hdf5_hl.h"
#define RANK2 2
#define RANK1 1
extern "C" void c_routine (
                        int int_arg_by_val,
						int int_array[2],
                        char* input_text,
                        char* output_text
                        )

{
	int n1 = int_array[0];
	int n2 =  int_array[1];
    sprintf(output_text,"%s%i%s%i",input_text,n1,"_", n2);
}

extern "C" void testhdf(float* data_float, int size_data_float)
{
 hid_t       file_id;
 hsize_t     dims[RANK2]={2,3};
 int         data[6]={1,2,3,4,5,6};
 herr_t      status;
 hsize_t     dims4[RANK1]={size_data_float};

 /* create a HDF5 file */
 file_id = H5Fcreate ("calledFromFortran.h5", H5F_ACC_TRUNC, H5P_DEFAULT, H5P_DEFAULT);

 /* create and write an integer type dataset named "dset" */
 status = H5LTmake_dataset(file_id,"/dset",RANK2,dims,H5T_NATIVE_INT,data);
 status = H5LTmake_dataset(file_id,"/another",RANK1,dims4,H5T_NATIVE_FLOAT,data_float);

 /* close file */
 status = H5Fclose (file_id);

 //return 0;
}