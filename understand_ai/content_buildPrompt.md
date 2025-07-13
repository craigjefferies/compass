# AS91898 Content Knowledge File

---

### 1. Metadata
- Assessment Code and Title: AS91898 – Demonstrate understanding of a computer science concept
- Level and Credits: Level 2, 3 Credits
- Key Topics: Artificial Intelligence, Mechanisms (e.g., CNN, LLM, Recommenders), Impacts (bias, privacy), Metrics, Data pipeline, Real-world applications
- Last Updated: 2025-07-13
- Scaffolding Notes: Simple = Achieved (name, describe); Detailed = Merit (explain, connect cause/effect); Implication = Excellence (evaluate, judge, propose fix)
- Source Files Used: as91898.pdf, as91898.json, CS_Exam_AI_Resource.txt, 91898-cat-B-2023.pdf

---

### 2. Key Terms

| Term | Definition |
|------|------------|
| Artificial Intelligence | Software that mimics human thinking to perform tasks. |
| Mechanism | A process or algorithm that makes the AI system work. |
| Impact | A consequence of using AI (ethical, social, human-factor, etc). |
| Machine Learning (ML) | A method where computers learn patterns from data. |
| Neural Network (NN) | A layered model that adjusts weights to recognize patterns. |
| Natural Language Processing (NLP) | AI that processes and generates human language. |
| Supervised Learning | ML using labeled data to learn patterns. |
| Convolution | A NN step that detects edges and features in images. |
| Backpropagation | A method for updating weights to reduce error in NN training. |
| Accuracy | Proportion of correct predictions overall. |
| Precision | How often predicted positives are actually correct. |
| Precision@K | Accuracy of top-K recommendations. |
| Perplexity | A measure of surprise in text prediction; lower is better. |
| Bias | Systematic unfairness in outcomes. |
| Privacy | Risks from collecting or storing sensitive data. |
| Explainability | How clearly we can understand AI’s decisions. |
| Misuse | Harmful or unintended use of AI. |
| Data Pipeline | Steps to collect, clean, split, and evaluate data for ML. |
| Future-proofing | Designing AI to stay relevant or safe long-term. |
| Chatbot | An AI system that interacts using natural language. |

---

### 3. Knowledge Tables (Grouped by Major Topics)

#### 1. AI Mechanisms

| # | Concept/Sub-Concept | Simple Sentence | Detailed Idea | Key Process / Formula | Quick Example | Implication / Risk / Misconception | OMI Link |
|----|----------------------|------------------|----------------|------------------------|----------------|--------------------------------------|-----------|
| 1.1 | Supervised Classification | Learns to sort examples into groups. | Finds a decision boundary using labeled data. | Accuracy = Correct ÷ Total | Spam filter labels 95 of 100 correctly. | High bias if training data lacks diversity. | OMI:describe_usage |
| 1.2 | CNN (Convolutional Neural Network) | Sees edges and shapes in images. | Layers convert pixels → edges → shapes → object. | Convolution layer, ReLU, Pooling | Detects pedestrians for braking. | Black-box decisions are hard to explain. | OMI:explain_mechanism |
| 1.3 | Transformer / LLM | Predicts next word in text. | Uses self-attention to weight words and generate output. | Self-attention mechanism | Summarizes doctor notes. | May hallucinate facts, causing errors. | OMI:explain_mechanism |
| 1.4 | Recommender System | Suggests based on similar users. | Compares user preferences using collaborative filtering. | Precision@K = hits ÷ top-K | TikTok "For You" feed. | Echo chambers reduce content diversity. | OMI:explain_application |

#### 2. Metrics and Evaluation

