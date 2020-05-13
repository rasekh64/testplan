#include "udf.h"
#define WALLID 25 /* Take care that you list the correct value here */
#define F_NAME "Force_yarn_reed_10mbar_point8_speed_70.txt"

DEFINE_ON_DEMAND(store_data)
{
	Message("\nUDF store_data started., %i\n",myid);
	int i;
	int n_faces;
  	real x[ND_ND], (*x_array)[ND_ND];
	real (*pF_array)[ND_ND];
	real (*vF_array)[ND_ND];
	real (*Ac_array)[ND_ND];
	real *p_array;
	
#if !RP_HOST
	Message("\nHere_A, %i\n",myid);	
	Domain *domain = Get_Domain(1);
	Thread *face_thread = Lookup_Thread(domain, WALLID);
	face_t face;
	Message("\nHere_B, %i\n",myid);	
#endif /* !RP_HOST */
	

#if PARALLEL
	Message("PARALLEL, %i",myid);
	int compute_node; 
#endif /* PARALLEL */


#if !RP_NODE /* SERIAL or HOST */
	FILE *fp;
	char filename[]=F_NAME;
	fp = fopen(filename, "w");
	Message("\nWriting data to %s...,%i \n",filename,myid);
#endif /* !RP_NODE */

	
#if !RP_HOST
	Message(" Collecting data on faces...%i\n",myid);
	
	n_faces = THREAD_N_ELEMENTS_INT(face_thread);
	
	x_array=(real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));
	pF_array = (real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));
	vF_array = (real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));
	Ac_array = (real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));
	p_array=(real * )malloc(n_faces*sizeof(real));

	begin_f_loop(face, face_thread)
	{
		if (PRINCIPAL_FACE_P(face, face_thread)) 
   		{

	    		F_CENTROID(x_array[face], face, face_thread);

			F_AREA(Ac_array[face],face,face_thread);
     			NV_VS(vF_array[face], =, F_STORAGE_R_N3V(face,face_thread,SV_WALL_SHEAR),*,-1.0);

     			pF_array[face][0]=F_P(face,face_thread)*Ac_array[face][0];
     			pF_array[face][1]=F_P(face,face_thread)*Ac_array[face][1];
     			pF_array[face][2]=F_P(face,face_thread)*Ac_array[face][2];

   		}  

		p_array[face] = F_P(face, face_thread);
	} 
	end_f_loop(face, face_thread);
#endif /* !RP_HOST */	

	
#if RP_NODE	
	Message(" Sending data to node 0...,%i\n",myid);
	
	compute_node = (I_AM_NODE_ZERO_P) ? node_host : node_zero;
	/* send to 
	- if compute_node = node_zero: node-zero sends data to the host
	- if compute_node is not node_zero: the node sends data to node_zero
	*/
	PRF_CSEND_INT(compute_node, &n_faces, 1, myid); /* send pointer to n_faces */	
	PRF_CSEND_REAL(compute_node, p_array, n_faces, myid); /* send pointer to p_array */
	PRF_CSEND_REAL(compute_node, x_array[0], ND_ND*n_faces, myid); /* send pointer to x_array */
	PRF_CSEND_REAL(compute_node, pF_array[0], ND_ND*n_faces, myid); 
	PRF_CSEND_REAL(compute_node, vF_array[0], ND_ND*n_faces, myid);
	PRF_CSEND_REAL(compute_node, Ac_array[0], ND_ND*n_faces, myid); 
	 	

	free(p_array); /* free array after data sent */
	free(x_array);
	free(pF_array);
	free(vF_array);
	free(Ac_array);

		
	
	Message(" Receiving data on node 0 and sending to host..., %i\n",myid);
	/*
	Now node_zero has to receive the data from the other nodes, and
	redirect it to the host. Therefore, node_zero loops over all other
	nodes. First, the size of the p_array is stored in n_faces, so that 
	enough space can be allocated. Then the received data is stored in 
	p_array, and immediately send onward to the host. At the end, p_array
	is freed.
	*/
	if(I_AM_NODE_ZERO_P)
	{
	Message(" I am node 0...,%i\n",myid);
		compute_node_loop_not_zero(compute_node)
		{
			PRF_CRECV_INT(compute_node, &n_faces, 1, compute_node);
			p_array=(real * )malloc(n_faces*sizeof(real));
			x_array=(real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));
			pF_array=(real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));
			vF_array=(real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));
			Ac_array=(real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));	
			
			PRF_CRECV_REAL(compute_node, p_array, n_faces, compute_node);
			PRF_CRECV_REAL(compute_node, x_array[0], ND_ND*n_faces, compute_node);
			PRF_CRECV_REAL(compute_node, pF_array[0], ND_ND*n_faces, compute_node);
			PRF_CRECV_REAL(compute_node, vF_array[0], ND_ND*n_faces, compute_node);
			PRF_CRECV_REAL(compute_node, Ac_array[0], ND_ND*n_faces, compute_node);
			
			PRF_CSEND_INT(node_host, &n_faces, 1, compute_node);
			PRF_CSEND_REAL(node_host, p_array, n_faces, compute_node);
			PRF_CSEND_REAL(node_host, x_array[0], ND_ND*n_faces, compute_node);
			PRF_CSEND_REAL(node_host, pF_array[0], ND_ND*n_faces, compute_node);
			PRF_CSEND_REAL(node_host, vF_array[0], ND_ND*n_faces, compute_node);
			PRF_CSEND_REAL(node_host, Ac_array[0], ND_ND*n_faces, compute_node);

			free(p_array);
			free(x_array);	
			free(pF_array);
			free(vF_array);
			free(Ac_array);
		}
	}
