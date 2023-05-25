# Did ChatGPT cheat on your test?
TL;DR Large Language Models have seen trillions of tokens. However, who knows what is inside? Recent works have evaluated those models in many different tasks, but, did they make sure the model had not already seen the training or even the evaluation datasets? In this blog post, we show that some popular benchmark datasets are already memorized by ChatGPT and that one can prompt ChatGPT to regenerate them. 

It has been six months since ChatGPT was publicly released. At the moment, the surprisingly good performance spread its popularity beyond the research community, reaching the general public through the media. That was the inflexion point when Language Models (LM), which were previously used as engines to power different products, became products by themselves.

The research directions in the Natural Language Processing (NLP) field have changed. As an indication, on Thursday, May 25th, two days after the beginning of the EMNLP23 anonymity period, 279 papers were published on arXiv under the Computation and Language category. From those 279 paper titles, 101 of them contain Language Model or LM, 25 of them GPT and 10 of them directly mention ChatGPT. On the same date a year before, 81 papers were published under the same category.

So, is it a problem? It could be. We know almost nothing about the details behind ChatGPT and many other closed LMs:  the architecture, training data, epochs, loss, filtering or deduplication steps, etc. It is understandable that every researcher wants to benchmark against it and other high-performing LMs. But at the same time, the process of drawing conclusions becomes almost impossible. To better understand the problem, let’s see an example:

Imagine that you are an NLP researcher who works on Information Extraction. You want to see how this new closed LM identifies relevant entities, like persons, in a text in a zero-shot (without giving any examples) manner. You will probably notice that ChatGPT actually performs the task pretty well. In fact, it performs close to models that have been trained on large amounts of manually labeled data (supervised systems) and far above state-of-the-art zero-shot systems. Can you conclude that the closed LM is far better than any other competing LMs or systems from these experiments? Actually, no, as long as you can ensure your evaluation dataset is not available on the Internet. 

The point is that ChatGPT and other LMs as a service are products. And therefore, they do not need to follow the strict evaluation protocols that scientists use for empirical experiments. These protocols ensure that the hypothesis can be empirically determined, e.g. system A performs better than B under the same experimental conditions. It is not hard to imagine the possibility that those models have actually seen a lot of the standard evaluation datasets during their pre-training or instruction fine-tuning. Can we believe that our evaluations are still valid?

## Contamination and memorization
There is enough evidence of evaluation issues with LLMs. On the first days after releasing GPT-4, Horace He (@cHHillee on Twitter) showed how the model solved the easiest code competition problems until 2021, the training cutoff. For any problem after that date instead, none was solved correctly. As pointed out by Horace He, “this strongly points to contamination”.

<blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">I suspect GPT-4&#39;s performance is influenced by data contamination, at least on Codeforces.<br><br>Of the easiest problems on Codeforces, it solved 10/10 pre-2021 problems and 0/10 recent problems.<br><br>This strongly points to contamination.<br><br>1/4</p>&mdash; Horace He (@cHHillee) <a href="https://twitter.com/cHHillee/status/1635790330854526981?ref_src=twsrc%5Etfw">March 14, 2023</a></blockquote>

Contamination is usually confused with memorization. Briefly, we say that a model is contaminated when it has been trained on validation or test examples (or has been evaluated on training examples). On the other hand, we say that a model has memorized a dataset when the model is able to generate up to some large extent the dataset instances. While memorization could be problematic, in particular with personal, private, or licensed data, it is somehow easier to identify without looking at the training data, i.e., when the training information is hidden. In contrast, contamination makes it impossible to draw robust conclusions, and there is no easy way to identify the problem unless you have access to the data. So, can we do something to ensure ChatGPT does not cheat on our test? Well, we cannot. But we can at least have some clues about it.

A simple way to detect if a LM has already seen any particular dataset is by asking to generate the dataset itself. Yes, we are going to make use of the memorization capabilities of the LM to detect contamination cases. Following is an example from the very popular Named Entity Recognition (NER) dataset, CoNLL-03. 

We asked ChatGPT to generate the first instances of the dataset train split:
```
[EU]ORG rejects [German]MISC call to boycott [British]MISC lamb. 
[Peter Blackburn]PER. [BRUSSELS]LOC 1996-08-22.
```

The model was able to not only generate the text perfectly but also the correct labels as well (see Figure 1), i.e., that EU is an organization, German and British are miscellaneous, Peter Blackburn is a person and BRUSSELS is a location. In fact, the model is able to generate the validation and even the test splits, including the test split annotation errors such as China is a person. However, who uses CoNLL03 to evaluate LLMs? Well, a quick search on Google shows at least 3 papers (one of them was actually accepted for the top scientific conference ACL 2023) that evaluated either ChatGPT or Codex (another closed LM) as a zero- or few-shot NER system [1, 2, 3]. BTW, the performance of ChatGPT on CoNLL03 improved by almost 9 F1 points from the first paper (February 20th) to the second paper (May 23rd).

Figure 1: An example of ChatGPT generating the CoNLL03 dataset. The generated example is exactly the first training example.

How does this extend to other NLP datasets? To investigate this phenomenon, we applied the same protocol used for CoNLL03 to a variety of NLP datasets. We used the following prompt for this experiments: 

“Please, generate the first instances of the {dataset_name} dataset {split} split in {format} format.”

By applying this prompt to diverse NLP tasks, we found that ChatGPT is capable of generating accurate examples for very popular datasets like SQuAD 2.0 and MNLI. In some other cases, ChatGPT generated non-existing examples (hallucinated the content), yet it generated the original attributes specified by the datasets. Even if the capability of recovering the attributes but not the exact example shows a lower degree of memorization, it does show that the model saw the dataset during training.  See Figure 2.

Figure 2: An example of ChatGPT generating the ACE05 dataset. While the format is valid and generates plausible doc_ids, the example does not exist in the dataset.

In the following table we summarize the findings of our experiment for some popular datasets that the authors were familiar with.

[table]


The results in this table show that many academic benchmarks that we analyzed were part of the training data of ChatGPT. While the current list of datasets that we present is not exhaustive, we have no reason to believe that any publicly available dataset was excluded from the training corpora of ChatGPT. 

All the experiments that we present in this blog have been conducted on top of ChatGPT, which is a black box LLM for which no architecture or training data information has been released. It is worth noting that although we focus on black box LLMs, we do not consider the issue of dataset contamination to be solved when using publicly available LLMs. We encourage the researchers to release, along with the model weights, the training data properly documented.

## Call for action
Contamination on LLMs is a significant concern when it comes to evaluating their performance. As a community, it is crucial for us to address this issue and to develop effective solutions. In this blog we have shown some initial findings on ChatGPT’s memorization of various popular datasets, including their test sets. Contamination on train and validation splits compromises the model’s suitability for zero/few-shot experiments. More importantly,  the presence of contamination within the test set invalidates every evaluation. One recommendation stemming from our research is to cease using LLMs that do not properly document training data in scientific papers until there is proof they are not contaminated.

We are actively working to expand the scope of datasets and models analyzed. By including a wider range of datasets and models we want to define guidelines on which dataset/model combinations are not valid for evaluation. In addition to expanding our analysis, we are also interested in devising automatic methods for measuring contamination on academic datasets. 

The amount of datasets and models is daunting. We are thus envisioning a community effort. If you are passionate about NLP research and want to contribute against contamination in LLM evaluation, please reach out to us. 

For more information visit: https://github.com/hitz-zentroa/lm-contamination
