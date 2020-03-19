# Dissertation (Topic Explorer)
This is the repository for my dissertation at EMAP-FGV, MSC in Mathematical Modeling.

In this project I have developed a visualization framework for results from topic modeling.

Programming Languages: `Python` (IDE Jupyter Notebook) and `D3.js` (IDE Observable).

## People
### Author
* [Marcelo B. Barata Ribeiro](https://www.linkedin.com/in/marcelo-barata-ribeiro-213b8733/)
### Tutors
* [Asla Medeiros e Sá](https://emap.fgv.br/corpo-docente/asla-medeiros-sa)
* [Renato Rocha Souza](https://emap.fgv.br/corpo-docente/renato-rocha-souza)

## Abstract
Nos últimos anos, diversos avanços foram promovidos no campo de modelagem de tópicos,
seja por meio do desenvolvimento de novos algoritmos, seja em processos de avaliação, assim
como pelo surgimento de novas ferramentas de visualização. Esta última frente avança
devido à percepção de que modelos de tópicos fornecem nova capacidade exploratória de
grandes coleções de documentos, o que, aliado a soluções de visualização, pode trazer nova
percepção analítica ao especialista de domínio.

Este trabalho buscou introduzir uma solução interativa e de alta amplitude analítica, tendo
como objeto de estudo uma coleção de documentos disponibilizada pelo CPDOC/FGV. A
metodologia envolveu uso de resultados provenientes de modelagem de tópicos e transformações
dos dados para o processo de visualização, o que demandou o uso de distintas
ferramentas de programação disponíveis. Após investigação do estado da arte, a hipótese
principal é que haveria baixa disponibilidade de ferramentas de visualização de tópicos
que incorporasse uma visão global do corpus acompanhada por um aumento gradual do
nível de detalhamento, passando pela análise de agrupamentos de objetos viabilizada pela
modelagem de tópicos, até a exploração de cada objeto.

A principal contribuição está na elaboração de uma nova ferramenta que atende a conceitos
de granularidade, usuário-alvo e data-ink ratio por meio de uma linguagem de programação
que forneça o máximo de flexibilidade. Por fim, conclui-se que haveria muito espaço de
melhoria, seja por meio de aumento de interatividade, quanto por maior dedicação a etapas
de pré-processamento no caso de coleções de documentos que tenham passado por processo
de OCR.

## Files List
It is important to emphasize that the aim of this project is to develop a visualization solution for topic modeling. The results from a previous topic modeling project were used here. But if you want to follow the role process, from data gathering to data visualization, I'm going to detach the preprocessing and topic modeling part from the visualization part.
### Notebooks
#### Preprocessing and topic modeling
It is noteworthy that the first 2 notebooks used data that is not available for public access. In spite of that, the topic modeling and visualization steps, which are the most important for this project, use data stored at the  SQLITE database.
* 01-tesseract_ocr.ipynb: It transform image files (.tif) into text files (.txt) by applying Optical Character Recognition with the program Tesseract.
* 02-text_processing.ipynb: It does data cleansing operations, mainly with regular expressions.
* 03-build_sql_database_docs.ipynb: it stores .txt files of each document into SQLITE.
* 04.1-clustering_lda_test_models.ipynb: It creates various different versions of topic modeling and saves each. 
* 04.2-clustering_lda_doc_topics_sql.ipynb: It stores topic modeling results into SQLITE
* 05-doc_entities_person_extract_and_store.ipynb: It applies entity recognition tool (Palavras) to extract data about people ocurrences in documents and stores the data into SQLITE.
#### Visualization
* thesis-vis.ipynb: This is the main file which prepares the data for visualization by building a series of json files which are imported by the Observable notebook for D3.
* thesis-vis-AUX.ipynb: It builds the auxiliar visualization which shows the whole view of the collection according to the heatmap of *scores* between documents and topics
### Data
#### Preprocessing and topic modeling
* LDAcorpus.pkl: Results from the notebook 04.1-clustering_lda_test_models.ipynb.
* LDAdictionary.pkl: Results from the notebook 04.1-clustering_lda_test_models.ipynb.
* model_lda_100_rs_00.pkl.gz: Results from the notebook 04.1-clustering_lda_test_models.ipynb.
* names_dataframe.csv: Database of names given by CPDOC.
* cpdoc_as.sqlite.gz: All data for the notebooks aimed at visualization are stored here on the following tables: docs, persons, person_doc, topics, topic_doc.
* URLS-AAS-marcelo.csv: Data with URLS for each group of documents (dossie).

#### Visualization
* heatmap.csv: Database built from thesis-vis-AUX.ipynb aimed for the heatmap visualization
* The JSON files with the prefixes names_list, tokens_list and topic were obtained from the notebook thesis-vis.ipynb.
### Images
* heatmap.png: Image built at the thesis-vis-AUX.ipynb and exported to the Observable notebook.
* heatmap-paper.png: Image built at the thesis-vis-AUX.ipynb and exported to the dissertation document.
## How to run the visualization
Just go to the visualization notebook, see the instructions there and wait a few seconds for it to render. Here is the link for the visualization
* https://observablehq.com/@marcelobbr/thesis-visualization


```sh
python3 test.py
```


## Requirements
If you are used to Linux and Python, this section isn't necessary, except in case of any malfunctioning or low experience with those softwares.

### Operating System
All the system was built using Linux Ubuntu. We strongly recommend that you also use a Linux Distribution or at least an OS from Unix family. In case you are using Windows, we suggest you to operate inside a Virtual Machine. Just follow one of the guides below:
* [lifewire guide](https://www.lifewire.com/run-ubuntu-within-windows-virtualbox-2202098)
* [VirtualBox guide](https://www.virtualbox.org/manual/ch01.html)

You will need the Ubuntu installer ISO file, which can be found at Ubuntu website. We worked with Ubuntu 18.04.3 LTS. LTS stands for long-term support and we suggest you to also choose LTS versions.
* [Ubuntu installer](https://ubuntu.com/download/desktop)

In Ubuntu, you will see that both C++ and Python are already installed, which is a great shortcut for you. Nevertheless, there are also some considerations about these programming languages. See below.

### C++


* cppimport==18.11.8
* Mako==1.1.0
* MarkupSafe==1.1.1
* pybind11==2.3.0 

### Python
We chose Python3 version of Python, while the standard version from Ubuntu is Python2. As there are some differences between the two versions, we suggest that you install python3. Anaconda is pretty handy to work with python as it has various preinstalled external Python packages.

To work with most of the files, it is necessary to have jupyter notebook installed on your system (if you already installed Anaconda, you might skip this step). To install it, go to terminal and type:
```sh
sudo apt update
pip install jupyter
```
Then go to your worspace folder with .ipynb files  and initialize jupyter notebook by doing
```sh
cd <your/folder/name>
jupyter notebook
```