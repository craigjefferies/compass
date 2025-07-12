# AS91898 Artificial Intelligence – **Content Guide (2025)**
*Exactly what a 16- to 17-year-old beginner must memorise for the external exam.*

---

## 1. AI Basics 🧠
| Term | 1-line definition |
|------|------------------|
| **Artificial Intelligence** | Software that imitates human **decision-making tasks**. |
| **Learning vs Rules** | AI **learns from data patterns** (e.g., spam filter retrains); a rule-based program just follows fixed “if → then” steps (e.g., microwave timer). |
| **Narrow AI** | AI focused on a single task (lane-keeping, spam filter). |

---

## 2. Four Core AI Mechanisms ⚙️  
*Start with the **Simple sentence** (teen-friendly).  
Then read the **Exact idea** for exam wording.*

| # | Mechanism | **Simple sentence** | **Exact idea** (exam-level) | Quick example you can quote | Main risk / issue |
|---|-----------|---------------------|-----------------------------|-----------------------------|-------------------|
| 1 | **Supervised Classification** | “Learns to sort stuff into the right group (e.g., spam vs not-spam).” | Finds an **invisible line** that separates *labelled* examples into classes. | Social-media hate-speech filter. | **Bias** if training data is unbalanced. |
| 2 | **Convolutional Neural Network (CNN)** | “Finds shapes inside pictures so it can tell what’s there.” | Stacks layers that spot **pixels → edges → shapes → full objects** in an image. | Car camera spots pedestrians. | **Explainability** – black-box errors hard to trace. |
| 3 | **Transformer / LLM (NLP)** | “Finishes your sentence by guessing the next word.” | Looks back at every word, gives more weight to the important ones (**self-attention**), then predicts the next word. | Summarises doctor notes into plain English. | **Hallucinations** – can invent fake facts. |
| 4 | **Collaborative-Filtering Recommender** | “Shows you things that people with similar tastes liked.” | Compares your likes with other users and recommends items preferred by those most similar to you (**collaborative filtering**). | TikTok **“For You”** feed. | **Echo chambers** that limit diverse views. |


---

## 3. Essential Metrics 📏  
*Exam prompts often ask “How is this AI evaluated?” Quote **one** matching metric.*

| Use-case | Metric to quote | 1-line description | Micro example |
|----------|-----------------|--------------------|---------------|
| Any **classification** model | **Accuracy** | Correct predictions ÷ total predictions. | CNN labels 95 of 100 images right → **95 % accuracy**. |
| Costly false-positives | **Precision** | When the model says *positive*, how often it is right. | 45 of 50 flagged emails really spam → **90 % precision**. |
| **Recommender** system | **Precision@K** | Relevant items in top-K ÷ K. | 4 of top 5 videos match you → **P@5 = 0.8**. |
| **NLP** text model *(optional)* | **Perplexity** | “Average surprise” at next word – lower = better. | Perplexity 15 writes smoother text than perplexity 25. |

**Accuracy ≠ Precision**

| Term | Plain meaning | Tiny example |
|------|---------------|--------------|
| **Accuracy** | How often the model is right overall. | 90 / 100 emails correct ⇒ 90 % accuracy. |
| **Precision** | When the model says *positive*, how often it is right. | 45 / 50 flagged spam really spam ⇒ 90 % precision. |

---

## 4. Mini Data Pipeline 🛠️  
Quote these verbs *(train / test)* for an easy detail mark.  

1. **Collect** data (e.g., road images).  
2. **Clean** data (remove blur, anonymise faces).  
3. **Split** into **train / test** sets.  
4. **Evaluate** the trained model (metrics above).

---

## 5. The Four Big Ethical Issues 🔒
| Issue | One-line consequence | Simple mitigation |
|-------|---------------------|-------------------|
| **Bias** | Unfair results for some groups. | Balance or re-weight the data. |
| **Privacy** | Sensitive info exposed or misused. | Anonymise data; encrypt storage. |
| **Explainability** | Hard to see why a decision was made. | Heat-maps or plain-language reports. |
| **Misuse / Security** | Deepfakes, scams, attacks. | Digital watermarks; authenticity checks. |

---

## 6. Exam Command Verbs ✍️  
| Word in question | What you must do | Grade target |
|------------------|------------------|--------------|
| **Describe** | Say what it is **and** how it works; give an example. | Achieved |
| **Explain**  | Add “because … / which means …” to show effect or reason. | Merit |
| **Discuss / Evaluate** | State benefit → risk → judgement. | Excellence |

---

## 7. Three Worked Ladders (Describe → Explain → Discuss) 🏆  

### 7.1 Social-Media AI – Hate-Speech Filter  
| Level | Sentence starter | Key points |
|-------|------------------|-----------|
| **Describe** | “A **Supervised Classification** model labels posts **hate-speech** or **acceptable** using tagged examples.” | Name mechanism + task. |
| **Explain** | “This protects users **because** hateful posts are hidden; **accuracy** of 95 % means fewer harmful messages slip through.” | Benefit + metric. |
| **Discuss** | “But **bias** can occur: if the data misses a dialect, the filter wrongly silences that group. Balanced data and human review are needed to stay fair.” | Risk + mitigation. |

### 7.2 Car-Safety AI – CNN Pedestrian Detection  
| Level | Sentence starter | Key points |
|-------|------------------|-----------|
| **Describe** | “A **CNN** processes dash-cam images to spot **pedestrians** so the car can brake.” | Name mechanism + task. |
| **Explain** | “It cuts stopping distance **because** AI reacts faster than a person; tests show **95 % accuracy**, reducing crashes.” | Benefit + metric. |
| **Discuss** | “The issue is **explainability**: if the CNN mistakes a bag for a person and brakes, engineers can’t see **why**. Without clarity, trust and legal accountability suffer; heat-maps help but don’t solve everything.” | Risk + mitigation. |

### 7.3 Healthcare AI – LLM Discharge Summaries  
| Level | Sentence starter | Key points |
|-------|------------------|-----------|
| **Describe** | “A **Transformer / LLM** reads long clinical notes and outputs a short, plain-English **discharge summary**.” | Name mechanism + task. |
| **Explain** | “This saves doctor time **because** it removes jargon; lower **perplexity** scores show clearer text.” | Benefit + metric. |
| **Discuss** | “However, LLMs can **hallucinate**: a fake dosage risks patient safety. Mandatory human review and citing source text lower the danger.” | Risk + mitigation. |

---

## 8. Memory Card Checklist 📇  
- **4 mechanisms** → simple idea → vivid example.  
- Metrics: **Accuracy, Precision, Precision@K** (+ Perplexity optional).  
- Data verbs: **Collect → Clean → Split → Evaluate**.  
- Ethics: **Bias, Privacy, Explainability, Misuse**.  
- Verbs ladder: **Describe → Explain → Discuss**.  
- Example ladders: Hate-speech filter, CNN pedestrian, LLM summary.

*Master every bullet above and you’re set for any AS91898 AI question.*