| # | Concept/Sub-Concept | Simple Sentence | Detailed Idea | Key Process / Formula | Quick Example | Implication / Risk / Misconception | OMI Link |
|----|----------------------|------------------|----------------|------------------------|----------------|--------------------------------------|-----------|
| 2.1 | Accuracy | Measures how often the model is right. | Accuracy = correct predictions ÷ total predictions. | Accuracy = TP + TN / Total | CNN classifies 95/100 correctly = 95%. | Doesn’t reflect false positives/negatives. | OMI:explain_application |
| 2.2 | Precision | Tells how correct the model's "yes" predictions are. | Precision = TP ÷ (TP + FP). | 45/50 flagged as spam were correct → 90%. | Precision focuses on false positives. | High precision ≠ high accuracy. | OMI:analyse_impact |
| 2.3 | Perplexity (NLP) | Lower means smoother, more predictable text. | Measures model surprise; lower is better. | Perplexity = 2^cross-entropy | Perplexity 15 better than 25. | Doesn't apply to image or recommender AI. | OMI:analyse_impact |

#### 3. Data Pipeline

| # | Concept/Sub-Concept | Simple Sentence | Detailed Idea | Key Process / Formula | Quick Example | Implication / Risk / Misconception | OMI Link |
|----|----------------------|------------------|----------------|------------------------|----------------|--------------------------------------|-----------|
| 3.1 | Data Collection | Gather data the model can learn from. | Images, text, or logs are collected from the field. | Step 1 | Dashcam images from city streets. | Poor quality data = poor AI. | OMI:explain_application |
| 3.2 | Data Cleaning | Remove errors and sensitive info. | Blur faces, remove duplicates, normalize values. | Step 2 | Blur faces in dashcam for privacy. | Missed cleaning = privacy or bias risk. | OMI:propose_mitigation_or_future_proofing |
| 3.3 | Train/Test Split | Train the model, then test accuracy. | Split data to train and evaluate model separately. | 80% train, 20% test split | CNN trains on 800, tests on 200 images. | Testing on train data gives false accuracy. | OMI:explain_mechanism |

#### 4. Ethical and Social Impacts

| # | Concept/Sub-Concept | Simple Sentence | Detailed Idea | Key Process / Formula | Quick Example | Implication / Risk / Misconception | OMI Link |
|----|----------------------|------------------|----------------|------------------------|----------------|--------------------------------------|-----------|
| 4.1 | Bias | AI can treat groups unfairly. | Unbalanced data leads to unequal results. | Reweighting, diverse data | Misses dialect → wrongly silences group. | Fails fairness and causes harm. | OMI:discuss_key_issues |
| 4.2 | Privacy | AI might leak private data. | AI models may store or expose sensitive input. | Anonymise / Encrypt | Chatbot stores conversation logs. | User data can be misused or hacked. | OMI:analyse_impact |
| 4.3 | Explainability | Hard to know how decisions were made. | Complex models (e.g. NN) are hard to audit. | Use heatmaps or reports | CNN brakes, no reason visible. | Low trust, legal accountability issues. | OMI:discuss_key_issues |
| 4.4 | Misuse / Security | AI may be used for harm. | Deepfakes, scams, or adversarial attacks. | Watermarking / Detection tools | AI voice clones scam calls. | Technology used for deception. | OMI:evaluate_issue_significance |

---

### 4. Common Misconceptions / Errors

- Confusing accuracy with precision (Fails OMI:explain_application)
- Describing AI without naming a specific mechanism (Fails OMI:identify_concept)
- Listing an AI application without linking it to a mechanism (Fails OMI:describe_usage)
- Saying "AI is helpful" without showing how it solves a problem (Fails OMI:explain_application)
- Mentioning bias or privacy without explaining cause and effect (Fails OMI:analyse_impact)
- Stating future-proofing ideas without linking to a specific issue (Fails OMI:propose_mitigation_or_future_proofing)
- Giving vague pros/cons without linking to the context (Fails OMI:articulate_advantage_or_limitation)
- Explaining a task but not the internal step (Fails OMI:explain_mechanism)

---

### 5. Sources
- NZQA Assessment Standard PDF: as91898.pdf
- OMI JSON file: as91898 (1).json
- Past Exams: 91898-cat-B-2023.pdf
- Curriculum Resource: CS_Exam_AI_Resource.txt (2025 Content Guide)

