# AS91898 Content Knowledge File

---

### 1. Metadata
- Assessment Code and Title: AS91898 – Demonstrate understanding of a computer science concept
- Level and Credits: Level 2, 3 Credits
- Key Topics: Artificial Intelligence, Core Mechanisms (Supervised Learning, CNN, LLM, Recommenders), Metrics, Data pipeline, Ethical Impacts, Real-world Applications (Social Media, Car Safety, Healthcare)
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
| Accuracy | Proportion of correct predictions overall. |
| Precision | How often predicted positives are actually correct. |
| Precision@K | Accuracy of top-K recommendations. |
| Bias | Systematic unfairness in outcomes. |
| Privacy | Risks from collecting or storing sensitive data. |
| Explainability | How clearly we can understand AI’s decisions. |
| Misuse | Harmful or unintended use of AI. |
| Data Pipeline | Steps to collect, clean, split, and evaluate data for ML. |
| Future-proofing | Designing AI to stay relevant or safe long-term. |
| Chatbot | An AI system that interacts using natural language. |

---

### 3. Knowledge Tables (Grouped by Major Topics)

#### 3.1 Core AI Mechanisms

| # | Mechanism | Simple Sentence | Exam-Level Idea | Example | Main Risk |
|---|-----------|------------------|------------------|---------|------------|
| 1 | **Supervised Classification** | Learns to sort stuff into the right group (e.g., spam vs not-spam). | Finds an invisible line that separates *labelled* examples into classes. | Social media hate-speech filter. | Bias if training data is unbalanced. |
| 2 | **CNN (Convolutional Neural Network)** | Finds shapes inside pictures so it can tell what’s there. | Layers spot pixels → edges → shapes → objects. | Car camera spots pedestrians. | Black-box: can't explain why it stopped. |
| 3 | **Transformer / LLM (NLP)** | Finishes your sentence by guessing the next word. | Uses self-attention to predict next word based on context. | Summarises doctor notes. | Hallucinations: can invent fake facts. |
| 4 | **Collaborative Recommender** | Shows things people with similar tastes liked. | Suggests based on user similarity via collaborative filtering. | TikTok "For You" feed. | Echo chambers reduce content diversity. |

---

#### 3.2 Metrics and Evaluation

| # | Concept | Simple Sentence | Detailed Idea | Key Formula | Quick Example | Risk / Misconception |
|----|--------|------------------|----------------|-------------|----------------|------------------------|
| 2.1 | Accuracy | How often the model is right. | Accuracy = correct predictions ÷ total. | Accuracy = TP + TN / Total | CNN classifies 95/100 correctly = 95%. | Doesn’t reflect false positives/negatives. |
| 2.2 | Precision | How right the “yes” predictions are. | Precision = TP ÷ (TP + FP). | Precision = 45/50 | Model flags 50 emails as spam; 45 actually are. | High precision doesn’t mean high recall. |
| 2.3 | Perplexity (NLP) | Lower = better, smoother predictions. | Measures how surprised model is by next word. | 2^cross-entropy | Perplexity 15 better than 25. | Doesn’t apply to image models. |
| 2.4 | Precision@K | Evaluates recommendations. | Correct items in top-K ÷ K. | P@5 = 4/5 = 0.8 | 4 of top 5 videos are relevant. | Doesn’t reflect long-tail quality. |

---

#### 3.3 Data Pipeline

| # | Stage | Simple Sentence | Detailed Idea | Key Step | Example | Risk |
|----|--------|------------------|----------------|----------|---------|------|
| 3.1 | Collection | Gather examples for training. | Gather labelled or raw data. | Step 1 | Dashcam images. | Bad data = bad model. |
| 3.2 | Cleaning | Remove bad or private data. | Blur faces, fix errors, anonymise data. | Step 2 | Blur faces before training CNN. | Leaks, bias, or unfairness if skipped. |
| 3.3 | Split | Divide for fair training/testing. | Keep test data unseen during training. | Step 3 | 80% train, 20% test. | Reusing test data fakes results. |
| 3.4 | Evaluation | Measure performance. | Use metrics like accuracy and precision. | Step 4 | 95% accuracy, P@5 = 0.8 | No single metric tells full story. |

---

#### 3.4 Ethical and Social Impacts

| # | Issue | Simple Sentence | Detailed Idea | Example | Risk |
|----|-------|------------------|----------------|---------|------|
| 4.1 | Bias | AI can be unfair. | Training data might favour one group. | Misses dialect → unfair filter. | Discrimination or harm. |
| 4.2 | Privacy | AI might leak data. | Sensitive info can be exposed or stored. | Chatbot saves conversations. | Legal + ethical issues. |
| 4.3 | Explainability | Decisions are hard to trace. | Complex models like NNs are opaque. | CNN brakes suddenly. | Trust and accountability suffer. |
| 4.4 | Misuse | AI used in harmful ways. | Deepfakes, scams, or manipulation. | AI clones voice for scam. | Can undermine trust in media. |

---

### 4. Common Misconceptions / Errors

- Confusing accuracy with precision.
- Describing AI without naming a specific mechanism.
- Listing an AI use-case without linking to the correct method.
- Explaining what AI does, but not how it does it.
- Mentioning ethics (like bias) without explaining cause/effect.
- Talking about “future proofing” without linking to an actual risk.
- Vague pros/cons not tied to examples or mechanisms.

---

### 5. Applied Scenarios (Describe → Explain → Discuss)

#### 5.1 Social Media – Hate Speech Filter

| Level | Sentence Starter | Key Points |
|-------|------------------|------------|
| **Describe** | A **Supervised Classification** model labels posts as **hate-speech** or **acceptable**, using training examples. | Name mechanism and task. |
| **Explain** | This protects users **because** hate is filtered out. A high **accuracy** (e.g., 95%) means fewer harmful posts get through. | Benefit + metric. |
| **Discuss** | But **bias** can occur: dialects not in the training set might be wrongly flagged. To fix this, balance the data or add human review. | Risk + fix = Excellence. |

---

#### 5.2 Car Safety – CNN Pedestrian Detection

| Level | Sentence Starter | Key Points |
|-------|------------------|------------|
| **Describe** | A **CNN** scans dash-cam images to detect **pedestrians** so the car can brake. | Name mechanism and task. |
| **Explain** | It reduces reaction time **because** the AI sees objects faster than humans. A test showed **95% accuracy**. | Benefit + metric. |
| **Discuss** | The issue is **explainability**: if the CNN misidentifies an object and brakes, engineers may not know why. **Heatmaps** can help, but not fully solve the problem. | Risk + partial mitigation. |

---

#### 5.3 Healthcare – LLM Discharge Summaries

| Level | Sentence Starter | Key Points |
|-------|------------------|------------|
| **Describe** | A **Transformer / LLM** reads medical notes and creates a short, plain-English **discharge summary**. | Name mechanism and task. |
| **Explain** | It saves time **because** it removes jargon and improves readability. Lower **perplexity** = better summaries. | Benefit + metric. |
| **Discuss** | However, **hallucinations** can occur — the AI might invent a dosage. **Mandatory review by doctors** and source-text quoting help avoid harm. | Risk + mitigation. |

---

### 6. Sources
- NZQA Assessment Standard PDF: as91898.pdf  
- OMI JSON file: as91898 (1).json  
- Past Exams: 91898-cat-B-2023.pdf  
- Curriculum Resource: CS_Exam_AI_Resource.txt (2025 Content Guide)
