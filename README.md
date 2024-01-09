<img src="docs/blog/imgs/hitz_logo.png" align="right" width="300">

# LM Contamination Index

Large Language Models have seen trillions of tokens – who knows what is inside? Recent works have evaluated those models on many different tasks, but did they make sure the model had not already seen the training or even the evaluation datasets? In the [blog post](https://hitz-zentroa.github.io/lm-contamination/blog), we show that some popular benchmark datasets are already memorized by ChatGPT and that one can prompt ChatGPT to regenerate them.

In this repo, we aim to collect (as much as possible) contamination evidence to provide to the research community a reliable resource to quickly check whether the model has already seen their evaluation dataset. However, we are aware of the incompleteness of the index and therefore we ask researchers to in any case, perform an small experiment of contamination beforehand.

You can visit the search tool [LM Contamination Index](https://hitz-zentroa.github.io/lm-contamination/)

## Contributing
The amount of datasets and models is daunting. We are thus envisioning a community effort. If you are passionate about NLP research and want to contribute against contamination in LLM evaluation, please follow the [contribution guidelines](CONTRIBUTING.md)

## Citation
If you want to refer to this work we would appreciate if you cite the followings:

> Oscar Sainz, Jon Ander Campos, Iker Garc ́ıa-Ferrero, Julen Etxaniz, and Eneko Agirre. Did chatgpt cheat on your test?, Jun 2023. URL https://hitz-zentroa.github.io/lm-contamination/blog/.
```bibtex
@misc{sainz2023chatgpt,
    title={Did ChatGPT cheat on your test?},
    url={https://hitz-zentroa.github.io/lm-contamination/blog/}, 
    author={Sainz, Oscar and Campos, Jon Ander and García-Ferrero, Iker and Etxaniz, Julen and Agirre, Eneko}, 
    year={2023}, 
    month={Jun}
} 
```

>  Oscar Sainz, Jon Campos, Iker García-Ferrero, Julen Etxaniz, Oier Lopez de Lacalle, and Eneko Agirre. 2023. [NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark](https://aclanthology.org/2023.findings-emnlp.722). In Findings of the Association for Computational Linguistics: EMNLP 2023, pages 10776–10787, Singapore. Association for Computational Linguistics.
```bibtex
@inproceedings{sainz-etal-2023-nlp,
    title = "{NLP} Evaluation in trouble: On the Need to Measure {LLM} Data Contamination for each Benchmark",
    author = "Sainz, Oscar  and
      Campos, Jon  and
      Garc{\'\i}a-Ferrero, Iker  and
      Etxaniz, Julen  and
      de Lacalle, Oier Lopez  and
      Agirre, Eneko",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2023",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-emnlp.722",
    doi = "10.18653/v1/2023.findings-emnlp.722",
    pages = "10776--10787",
    abstract = "In this position paper we argue that the classical evaluation on Natural Language Processing (NLP) tasks using annotated benchmarks is in trouble. The worst kind of data contamination happens when a Large Language Model (LLM) is trained on the test split of a benchmark, and then evaluated in the same benchmark. The extent of the problem is unknown, as it is not straightforward to measure. Contamination causes an overestimation of the performance of a contaminated model in a target benchmark and associated task with respect to their non-contaminated counterparts. The consequences can be very harmful, with wrong scientific conclusions being published while other correct ones are discarded. This position paper defines different levels of data contamination and argues for a community effort, including the development of automatic and semi-automatic measures to detect when data from a benchmark was exposed to a model, and suggestions for flagging papers with conclusions that are compromised by data contamination.",
}
```
