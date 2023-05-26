# Did ChatGPT cheat on your test?
**Authors:** [Oscar Sainz](https://osainz59.github.io/), [Jon Ander Campos](), [Iker Garcia-Ferrero](), [Julen Etxaniz](), [Eneko Agirre]()

It has been six months since ChatGPT was publicly released. At the moment, the surprisingly good performance spread its popularity beyond the research community, reaching the general public through the media. That was the inflexion point when Language Models (LM), which were previously used as engines to power different products, became products by themselves.

The research directions in the Natural Language Processing (NLP) field have changed accordingly. As an indication, on Thursday, May 25th, two days after the beginning of the EMNLP23 anonymity period, 279 papers were published on arXiv under the Computation and Language category. From those 279 paper titles, 101 of them contain Language Model or LM, 25 of them GPT and 10 of them directly mention ChatGPT. On the same date a year before, 81 papers were published under the same category.

Unfortunately we know almost nothing about the details behind ChatGPT and many other closed LMs:  the architecture, epochs, loss, filtering or deduplication steps and especially the data used to train them. Given the good performance of ChatGPT many studies are benchmarked against it or other closed LMs. But at the same time, the process of drawing empirical conclusions becomes almost impossible. To better understand the problem, let’s see an example:

Imagine that you are an NLP researcher who works on Information Extraction. You want to see how this new closed LM identifies relevant entities, like persons, in a text in a zero-shot manner (i.e. without giving any labeled examples to the model). You will probably notice that ChatGPT performs the task pretty well. In fact, it performs close to models that have been trained on large amounts of manually labeled data (supervised systems) and far above state-of-the-art zero-shot systems. Can you conclude that ChatGPT is far better than any other competing LMs? Actually, no, unless you can be 100% sure that  the evaluation dataset is not available on the Internet and therefore has not been seen by ChatGPT during training. 

The point is that ChatGPT and other LMs as a service are **products**. And therefore, they do not need to follow the strict evaluation protocols that scientists use for empirical experiments. These protocols ensure that hypotheses can be empirically determined, e.g. system A performs better than B under the same experimental conditions. In the case of large LMs there is the possibility that those models have seen the standard evaluation datasets during their pre-training or instruction fine-tuning. Without ruling out this possibility, we cannot conclude their superiority over other systems. 

## Contamination and memorization
There is enough evidence of evaluation issues with LLMs. On the first days after releasing GPT-4, Horace He ([@cHHillee](https://twitter.com/cHHillee) on Twitter) showed how the model solved the easiest code competition problems until 2021, the training cutoff. For any problem after that date instead, none was solved correctly. As pointed out by Horace He, *“this strongly points to contamination”*.

<blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">I suspect GPT-4&#39;s performance is influenced by data contamination, at least on Codeforces.<br><br>Of the easiest problems on Codeforces, it solved 10/10 pre-2021 problems and 0/10 recent problems.<br><br>This strongly points to contamination.<br><br>1/4</p>&mdash; Horace He (@cHHillee) <a href="https://twitter.com/cHHillee/status/1635790330854526981?ref_src=twsrc%5Etfw">March 14, 2023</a></blockquote>

Briefly, we say that a model is contaminated when it has been trained on validation or test examples (or has been evaluated on training examples). A related concept is memorization. We say that a model has memorized a dataset when the model is able to generate up to some large extent the dataset instances. While memorization could be problematic, in particular with personal, private, or licensed data, it is somehow easier to identify without looking at the training data, i.e., when the training information is hidden. In contrast, contamination makes it impossible to draw robust conclusions, and there is no easy way to identify the problem unless you have access to the data. So, can we do something to ensure ChatGPT does not cheat on our test? We cannot, as this will require having access to the full set of documents used by ChatGPT during its training. But we can have some clues about it, as follows.

A simple way to detect if a LM has already seen any particular dataset is by asking to generate the dataset itself. We are going to make use of the memorization capabilities of the LM to detect contamination cases. For instance, regarding a very popular Named Entity Recognition (NER) dataset, CoNLL-03, we asked ChatGPT to generate the first instances of the dataset train split, which are the following:
> [EU]<sub>ORG</sub> rejects [German]<sub>MISC</sub> call to boycott [British]<sub>MISC</sub> lamb. [Peter Blackburn]<sub>PER</sub>. [BRUSSELS]<sub>LOC</sub> 1996-08-22.

As seen below in Figure 1, the model generated the text and labels perfectly i.e., that EU is an organization, German and British are miscellaneous, Peter Blackburn is a person and BRUSSELS is a location. In fact, the model is able to generate the validation and even the test splits, including annotation errors such as China labeled as a person. A quick search on Google shows that at least 3 papers (one of them was actually accepted for the top scientific conference ACL 2023) did  evaluate either ChatGPT or Codex (another closed LM) as a zero-shot or few-shot NER system [1, 2, 3]. BTW, the performance of ChatGPT on CoNLL03 improved by almost 9 F1 points from the first paper (February 20th) to the second paper (May 23rd) for unknown reasons, but that’s another story beyond this post.

![An example of ChatGPT generating the CoNLL03 dataset.](imgs/CoNLL03_train_small.png)

***Figure 1**: An example of ChatGPT generating the CoNLL03 dataset. The generated example is exactly the first training example.*

How does this extend to other NLP datasets? To investigate this phenomenon, we applied the same protocol used for CoNLL03 to a variety of NLP datasets. We used the following prompt for this experiments: 

> “Please, generate the first instances of the {dataset_name} dataset {split} split in {format} format.”

By applying this prompt to diverse NLP tasks, we found that ChatGPT is capable of generating accurate examples for other popular datasets like SQuAD 2.0 and MNLI. In some other cases, ChatGPT generated non-existing examples (hallucinated the content), yet it generated original attributes like format or identifiers in the datasets. Even if the capability of recovering the attributes but not the exact example shows a lower degree of memorization, it does show that the model saw the dataset during training.  See Figure 2.

![An example of ChatGPT generating the ACE05 dataset.](imgs/ACE_format_small.png)

***Figure 2**: An example of ChatGPT generating the ACE05 dataset. While the format is valid and generates plausible doc_ids, the example does not exist in the dataset.*

In the following table we summarize the findings of our experiment for some popular datasets that the authors were familiar with.

[table]
|**Dataset**|**Task**|**Release date**|**Train split**|**Dev split**|**Test split**|**Guidelines**|
|:----------|:-------|:---------------|:--------------|:------------|:-------------|:------------:|
|CoNLL03    | IE     | 2003           |[<img src="https://img.shields.io/badge/-Examples%20-red">]() | [<img src="https://img.shields.io/badge/-Examples%20-red">]() | [<img src="https://img.shields.io/badge/-Examples%20-red">]() | |
|ACE05      | IE     | 2005           |[<img src="https://img.shields.io/badge/-Attributes%20-blue">]() | [<img src="https://img.shields.io/badge/-Attributes%20-blue">]() | [<img src="https://img.shields.io/badge/-Attributes%20-blue">]() | ✔️ |
|OntoNotes  | IE     | 2013           |[<img src="https://img.shields.io/badge/-Hallucinates%20-green">]() | [<img src="https://img.shields.io/badge/-Hallucinates%20-green">]() |[<img src="https://img.shields.io/badge/-Hallucinates%20-green">]() | ✔️ |


