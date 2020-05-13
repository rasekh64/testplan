#!/bin/bash -l
#
#PBS -N job_name
#PBS -l walltime=71:00:00
#PBS -l nodes=4:ppn=28
#PBS -m bae
#PBS -A lt1_2019-51

module load FLUENT/18.1

export ANSYSLI_SERVERS=2325@ir03lic1.ugent.be
export ANSYSLMD_LICENSE_FILE=1055@ir03lic1.ugent.be

CASE_NAME=folder_name
CASE_PATH=$VSC_DATA_VO_USER/Test_plan/$CASE_NAME
cd $CASE_PATH
FLUENT_INPUTFILE=journal_file.jou
FLUENT_HOSTFILE=fluent.hosts.`date +%s`
cat $PBS_NODEFILE | sed -e 's/\.golett.*$//' > $FLUENT_HOSTFILE
FLUENT_PROCESSES=`cat $FLUENT_HOSTFILE | wc -l`
fluent 3ddp -g -t$FLUENT_PROCESSES -cnf=$FLUENT_HOSTFILE -ssh < $FLUENT_INPUTFILE &> $CASE_PATH/$USER.$PBS_JOBID.log

