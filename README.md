# QM
In order to use the xyzgjf script, the .xyz file should be formatted as such:

Dir_subdir_filename.xyz 
Dir_filename.xyz
filename.xyz

Each keyword should be separated by "_" and will correspond to the main directory, subdirectory, and job directory. The job directory will contain the input and run scripts.
In each case, the xyz file will be converted to the gjf file and associated .sh job script in the following formats:


Dir/Subdir/jobdir/filename.xyz
Dir/jobdir/filename.xyz
jobdir/filename.xyz


The directory can be used as keywords within the script, like in the example of electric field calculations:

Z+10_180_0.xyz

Z+10/180/0/0.gjf
Z+10/180/0/run.sh

where the input file 0.gjf contains the line
#P m062x/def2svp opt freq field=Z+10

in the case where the xyz file does not follow the format, the output will be:

filename.xyz
filename/filename.gjf
filename/run.sh
