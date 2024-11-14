# Project Improvements and Key Ideas

## Overview

To address limitations in current Gen AI interfaces and the inability to set hyperparameters, the following improvements focus on structuring prompts to encourage more robust and consistent responses.

## Prompt Structuring and Hyper-Parameters

Since we cannot adjust settings like temperature, refining prompt structure can improve response quality. Include this in standard prompts to enhance clarity and factual accuracy:

> "Please provide a clear, well-supported response. Focus on fact-based information, use relevant data or sources where possible, and avoid speculation. Summarize key points and offer a balanced view."

This prompt guides the model in delivering precise, factual answers, enhancing clarity and accuracy.

## Additional Improvements

### 1. Enhancing Grading Accuracy

**Challenge**: During testing, the system struggles particularly with the **Achieved-Merit grade boundary**. This issue stems from the model's difficulty in interpreting taxonomy-based grading, such as accurately identifying "explain" level ideas.

To address this challenge and improve the model’s grading ability, consider the following approaches:

- **Real-World Samples Collection**: Gather a set of student work samples from schools. Comparing model responses to educator feedback will help gauge accuracy against authentic grading criteria.
  
- **Synthetic Data for Testing**: Develop synthetic data with clear grading labels and criteria. This controlled testing environment allows for a structured feedback loop, highlighting areas for improvement in grading consistency.

Combining real-world samples and synthetic data creates a balanced approach to evaluate and refine the model’s accuracy, especially at critical grade boundaries like Achieved-Merit.
