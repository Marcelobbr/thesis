# Master Thesis (Topic Explorer)
This is the repository for my master thesis at FGV/EMAP, MSc in Mathematical Modeling.

In this project I have developed a visualization framework for results from topic modeling.

## People
### Author
* [Marcelo B. Barata Ribeiro](https://www.linkedin.com/in/marcelo-barata-ribeiro-213b8733/)
### Tutors
* [Asla Medeiros e Sá](https://emap.fgv.br/corpo-docente/asla-medeiros-sa)
* [Renato Rocha Souza](https://emap.fgv.br/corpo-docente/renato-rocha-souza)

## Abstract
In recent years, several advances have been promoted in topic modeling, either through the development of new algorithms, or in evaluation processes, as well as by the emergence of novel visualization tools. This last field advances due to the realization that topic models provide new exploratory capabilities for large collections of documents which, combined with visualization solutions, can bring new insights to domain specialists.

This work sought to introduce a novel interactive and highly analytical solution, having as object of study a document collection provided by FGV/CPDOC. The methodology comprises the use of results from topic modeling and data transformations for the data visualization, which required using distinct programming languages avaliable. After the investigation of the state of the art, the main hypothesis is that there would be low availability of visualization tools aimed at topic models able to incorporate a global view of the corpus together with a gradual increase on the level of detail, passing through the analysis of object clusters provided by topic modeling, until the exploration of each unique object.

The main contribution is the implementation of a novel tool that meets the concepts of granularity, target-user and data-ink ratio through a programming language that provides maximum flexibility. Finally, it is reckoned that there would be room for improvement, either through increased interactivity, or through greater dedication to pre-processing steps in the case of document collections that have gone through OCR processes.

## Structure
```bash
.
├── data
│   ├── cpdoc_as.sqlite.gz                                  # All data for the notebooks aimed at visualization are stored here on the following tables: docs, persons, person_doc, topics, topic_doc.
│   ├── doc_id_list.pkl
│   ├── 05_names_dataframe.csv                              # Database of names given by CPDOC.
│   ├── 05_person_doc.pkl
│   ├── 01_raw                                              # folder containing original files
│   │   ├── URLS_AAS.csv                                    # Data with URLS for each group of documents (dossie). File was given by CPDOC.
│   │   ├── samples (folder)                                # folder to store samples for the whole project. Useful for demonstration. (TO DO)
│   ├── 04_model
│   │   ├── corpus.pkl                                      # Results from the notebook 04_1_topic_model_tests.ipynb.
│   │   ├── dictionary.pkl                                  # Results from the notebook 04_1_topic_model_tests.ipynb.
│   │   ├── model_100.pkl.gz                                # Results from the notebook 04_1_topic_model_tests.ipynb.
│   │   ├── pyldavis_output_100topics.html                  # Results from the notebook 04_1_topic_model_tests.ipynb.
│   ├── 06_outputs                                          # The JSON files with the prefixes names_list, tokens_list and topic were obtained from the notebook 06_1_thesis_vis.ipynb.
│   │   ├── names_list_<topic id>.json
│   │   ├── tokens_list_<topic id>.json
│   │   ├── topic_<topic id>.json
│   ├── 06_outputs_aux                                      # files related to the heatmap vis (built at 06_2_thesis_vis_AUX)
│   │   ├── heatmap_paper.png                               # Image exported to the Observable notebook.
│   │   ├── heatmap.png                                     # Image exported to the thesis document.
├── docs                                                    # documents related to the thesis
├── notebooks
│   ├── 01_tesseract_ocr.ipynb                              # It transform image files (.tif) into text files (.txt) by applying Optical Character Recognition with the program Tesseract. (NEEDS REFACTORING)
│   ├── 02_text_processing.ipynb                            # It does data cleansing operations, mainly with regular expressions. (NEEDS REFACTORING)
│   ├── 03_build_sql_database_docs.ipynb                    # it stores .txt files of each document into SQLite.
│   ├── 04_1_topic_model_tests.ipynb                        # It tests various different versions of topic modeling and saves each. 
│   ├── 04_2_topic_model_to_sql.ipynb                       # It stores topic modeling results into SQLite.
│   ├── 05_1_doc_entities_person_names_list.ipynb           # it prepares data for entity extraction. (NEEDS REFACTORING)
│   ├── 05_2_doc_entities_person_extract_and_store.ipynb    # It applies entity recognition tool (Palavras) to extract data about people ocurrences in documents and stores the data into SQLITE.
│   ├── 06_1_thesis_vis.ipynb                               # This is the main file which prepares the data for visualization by building a series of json files which are imported by the Observable notebook for D3.
│   ├── 06_2_thesis_vis_AUX.ipynb                           # It builds the auxiliar visualization which shows the whole view of the collection according to the heatmap of scores between documents and topics
├── src                                                     # source code
│   ├── utils.py                                            # General functions
│   ├── 06_vis.py                                           # Scripts for vis notebooks
├── README.md
└── requirements.txt

3 directories, 363 files
```
It is important to emphasize that the aim of this project is to develop a visualization solution for topic modeling. The results from a previous topic modeling project were used here. But if you want to follow the role process, from data gathering to data visualization, I'm going to detach the preprocessing and topic modeling part from the visualization part.

Important Notes: 
* You can see brief descriptions of some of the files above by accessing the raw version of README or by just clicking [here](https://raw.githubusercontent.com/Marcelobbr/thesis/master/README.md).
* Notebooks are sorted according to the order they should be run.
    * It is noteworthy that the first 2 notebooks used data that is not available for public access. In spite of that, the topic modeling and visualization steps, which are the most important for this project, use data stored on SQLite database.
* Data folder files generally have prefixes which associate them to the notebook which uses or builds them. 
    * Those without prefixes are files related to multiple notebooks. 
    * Subfolders were created to group multiple files related to the same notebook.
* src has some functions which are used by notebooks. They might also have prefixes.
    * utils.py has general functions. 

Related project:
*   The notebooks from prefix 01 to 05 are related to preprocessing and modeling steps. They were built (slightly refactored) during a previous project located at the following repository: 
    * https://github.com/rsouza/text-learning-tools

## How to run the visualization
Just go to the visualization notebook, see the instructions there and wait a few seconds for it to render. Here is the link for the visualization:
* https://observablehq.com/@marcelobbr/thesis-visualization

## Requirements
Programming Languages: `Python` (Jupyter Notebook), `D3.js` (Observable) and `Vega-Lite` (Observable).

### Operating System
Most of the jupyter notebooks can be run on windows, but there are 2 exceptions: 
* 01_tesseract_ocr.ipynb: It uses tesseract, a program which runs only on Linux.
* 05_doc_entities_person_extract_and_store.ipynb: It uses Palavras, a program which runs only on Linux.

In case you want to use/test all notebooks, we strongly recommend that you also use a Linux Distribution or at least an OS from Unix family. In case you are using Windows, we suggest you to operate inside a Virtual Machine. Just follow one of the guides below:
* [lifewire guide](https://www.lifewire.com/run-ubuntu-within-windows-virtualbox-2202098)
* [VirtualBox guide](https://www.virtualbox.org/manual/ch01.html)

You will need the Ubuntu installer ISO file, which can be found at Ubuntu website. We worked with Ubuntu 18.04.3 LTS. LTS stands for long-term support and we suggest you to also choose LTS versions.
* [Ubuntu installer](https://ubuntu.com/download/desktop)

In Ubuntu, you will see Python is already installed, which is a great shortcut for you. Nevertheless, there are also some considerations about these programming languages. See below.

The Palavras program is aimed at Entity Extraction. It is neccessary to pay for the licence, which the Fundação Getulio Vargas has access. There are also alternatives, such as [Stanford NLP](https://nlp.stanford.edu/software/).

The Tesseract program is free of charge. To use it, just follow [this link](https://www.pyimagesearch.com/2017/07/03/installing-tesseract-for-ocr/).

### Python
We chose Python3 version of Python, while the standard version from Ubuntu is Python2. As there are some differences between the two versions, we suggest that you install python3. Anaconda is pretty handy to work with python as it has various preinstalled external Python packages. To follow the link below:
* [Anaconda Distribution](https://www.anaconda.com/distribution/)

To work with most of the files, it is necessary to have jupyter notebook installed on your system (if you already installed Anaconda, you might skip this step). To install it, go to terminal and type:
```sh
sudo apt update
pip install jupyter
```
Then go to your worspace folder with .ipynb files  and initialize jupyter notebook by typing:
```sh
cd <your/folder/name>
jupyter notebook
```
The following Python packages are essential to run the notebooks, some of them pre-installed on Anaconda:
> enchant - gensim - numpy - matplotlib - nltk - pandas - pyldavis - seaborn - sqlite3 - 

The version of each package is located at `requirements.txt`.