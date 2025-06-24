# mod5_dataviz_project

Information on creating my Data_Viz Project

Development workflows
=======================

Create new project
----------------------

Ran:

```bash
cookiecutter
 gh:JulesU/mod5_dataviz_project
```

Put project under version control
---------------------------------

Added files to my git folder ( I actually forgot to do the initial commit until later-oops)

```bash
git init
git add *.ipynb
git add *.md
git add output/*.html
git commit -m "Initial commit"
```

For the remote repository, make a github repository named mod5_dataviz_project, then do;

```bash
git remote add origin git@github.com:JulesU/mod5_dataviz_project.git
git branch -M main
git push -u origin main
```

Version control is good.

Once done with notebook, notes, and readme file changes, ran again from command line::

git push -u origin main

Folder structure
-----------------

Here's the folder structure that gets created by `cookiecutter-datascience-simple`: (I did the more complex one)

	├── mod5_dataviz_project<- Your notebooks, scripts will live in the main project folder
		│   .gitignore				<- Common file types for git to ignore 								(oops I added this to git)
		│   README.md				<- Top-level README for developers
		│   
        	├───notebooks
   		│   └───input
		│   	└───mod5_dataviz_project.ipynb  <- Jupyter notebook of my  project
		│   	└───pbp_proj.py			<- this is the python file that is 			│ 					brought in with the Excel button - open 		│ 					pbp_proj.xlsm to enter data and press 			|					button - this ended up not working
		│   	└───pbp_proj.xlsm		<- OPEN THIS when reach later section of 		|					notebook to run xlwings. Not working but 		|					can see attempts
		│   	└───pizzanew.db			<- this is the sqlite.db I created my 			|					migrating it from Access db with 			|					sqlalchemy
		│
		├───data				<- Final and intermediate data
		│   └───raw				<- The original, immutable data dump
		│
		├───docs
		│   	└───notes.md			<- Simple markdown for project notes
		├───images				<-  screenshots of my xlwings work - I 			|					hope to get them to show up in my 			|					notebook
		|
		└───output				<-- None

		readme.md				<- Guidance for using this folder


Documentation
--------------

In this very simple project structure template, I included a markdown file (notes.md) with some section headings to use for project notes and included screenshots of my work. My plan is to add the screenshots that occurred outside python and python notebook - for example, the VBA work in Excel.

The first section is mostly Data Visualization with Great Tables and Plotly. Data wrangling was done first and I have way too many dataframes.


I have a later section of my notebook that can't be run on my Mac but for anyone running in a Windows environment  should not have any issues. I developed that code after making a repo of my notebook and other Excel work on my PC and then committed those changes and pushed them back to the repo. I unfortunately  re-ran the code in my Mac but a User running the notebook in Windows should be able to generate the same data. In the end, the final output did not work but it involved much of my project researching and testing the errors, uninstalling Anaconda, re-installing, to no avail. 


Citation of Great Tables: @software{Iannone_great_tables, author = {Iannone, Richard and Chow, Michael}, license = {MIT}, title = {{great-tables: Make awesome display tables using Python.}}, url = {https://github.com/posit-dev/great-tables}, version = {0.14.0} }
