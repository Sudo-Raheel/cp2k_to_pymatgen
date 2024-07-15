# Cp2k_to_pymatgen
Tutorials to use [pymatgen](https://github.com/materialsproject/pymatgen) for post processing [cp2k](https://github.com/cp2k/cp2k)output files and generating input files 
## [Cube parsing](./cube_file/)
- Contains snippets to convert cp2k cube files to pymatgen volume object .
- Different functions like planar average of pymatgen used and bencmarked with cubecruncher
## [Output parsing](./_output_file/)
- convert the cp2k output file to  pymatgen.io.cp2k.output
- The class can be used to parse different information like energy,force and structures(initial and relaxed)
## [DOS parsing](./dos_file/)  
- parse the dos from cp2k output file to pymatgen dos object
- all the functionalies like plotting and different parameters can be obtained from this class 
## [Bandstructure parsing](./bs_file/)  
- get the bandstructure information and pass it to pymatgen BS object
   all the functionalies like plotting and different parameters can be obtained from this class 
## [Structure analysis](./stc_file/) 
- using different pymatgen modules to generate disordered structures , slabs etc 
