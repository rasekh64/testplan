#include "udf.h"
#include "mem.h"
#define COMPRESSIBILITY |compressibility|
#define COMPRESSIBILITYPRINT |compressibilityPrint|
#define end_surface_id 7

#define PREPARE_MEMORY(name) name = NULL

#define DECLARE_MEMORY(name,type) type *name = NULL

#define RELEASE_MEMORY(name)										\
if (NNULLP(name)) {													\
	free(name); 													\
	name = NULL;													\
}

#define ASSIGN_MEMORY(name,size,type) 								\
if (size) {															\
	if (NNULLP(name)) { 											\
		name = (type *)realloc(name, size*sizeof(type));			\
	} else {														\
		name = (type *)malloc(size*sizeof(type));					\
	} 																\
	if (NULLP(name)) {												\
		Error("\nUDF-error: Memory assignment failed for name."); 	\
		exit(1);													\
	}																\
}

typedef struct ring_struct {
	int id;
	real coord[ND_ND];
	real normal[ND_ND];
} Ring;

DEFINE_ON_DEMAND(get_load_beam){
	int i,j;
	Domain *domain;
	int n_rings = 721;
	Ring *CL_pos;
	int surfaceID = 22; /*Surface ID of the surface to retrieve the load, could use an array as in Tango and distinguish for end face */
#if !RP_HOST
	Thread *face_thread;
	face_t face;
	real pressure, shear[ND_ND];
	real area[ND_ND];
	Node *v;
	real Fpx,Fpy,Fpz; /* Force components due to pressure and viscous forces */
	int temp_id, n, nn;
#endif /* !RP_HOST */

#if PARALLEL
	int compute_node, size;
#endif /* PARALLEL */
	DECLARE_MEMORY(array, real);

#if !RP_NODE
	char filename_load[256];
	FILE *file_load;
	int size_bis;
	real dist;
#endif /* !RP_NODE */


	domain = Get_Domain(1);
	/*printf("CL-pos has been read \n");fflush(stdout);*/

	Message0("Looping over faces \n");

#if !RP_HOST
	face_thread = Lookup_Thread(domain, surfaceID);
#endif /* !RP_HOST */

#if !RP_NODE
		sprintf(filename_load, "Test_Output.dat");
		file_load = NULL;
		if ((file_load = fopen(filename_load, "w")) == NULL) {
			Error("\nUDF-error: Unable to open %s for writing\n", filename_load);
			exit(1);
		}
/* Write header for the files */
#if RP_2D
		fprintf(file_load, "%27s%27s%27s\t[N]\n","0-column","x-force","y-force");
#else /* RP_2D */
		fprintf(file_load, "%27s%27s%27s%27s\t[N]\n","0-column","x-force","y-force","z-force");
#endif /* RP_2D */
#endif /* !RP_NODE */

	/*host_to_node_int_1(n_rings);*/

#if PARALLEL
#if RP_NODE
		size = (ND_ND+1)*(n_rings-1); /* Need a 0 column and then 3 force components per ring of faces (one less than rings of nodes)*/
		printf("size = %i \n",size);fflush(stdout);
		ASSIGN_MEMORY(array, size, real);
		/* Initialize array to 0.0 */
		for (i = 0; i < (ND_ND+1)*(n_rings-1); i++){
			array[i]=0.0;
		}
		begin_f_loop_int(face,face_thread) {
			if (PRINCIPAL_FACE_P(face, face_thread)) {
				temp_id = 0;
				nn = 0;
				f_node_loop(face, face_thread,n)
				{
					v = F_NODE(face, face_thread, n);
					temp_id += N_UDMI(v,1);	
					nn += 1;
				}	
				temp_id = floor(temp_id/(float)nn);
				temp_id = (int)(temp_id);
				array[(ND_ND+1)*temp_id] += 0.0; /* Put zero in the first column */
				F_AREA(area, face, face_thread); /* Returns an area vector in the array "area" */
     				Fpx = F_P(face,face_thread)*area[0];
     				Fpy = F_P(face,face_thread)*area[1];
     				Fpz = F_P(face,face_thread)*area[2];	
				real loc[3];
				F_CENTROID(loc,face,face_thread);
				/*printf("x = %f, y= %f, z= %f, p= %f, Fpx = %f, Fpy = %f, Fpz = %f \n",loc[0],loc[1],loc[2],F_P(face,face_thread),Fpx,Fpy,Fpz);fflush(stdout);*/						
				NV_VS(shear, =, F_STORAGE_R_N3V(face, face_thread, SV_WALL_SHEAR), *, -1.0); /* Need force not force per area */
				array[(ND_ND+1)*temp_id+1] += (Fpx + shear[0]);
				array[(ND_ND+1)*temp_id+2] += (Fpy + shear[1]);
				array[(ND_ND+1)*temp_id+3] += (Fpz + shear[2]);
				/*if (temp_id == 9411){
					printf("coord = [%f,%f,%f] \n Area = [%.20f,%.20f,%.20f] \n shear = [%.20f,%.20f,%.20f] \n pressure forces = [%.20f,%.20f,%.20f] \n ",loc[0],loc[1],loc[2],area[0],area[1],area[2],shear[0],shear[1],shear[2],Fpx, Fpy,Fpz);fflush(stdout);
					printf("sum = [%.20f,%.20f,%.20f] \n ----SPLIT ----- \n",array[(ND_ND+1)*temp_id+1],array[(ND_ND+1)*temp_id+2],array[(ND_ND+1)*temp_id+3]);
				}*/
			}
		} end_f_loop_int(face,face_thread)
		printf("core: %i ; after loop \n",myid);fflush(stdout);

		compute_node = (I_AM_NODE_ZERO_P) ? node_host : node_zero;
		PRF_CSEND_INT(compute_node, &size, 1, myid);
		PRF_CSEND_REAL(compute_node, array, size, myid);
		RELEASE_MEMORY(array);

		if (I_AM_NODE_ZERO_P) {
			compute_node_loop_not_zero (compute_node) {
				PRF_CRECV_INT(compute_node, &size, 1, compute_node);
				ASSIGN_MEMORY(array, size, real);
				PRF_CRECV_REAL(compute_node, array, size, compute_node);
				PRF_CSEND_INT(node_host, &size, 1, myid);
				PRF_CSEND_REAL(node_host, array, size, myid);
				RELEASE_MEMORY(array);
			}
		}

#else /* RP_NODE */
		DECLARE_MEMORY(array_sum, real);
		size_bis = (ND_ND+1)*(n_rings-1);
		ASSIGN_MEMORY(array_sum, size_bis, real);
		/* Initialize array to 0.0 */
		for (i = 0; i < size_bis; i++)
			array_sum[i]=0.0;

		compute_node_loop (compute_node) {
			PRF_CRECV_INT(node_zero, &size, 1, node_zero);
			ASSIGN_MEMORY(array, size, real);
			PRF_CRECV_REAL(node_zero, array, size, node_zero);
			for (i = 0; i < size; i++) {
				array_sum[i] += array[i];
			}
			RELEASE_MEMORY(array);
		}
		for (i = 0; i < size_bis/(ND_ND+1); i++) {
			for (j = 0; j < ND_ND; j++)
				fprintf(file_load, "%27.17E", array_sum[(ND_ND+1)*i+j]);
			fprintf(file_load, "%27.17E\n", array_sum[(ND_ND+1)*i+ND_ND]);
		}
#endif /* RP_NODE */
#else /* PARALLEL */
		size = (ND_ND+1)*(n_rings-1);
		begin_f_loop_int(face,face_thread) {
			if (PRINCIPAL_FACE_P(face, face_thread)) {
				temp_id = 0;
				nn = 0;
				f_node_loop(face, face_thread,n)
				{
					v = F_NODE(face, face_thread,n);
					temp_id += N_UDMI(v,1);	
					nn += 1;
				}	
				temp_id = int(floor(temp_id/float(nn)));
				array[(ND_ND+1)*temp_id] += 0.0; /* Put zero in the first column */
				
				F_AREA(area, face, face_thread); /* Returns an area vector in the array "area" */
     				Fpx = F_P(face,face_thread)*area[0];
     				Fpy = F_P(face,face_thread)*area[1];
     				Fpz = F_P(face,face_thread)*area[2];							
				NV_VS(shear, =, F_STORAGE_R_N3V(face, face_thread, SV_WALL_SHEAR), *, -1.0); /* Need force not force per area */
				array[(ND_ND+1)*temp_id+1] += (Fpx + shear[0]);
				array[(ND_ND+1)*temp_id+2] += (Fpy + shear[1]);
				array[(ND_ND+1)*temp_id+3] += (Fpz + shear[2]);
			}
		} end_f_loop_int(face,face_thread)

		for (i = 0; i < size/(ND_ND+1); i++) {
			/* i will correspond to the ring number of the face, this face is in between node ring i and i+1 */
			for (j = 0; j < ND_ND; j++)
				fprintf(file_load, "%27.17E", array[(ND_ND+1)*i+j]);
			fprintf(file_load, "%27.17E\n", array[(ND_ND+1)*i+ND_ND]);
		}
		
#endif /* PARALLEL */

#if !RP_NODE
		fclose(file_load);
#endif /* !RP_NODE */

	Message0("Done writing loads\n");
}

