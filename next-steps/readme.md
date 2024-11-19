# Project Improvements and Key Ideas


## 1.Prompt Structuring and Hyper-Parameters

Since we cannot adjust settings / hyperparamters like temperature in a consumer facing product like ChatPGT, refining prompt structure could improve response quality. Playing with the generic educational prompt set may provide improvements, example:

> "Please provide a clear, well-supported response. Focus on fact-based information, use relevant data or sources where possible, and avoid speculation. Summarize key points and offer a balanced view."

## 2.Parsing NZQA Achievement Standard PDF's
Would be very useful to be able to parse the AS PDF's to get exactly the information required in the correct output structure needed for the framework

## 3.Automating the process of creating and Fine-Tuning
The process of creating custom GPTs is lengthy, having some programmable solution would be great. Here is a UI interface element version with no programming logic, its how I imagine administrators could interact with the creation of these GPTs
> [If you more a developer here is an static Interface idea in streamlit](https://compass-7xbge7bantgy42qruygvgb.streamlit.app/)

## 4.Enhancing Grading Accuracy


**Challenge**: During testing, the system struggles particularly with the **Achieved-Merit grade boundary**. This issue stems from the model's difficulty in interpreting taxonomy-based grading, such as accurately identifying "explain" level ideas.

To address this challenge and improve the model’s grading ability, consider the following approaches:

- **Real-World Samples Collection**: Gather a set of student work samples from schools. Comparing model responses to educator feedback will help gauge accuracy against authentic grading criteria.
  
- **Synthetic Data for Testing**: Develop synthetic data with clear grading labels and criteria. This controlled testing environment allows for a structured feedback loop, highlighting areas for improvement in grading consistency.

Combining real-world samples and synthetic data creates a balanced approach to evaluate and refine the model’s accuracy, especially at critical grade boundaries like Achieved-Merit.
