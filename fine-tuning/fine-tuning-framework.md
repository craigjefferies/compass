# Fine-Tuning Framework for Compass

This guide explains how to fine-tune custom GPT models within the **Compass** framework. Each model is tailored to provide NCEA-aligned feedback, assisting students with specific Achievement Standards in New Zealand’s educational framework.

## Fine-Tuning Structure

Fine-tuning in Compass is divided into three main sections:

### 1. Static Instructions
   **Purpose**: These are generic instructions that describe how the model should behave in an educational context. They ensure that the AI teaching assistant engages with students thoughtfully and respectfully, similar to how a teacher would guide them.

   **Example**:
   ```
   ### IDENTITY AND PURPOSE
   You are an AI educational assistant providing clear explanations, actionable feedback, and targeted resources. Always prioritize explicit evidence over inference to deepen student understanding and support effective teaching..
```
### 2. Standard-Specific Content
   **Purpose**: This section is customized to align the prompts with the specific Achievement Standard. It ensures the AI assistant provides feedback that reflects the learning outcomes and knowledge areas required by each standard.

   **Example**:
   ```
   ### ACHIEVEMENT STANDARD SPECIFICS
   ACHIEVEMENT_STANDARD_TITLE: Demonstrate understanding of genetic variation and change (Biology - AS2.5)  
   ACHIEVEMENT_STANDARD_PURPOSE: Students explain how ecological factors and natural selection lead to genetic changes within populations.
   ```
   Here, specific content related to genetic variation is set, guiding the AI to focus on this topic when interacting with students.

### 3. Clarifications for Grading
   **Purpose**: This section provides detailed criteria for Achieved, Merit, and Excellence grading levels. It helps the AI assistant give precise, targeted feedback aligned with the grading benchmarks of each Achievement Standard.

   **Example**:
   ```
   ### ACHIEVEMENT_STANDARD_GRADING_CLARIFICATIONS

   - **ACHIEVED (A3 & A4)**:
     - **KEY INDICATORS:** Provides clear definitions, uses Punnett squares for monohybrid or dihybrid inheritance, and describes genetic variation with examples, including the founder effect or genetic bottlenecks.
     - **APPROACH:** Prompt with questions like, “How does mutation introduce new alleles into a gene pool?” or “What is the significance of the 2:1 phenotype ratio in lethal alleles?”
   
   - **EXCELLENCE (E7 & E8)**:
     - **KEY INDICATORS:** Insightfully links genetic concepts and ecological factors, demonstrating advanced reasoning.
     - **APPROACH:** Encourage analytical depth by asking, “How might genetic drift during a bottleneck event differ from genetic drift in a stable population?”
```
   This breakdown provides clear indicators and sample questions that the AI assistant can use to guide students at each achievement level.

## Example Fine-Tuning Workflow

1. **Start with Static Instructions**: Set up the general behavior guidelines to ensure the AI assistant is approachable and supportive.
   
2. **Add Standard-Specific Content**: Customize this section to align with the Achievement Standard’s specific requirements, like focusing on genetic variation for a biology standard.

3. **Refine Grading Clarifications**: Use detailed descriptors for Achieved, Merit, and Excellence levels to guide the model’s feedback. Test responses to ensure they align well with NCEA grading.

By structuring fine-tuning this way, Compass creates AI assistants that are not only educational but also aligned with NCEA Achievement Standards, enhancing the support students receive in their studies.
