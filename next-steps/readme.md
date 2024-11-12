# Idea and Improvements

Due to currently using standard Gen AI interfaces and the inability to set hyperparameters, consider structuring prompts to encourage robust responses.

In a standard prompt, include the following:

> "Please provide a comprehensive, fact-based response to the following question. Focus on well-supported information, include relevant data or sources where possible, and avoid speculative answers. Summarize key points clearly and provide a balanced perspective on the topic."

This phrasing can help guide the model to deliver well-considered, factual, and thorough answers, even when hyperparameters like temperature cannot be manually adjusted.

## Additional Ideas and Improvements

### Measuring Accuracy and Grading Ability

To quantify the model's grading accuracy, we could consider the following approaches:

- **Collate Real-World Samples from Schools**: Gathering a diverse set of student work from schools would enable us to evaluate the model against real grading standards and feedback from educators.
  
- **Generate Synthetic Data for Controlled Testing**: Creating synthetic data with predefined criteria and grading labels could allow for structured feedback loops. This synthetic dataset can simulate a wide range of grading scenarios, providing insights into the model’s grading consistency and accuracy.

By using both real-world samples and synthetic data, we can achieve a balanced approach for evaluating grading ability and improving the model’s accuracy and reliability in educational settings.
