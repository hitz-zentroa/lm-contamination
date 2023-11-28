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
(To be updated with EMNLP-2023 Findings reference)
>  Oscar Sainz, Jon Ander Campos, Iker García-Ferrero, Julen Etxaniz, Oier Lopez de Lacalle, and Eneko Agirre. Nlp evaluation in trouble: On the need to measure llm data contamination for each benchmark, 2023. URL https://arxiv.org/abs/2310.18018
```bibtex
@misc{sainz2023nlp,
      title={NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark}, 
      author={Oscar Sainz and Jon Ander Campos and Iker García-Ferrero and Julen Etxaniz and Oier Lopez de Lacalle and Eneko Agirre},
      year={2023},
      eprint={2310.18018},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2310.18018}
}
```
