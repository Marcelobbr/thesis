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
├── inputs
│   ├── inputs/LDAcorpus.pkl
│   ├── inputs/LDAdictionary.pkl
│   ├── inputs/URLS-AAS-marcelo.csv
│   ├── inputs/cpdoc_as.sqlite.gz
│   ├── inputs/doc_id_list.pkl
│   ├── inputs/model_lda_100_rs_00.pkl.gz
│   ├── inputs/names_dataframe.csv
│   ├── inputs/person_doc.pkl
├── notebooks
│   ├── 01-tesseract_ocr.ipynb
│   ├── 02-text_processing.ipynb
│   ├── 03-build_sql_database_docs.ipynb
│   ├── 04.1-clustering_lda_test_models.ipynb
│   ├── 04.2-clustering_lda_doc_topics_sql.ipynb
│   ├── 05-doc_entities_person_extract_and_store.ipynb
│   ├── 06.1-thesis-vis.ipynb
│   ├── 06.2-thesis-vis-AUX.ipynb
├── outputs
│   ├── outputs/docs.json
│   ├── outputs/heatmap-paper.png
│   ├── outputs/heatmap.csv
│   ├── outputs/heatmap.png
│   ├── topics_dict.pkl
│   ├── topics_metadata.json	
│   ├── ...
└── README.md

3 directories, 363 files

```
## Detailed Structure
It is important to emphasize that the aim of this project is to develop a visualization solution for topic modeling. The results from a previous topic modeling project were used here. But if you want to follow the role process, from data gathering to data visualization, I'm going to detach the preprocessing and topic modeling part from the visualization part.
### Notebooks
#### Preprocessing and topic modeling
All the listed notebooks in this section were built during a previous project located at the following repository: 

* https://github.com/rsouza/text-learning-tools

It is noteworthy that the first 2 notebooks used data that is not available for public access. In spite of that, the topic modeling and visualization steps, which are the most important for this project, use data stored on SQLite database.
* 01-tesseract_ocr.ipynb: It transform image files (.tif) into text files (.txt) by applying Optical Character Recognition with the program Tesseract.
* 02-text_processing.ipynb: It does data cleansing operations, mainly with regular expressions.
* 03-build_sql_database_docs.ipynb: it stores .txt files of each document into SQLite.
* 04.1-clustering_lda_test_models.ipynb: It creates various different versions of topic modeling and saves each. 
* 04.2-clustering_lda_doc_topics_sql.ipynb: It stores topic modeling results into SQLite
* 05-doc_entities_person_extract_and_store.ipynb: It applies entity recognition tool (Palavras) to extract data about people ocurrences in documents and stores the data into SQLITE.
#### Visualization
* 06.1-thesis-vis.ipynb: This is the main file which prepares the data for visualization by building a series of json files which are imported by the Observable notebook for D3.
* 06.2-thesis-vis-AUX.ipynb: It builds the auxiliar visualization which shows the whole view of the collection according to the heatmap of *scores* between documents and topics
### Data
#### Preprocessing and topic modeling
* inputs/LDAcorpus.pkl: Results from the notebook 04.1-clustering_lda_test_models.ipynb.
* inputs/LDAdictionary.pkl: Results from the notebook 04.1-clustering_lda_test_models.ipynb.
* inputs/model_lda_100_rs_00.pkl.gz: Results from the notebook 04.1-clustering_lda_test_models.ipynb.
* inputs/names_dataframe.csv: Database of names given by CPDOC.
* inputs/cpdoc_as.sqlite.gz: All data for the notebooks aimed at visualization are stored here on the following tables: docs, persons, person_doc, topics, topic_doc.
* inputs/URLS-AAS-marcelo.csv: Data with URLS for each group of documents (dossie).

#### Visualization
* outputs/heatmap.csv: Database built from 06.2-thesis-vis-AUX.ipynb aimed for the heatmap visualization
* The JSON files with the prefixes names_list, tokens_list and topic were obtained from the notebook 06.1-thesis-vis.ipynb.
### Images
* outputs/heatmap.png: Image built at the 06.2-thesis-vis-AUX.ipynb and exported to the Observable notebook.
* outputs/heatmap-paper.png: Image built at the 06.2-thesis-vis-AUX.ipynb and exported to the dissertation document.
## How to run the visualization
Just go to the visualization notebook, see the instructions there and wait a few seconds for it to render. Here is the link for the visualization:
* https://observablehq.com/@marcelobbr/thesis-visualization

## Requirements
Programming Languages: `Python` (Jupyter Notebook), `D3.js` (Observable) and `Vega-Lite` (Observable).

### Operating System
Most of the jupyter notebooks can be run on windows, but there are 2 exceptions: 
* 01-tesseract_ocr.ipynb: It uses tesseract, a program which runs only on Linux.
* 05-doc_entities_person_extract_and_store.ipynb: It uses Palavras, a program which runs only on Linux.

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

It is important to take note on the Python version of some programs
* gensim==3.8.0
* numpy==1.17.4 
* nltk==3.4.5
* pandas==0.25.3
* pyldavis==2.1.2 
* seaborn==0.9.0
* sqlite3==3.30.1