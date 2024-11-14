# Project Improvements and Key Ideas

## Overview

**Challenge**: During testing, the system struggles particularly with the **Achieved-Merit grade boundary**. This issue stems from the model's difficulty in interpreting taxonomy-based grading (e.g., accurately identifying "explain" level ideas). The following improvements focus on refining the model's prompts to guide it toward clearer, more robust grading distinctions.

## Prompt Structuring for Consistency

As we currently use standard Gen AI interfaces without hyperparameter adjustments, refining prompt structure can improve response quality. Include this in standard prompts to enhance clarity and factual accuracy:

> "Please provide a clear, well-supported response. Focus on fact-based information, use relevant data or sources where possible, and avoid speculation. Summarize key points and offer a balanced view."

This prompt aims to guide the model in delivering precise, factual answers, even when we cannot manually adjust settings like temperature.

## Additional Improvements

### 1. Enhancing Grading Accuracy

To better assess and improve the model’s grading ability, consider the following approaches:

- **Real-World Samples Collection**: Gather a set of student work samples from schools. Comparing model responses to educator feedback will help gauge accuracy against authentic grading criteria.
  
- **Synthetic Data for Testing**: Develop synthetic data with clear grading labels and criteria. This controlled testing environment allows for a structured feedback loop, highlighting areas for improvement in grading consistency.

Combining real-world samples and synthetic data creates a balanced approach to evaluate and refine the model’s accuracy, especially at critical grade boundaries like Achieved-Merit.
