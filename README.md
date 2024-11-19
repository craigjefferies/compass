# Compass: Custom GPT Framework for NCEA Achievement Standards

![Development Status](https://img.shields.io/badge/Development-Early%20Stage-yellow)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

**Compass** is a framework designed to help educators in New Zealand create custom GPT models aligned with **Achievement Standards** within the NCEA (National Certificate of Educational Achievement) framework. This tool guides teachers in crafting AI-driven learning assistants tailored to specific assessment standards, providing students with interactive support that matches the learning outcomes and grading criteria of each Achievement Standard.

> ## [**Teachers: Explore ChatGPT Models**](https://github.com/craigjefferies/compass/blob/main/ChatGPT-links.md)

## Table of Contents

- [Why Use Compass?](#why-use-compass)
- [Key Features](#key-features)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Why Use Compass?

Compass helps educators:

- **Create Targeted AI Assistants:** Align AI feedback with NCEA Achievement Standards, ensuring students receive guidance directly related to their learning goals.
- **Customize GPT Interactions:** Design prompts and feedback that build student understanding step-by-step.
- **Simplify Moderation and Grading:** Integrate Achievement Standards into AI feedback, ensuring student responses meet NCEA expectations.

## Key Features

- **Comprehensive Instructional Structure:** Compass provides an effective framework for creating instructional Language Learning Models (LLMs) tailored to NCEA Achievement Standards. This structured approach ensures that AI-driven interactions are aligned with specific educational goals and grading criteria.

- **Achievement Standard Integration:** Align each GPT model with specific NCEA Achievement Standards, allowing the AI to provide feedback based on real grading criteria (Achieved, Merit, and Excellence).

- **Adaptable Prompts and Fine-Tuning:** Customize prompts and responses to fit various Achievement Standards. This ensures interactions remain relevant to specific learning outcomes and criteria.

- **Modular Fine-Tuning Framework:** The fine-tuning setup is organized into three main sections:
  - **Static Instructions:** Generic instructions that define the LLM's behavior in an educational context.
  - **Standard-Specific Content:** Tailored prompts addressing the unique requirements of each Achievement Standard.
  - **Clarifications for Grading:** Detailed criteria for Achieved, Merit, and Excellence levels, enhancing the GPT's ability to respond with clarity and accuracy.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/craigjefferies/compass.git
    cd compass
    ```

2. **Install Dependencies:**

    ```bash
    npm install
    ```

3. **Set Up Environment Variables:**

    Create a `.env` file based on the provided `.env.example` and add your configuration settings.

## Getting Started

1. **Configure Achievement Standards:**
   - Define the NCEA Achievement Standards you wish to align with.
   - Customize prompts and responses within the `config` directory.

2. **Run the Framework:**

    ```bash
    npm start
    ```

3. **Access the AI Assistant:**
   - Use the provided [ChatGPT links](https://github.com/craigjefferies/compass/blob/main/ChatGPT-links.md) to interact with your custom models.

## Usage Examples

Provide examples or scenarios demonstrating how educators can use Compass to create and deploy AI assistants aligned with specific Achievement Standards.

```bash
# Example command to start a specific model
npm run start -- --model standard-xyz