#endif /* RP_NODE */


#if !RP_NODE /* Print data to file */
#if RP_HOST	/* Receive data on host before printing */
	Message(" Receiving data on host..., %i\n",myid);
	fprintf(fp, "x  y  z  p_Fx  p_Fy  p_Fz  viscous_Fx  vicous_Fy  viscous_Fz Ax Ay Ay p \n");
	compute_node_loop (compute_node)
	{
		Message(" In loop at node %i ; %i\n", compute_node, myid);
		PRF_CRECV_INT(node_zero, &n_faces, 1, compute_node);

		Message(" In loop at node %i B; %i\n", compute_node, myid);
		p_array=(real * )malloc(n_faces*sizeof(real));
		x_array=(real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));
		pF_array=(real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));
		vF_array=(real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));
		Ac_array=(real (*)[ND_ND])malloc(ND_ND*n_faces*sizeof(real));
		
		Message(" In loop at node %i C; %i\n", compute_node, myid);
		PRF_CRECV_REAL(node_zero, p_array, n_faces, compute_node);
		PRF_CRECV_REAL(node_zero, x_array[0], ND_ND*n_faces, compute_node);
		PRF_CRECV_REAL(node_zero, pF_array[0], ND_ND*n_faces, compute_node);
		PRF_CRECV_REAL(node_zero, vF_array[0], ND_ND*n_faces, compute_node);
		PRF_CRECV_REAL(node_zero, Ac_array[0], ND_ND*n_faces, compute_node);
		
		Message(" In loop at node %i D; %i\n", compute_node, myid);
#endif /* RP_HOST */
		
		Message(" Printing data to files...\n");

		for (i=0; i<n_faces; i++)
		{
			fprintf(fp, "%12.4e %12.4e %12.4e %12.4e %12.4e %12.4e %12.4e %12.4e %12.4e %12.4e %12.4e %12.4e %12.4e\n",x_array[i][0], x_array[i][1], x_array[i][2], pF_array[i][0], pF_array[i][1], pF_array[i][2], vF_array[i][0], vF_array[i][1], vF_array[i][2], Ac_array[i][0], Ac_array[i][1], Ac_array[i][2], p_array[i]);
		}
		free(p_array);
		free(x_array);
		free(pF_array);
		free(vF_array);
		free(Ac_array);

#if RP_HOST /* Close compute_node_loop */
	} 
#endif /* RP_HOST */
	fclose(fp);
#endif /* !RP_NODE */

	Message("UDF store_data finished.\n");
}
