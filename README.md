# SIN-393 - Introducao à visão computacional (2022-2)

### Prof. João Fernando Mari ([*joaofmari.github.io*](https://joaofmari.github.io/))
---

## Aula 01 - Imagens digitais
---
* [Slides](/slides/Aula01.ImagensDigitais.(2022-2).pdf)
* [Notebook](/notebooks/Aula%2001%20-%20Imagens%20digitais.ipynb)

## Aula 02 - Introdução ao Python
---
* [Notebook](https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2/blob/main/notebooks/Aula%2002%20-%20Introdu%C3%A7%C3%A3o%20ao%20Python.ipynb)

## Aula 03 - Introdução ao NumPy
---
* [Notebook](https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2/blob/main/notebooks/Aula%2003%20-%20Introdu%C3%A7%C3%A3o%20ao%20NumPy.ipynb)

## Aula 04 - Classificação de imagens
---
* [Slides](/slides/Aula04.ClassificacaoDeImagens.(2022-2).pdf)
* [Notebook](https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2/blob/main/notebooks/Aula%2004%20-%20Classifica%C3%A7%C3%A3o%20de%20imagens.ipynb)

## Aula 05 - Redes neurais artificiais 1
---
* [Slides](/slides/Aula05.RedesNeuraisArtificiais.1.(2022-2).pdf)
* [Notebook](https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2/blob/main/notebooks/Aula%2005%20-%20Redes%20Neurais%20Artificiais%201.ipynb)

## Aula 06 - Redes neurais artificiais 2
---
* [Slides](/slides/Aula06.RedesNeuraisArtificiais.2.(2022-2).pdf)
* [Notebook](https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2/blob/main/notebooks/Aula%2006%20-%20Redes%20Neurais%20Artificiais%202.ipynb)

## Aula 07 - Classificadores: K-nn, Bayes e SVM
---
* [Notebook](https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2/blob/main/notebooks/Aula%2007%20-%20Classificadores%20K-NN%2C%20Bayes%20e%20SVM.ipynb)

## Aula 08 - Redes neurais convolucionais
---
* [Slides](/slides/Aula08.RedesNeuraisConvolucionais.(2022-2).pdf)
* [Notebook - Parte 1](https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2/blob/main/notebooks/Aula%2008%20-%20Redes%20Neurais%20Convolucionais%20(Parte%201).ipynb)
* [Notebook - Parte 1 - Colab](https://colab.research.google.com/drive/1jlgl6d03pyJeG2WGiVwUtnTmyu0w6Evi?usp=sharing)
* [Notebook - Parte 2](https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2/blob/main/notebooks/Aula%2008%20-%20Redes%20Neurais%20Convolucionais%20(Parte%202).ipynb)
* [Notebook - Parte 2 - Colab](https://colab.research.google.com/drive/1PjQlQMFNMJNn9HuK3YgK4xqcd200PnsG?usp=sharing)


## Aula 09 - Detecção e reconhecimento de objetos
---
* [Slides](/slides/Aula09.DeteccaoDeObjetos.(2022-2).pdf)
* [Notebook - Parte 1](https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2/blob/main/notebooks/Aula%2009%20-%20Detec%C3%A7%C3%A3o%20e%20reconhecimento%20de%20objetos%20(Parte%201).ipynb)
* [Notebook - Parte 2](https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2/blob/main/notebooks/Aula%2009%20-%20Detec%C3%A7%C3%A3o%20e%20reconhecimento%20de%20objetos%20(Parte%202).ipynb)

## Aula 10 - Segmentação semântica
---
* [Slides](/slides/Aula10.SegmentacaoSemantica.(2022-2).pdf)
* [Notebook](https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2/blob/main/notebooks/Aula%2010%20-%20Segmenta%C3%A7%C3%A3o%20sem%C3%A2ntica.ipynb)


# Configurando o ambiente de desenvolvimento

* instalar o Anaconda Distribution

* Criar um ambiente de execução virtual
    
    ```$ conda create -n sin393-2022-py38 python=3.8```

    ```$ conda activate sin393-2022-py38```

* Instalar as bibliotecas necessárias

    ``` $ conda install numpy scikit-image scikit-learn matplotlib pandas seaborn notebook ```

    ``` $ pip install opencv-python ```

* PyTorch. 
    * Instalação no Ubuntu com GPU.
    * Para instalação no Windows ou sem GPU, consultar [pytorch.org](https://pytorch.org/).

    ```$ conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia```

    ```$ pip install -U albumentations```



# Bibligrafia

* GONZALEZ, R.C.; WOODS, R.E. Processamento de Imagens Digitais. 3. ed. Pearson, 2010.
* COSTA, L.F.; CÉSAR-JR., R.M. Shape analysis and classification: Theory and practice. 1. ed. CRC Press, 2000.
* RUSSEL, S.J.; NORVIG, P. Inteligência Artificial. 2.ed. Campus, 2004.
* DUDA, R.O.; HART, P.E.; STORK, D.G. Pattern Classification. Wiley, 2001. 
* CHITYALA, R.; PUDIPEDDI, S. Image processing and acquisition using Python. CRC Press, 2014.
* MARQUES FILHO, O.; VIEIRA NETO, H. Processamento digital de imagens. Brasport, 1999.
    * http://dainf.ct.utfpr.edu.br/~hvieir/pub.html   
* PONTI, M. Everything you wanted to know about Deep Learning for Computer Vision but were afraid to ask. SIBGRAPI 2017 Tutorial.
    * http://conteudo.icmc.usp.br/pessoas/moacir/p17sibgrapi-tutorial/  
* PONTI, M; COSTA, G. B. P. Como funciona o Deep Learning. Computer Vision and Pattern Recognition. 2017.
    * https://arxiv.org/abs/1806.07908  
* CS231n: Convolutional Neural Networks for Visual Recognition.
    * http://cs231n.stanford.edu/ 
* GOODFELLOW, I.; BENGIO, Y.; COURVILLE, A. Deep Learning. MIT Press, 2016. 
    * http://www.deeplearningbook.org 
* NIELSEN, M. Neural Networks and Deep Learning. Livro On-Line. 
    * http://neuralnetworksanddeeplearning.com  



# Ferramentas computacionais

* Anaconda Distribution
    * https://www.anaconda.com/distribution/
* Google Colab
    * https://colab.research.google.com
* Scikit-image
    * https://scikit-image.org/
* Scikit-learn
    * https://scikit-learn.org/
* OpenCv
    * https://opencv.org/
    * <i>Binding</i> para Python:
        * https://pypi.org/project/opencv-python/
        * https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
* PyTorch
    * https://pytorch.org/

# Edições anteriores da disciplina

* [2018-2](https://github.com/joaofmari/computer-vision/tree/master/sin393-2018)
* [2019-2](https://github.com/joaofmari/computer-vision/tree/master/sin393-2019)

# Citação

* Como citar este material:

```
    @misc{mari_comp_vis_2022,
        author = {João Fernando Mari},
        title = {Introdução à visão computacional},
        year = {2022},
        publisher = {GitHub},
        journal = {GitHub repository},
        howpublished = {\url{https://github.com/joaofmari/SIN393_Introducao-a-visao-computacional_2022-2}}
    }
```

---
João Fernando Mari - UFV-CRP - 2022-2 - [joaofmari.github.io](joaofmari.github.io) - joaof.mari@ufv.br