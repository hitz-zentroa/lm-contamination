# Contributing to the LM Contamination Index

As we mention in the blog post, the number of datasets and models is daunting; therefore, we are looking for contributions to the LM Contamination Index.

If you have a model-dataset configuration that you would like to add to the LM Contamination Index, please follow the steps below:

0. Check if your configuration does not already exist. Use the search tool [LM Contamination Index](https://hitz-zentroa.github.io/lm-contamination/)
1. Test the contamination level following the **evaluation protocol**. (See the section below)
2. Fork the repository
3. Add your results as a new row to the `data.json` file.
4. Create a pull request

## Evaluation protocol

The evaluation protocol is the same as the one used in the blog post.

Ask the LM at least one of the following prompts:
1. (zero-shot) `Please, generate the first instances of {DATASET_NAME} dataset {SPLIT} split in {FORMAT} format.`
2. (few-shot) `{DATASET_NAME}:\n {FEW_DATASET_INSTANCES}`

The first prompt is intended to be used with instruction tuned models, whereas the second can be used with standard LMs.

**How to determine the level of contamination?**

There could be different levels of contamination, and, as we are measuring them by the memorization level of the LM, we are using the following guidelines:

* The model is **contaminated** if it is able to generate examples of the dataset (text or labels).
* The model is **suspicious** if it is able to generate characteristic attributes such as data format, ids, or other relevant information that characterizes the dataset. 
* We consider the model to be **clean** if the it is not able to generate anything that is reflected in the original dataset.
* If a specific split of a dataset is not publicly available, we use the label `n/a`. 

**How to post the results**

In addition to the results, we would like to see the number of executions needed to obtain the result and a screenshot that serves as "evidence".
