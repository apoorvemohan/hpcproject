LET DIR be the absolute path of the cloned git repository

- Sample job inputs are present in the input directory (XML files)
- ONE xml file represents one job
- Syntax/Format of how to create app XML is present in DIR/hpcproject/data/README

CHANGES TO BE MADE AFTER CLONING THE REPOSITORY:

- Once the repository has been cloned edit the 'BASE' constant in DIR/hpcproject/common/imports/constants.py. Set it to the absolute path of the repository.  

HOW TO EXECUTE PHASE 1(sequential): 

- Place the xml files for all the jobs(applications) in DIR/hpcproject/data/seq/appdata/app_instance_xml
- cd DIR/hpcproject/
- bin/sequential
- logs will be created in DIR/log that contains the start and the end time of the script

HOW TO EXECUTE PHASE 2 (parallel):

- Place the xml files for all the jobs(applications) in DIR/hpcproject/data/parallel/appdata/app_instance_xml
- edit DIR/hpcproject/data/parallel/appdata/random/R.xml and mention the overcommitment factor or the total number of threads you want in the system to run in parallel. If you haveboth in the xml file the any one will be picked randomly.
- cd DIR/hpcproject/
- bin/sequential -r
- logs will be created in DIR/log that contains the start and the end time of the script
