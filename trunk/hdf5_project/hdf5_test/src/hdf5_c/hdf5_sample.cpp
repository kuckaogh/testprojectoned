#include "hdf5.h"
#include "hdf5_hl.h"

#define RANK 2
int testhdf();

int main( void )
{
int errorCode;
	
errorCode = testhdf();
}


int testhdf()
{
 hid_t       file_id;
 hsize_t     dims[RANK]={2,3};
 int         data[6]={1,2,3,4,5,6};
 herr_t      status;

 /* create a HDF5 file */
 file_id = H5Fcreate ("ex_lite1.h5", H5F_ACC_TRUNC, H5P_DEFAULT, H5P_DEFAULT);

 /* create and write an integer type dataset named "dset" */
 status = H5LTmake_dataset(file_id,"/dset",RANK,dims,H5T_NATIVE_INT,data);

 /* close file */
 status = H5Fclose (file_id);

 return 0;
}