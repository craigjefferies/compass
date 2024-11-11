# Fine Tuning: Using Clarifications for Better Alignment with NCEA Standards

The **Clarifications** section in Compass refines the LLM’s feedback using **Evaluation**, **Key Indicators**, and **Approach** for each grading level. Each element provides a focused way to ensure the assistant’s feedback aligns closely with NCEA grading criteria and standards.

---

### Purpose of Fine Tuning

Fine-tuning allows Compass to:
1. **Match NCEA Standards**: Ensure the assistant's feedback is consistent with official criteria and expectations.
2. **Provide Precise Feedback**: Guide the LLM to respond in a way that reflects each level’s requirements, helping students understand how to improve.
3. **Maintain Consistency**: Increase accuracy by using clear benchmarks across different grading levels.

---

## Fine-Tuning Elements

First lets look at the Fine-Tuning section found within the context window or instruction set for each assessment.

```
### ACHIEVEMENT_STANDARD_GRADING_CLARIFICATIONS

- **NOT ACHIEVED (N1 & N2):**
  - **EVALUATION:** Has not fully met one or more of the **ACHIEVEMENT_CRITERIA_GRADING_LEVELS**.
  - **KEY INDICATORS:** Limited or unclear description of the outcome's purpose or basic functionality. Lacks sufficient testing or refinement.
  - **APPROACH:** Guide the student to clearly articulate the purpose of the project, outline specific user needs, and conduct initial testing. Prompt with questions such as, “What’s the main goal of your outcome?” and “How can testing reveal areas to improve?”

- **ACHIEVED (A3 & A4):**
  - **EVALUATION:** Demonstrates understanding by developing an outcome that meets basic requirements and functions as intended.
  - **KEY INDICATORS:** Shows basic functionality that aligns with user needs, includes testing, and addresses fundamental requirements.
  - **APPROACH:** Encourage the student to refine their outcome by identifying and incorporating basic feedback. Use questions like, “What did you discover during testing that could improve the outcome?” and “How can you ensure it meets user requirements?”

- **MERIT (M5 & M6):**
  - **EVALUATION:** Refines the outcome by applying conventions and making improvements based on test results.
  - **KEY INDICATORS:** Demonstrates improved functionality by responding to testing insights and refining aspects based on digital domain conventions.
  - **APPROACH:** Guide the student to focus on specific conventions that enhance the outcome. Ask questions like, “What conventions from this field could you apply to improve functionality?” and “How did user feedback inform your recent changes?”

- **EXCELLENCE (E7 & E8):**
  - **EVALUATION:** Enhances the outcome with sophisticated testing, refining based on trials to meet high standards of user functionality and experience.
  - **KEY INDICATORS:** Shows advanced understanding and refinement, optimizing the outcome based on extensive testing and user feedback.
  - **APPROACH:** Encourage the student to explore the deeper aspects of user experience and functionality. Use questions like, “What adjustments will have the most impact on user satisfaction?” and “How does this enhancement address a specific user need?”
 
```
Each clarification is made up of three elements that serve specific roles in guiding the LLM’s responses:

### 1. **Evaluation**
   - **What it Represents**: An overview statement describing what is required to meet the specific grading level.
   - **Role in Fine-Tuning**: Defines the key expectations of each level (e.g., Not Achieved, Achieved, Merit, Excellence), giving the LLM a simple benchmark to guide feedback.
   - **How it Helps**: Ensures the assistant’s feedback stays aligned with NCEA grading standards by setting clear level-specific goals.

### 2. **Key Indicators**
   - **What it Represents**: Specific characteristics or qualities that distinguish work at each grading level.
   - **Role in Fine-Tuning**: Provides detailed benchmarks for each level that clarify what the assistant should look for in student responses.
   - **How it Helps**: Improves feedback quality by highlighting what’s typical for each level, from “basic description” (Achieved) to “sophisticated analysis” (Excellence). Helps the assistant recognize and reflect on these elements to match NCEA expectations.

### 3. **Approach**
   - **What it Represents**: Suggested prompts or questions to guide students in improving their work.
   - **Role in Fine-Tuning**: Provides the assistant with ways to prompt the student toward deeper thinking or more specific improvements, based on where they currently stand.
   - **How it Helps**: Encourages the LLM to help students reach the next level by asking guiding questions. This makes feedback more interactive and supportive, encouraging students to reflect and revise their responses based on the specific level requirements.

---

## How to Apply Fine-Tuning

When fine-tuning, you can:
1. **Use Evaluation to Set the Tone**: Ensure each level’s response aligns with its expectations.
2. **Apply Key Indicators for Specificity**: Guide the assistant to comment on particular strengths or areas needing improvement.
3. **Leverage Approach for Constructive Feedback**: Encourage students to consider specific aspects that will help them reach higher achievement levels.

By refining these elements, Compass ensures that feedback is not only accurate but also actionable, supporting students in their understanding and progress according to NCEA standards.
