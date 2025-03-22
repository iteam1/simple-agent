### Planning

This content outlines a structured approach to problem-solving by systematically analyzing tasks, identifying available and missing information, and developing an efficient step-by-step plan. It ensures clarity, adaptability, and effective resource utilization throughout the process.  

Key objectives:  
1. **Decomposing complex problems into manageable steps.**  
2. **Gathering all necessary information before execution.**  
3. **Continuously refining the plan based on new insights.**  
4. **Maximizing efficiency through tools and collaboration.**

---

#### **1. Fact-Gathering and Analysis**
- The **initial_facts** section helps establish a clear understanding of what is known and what still needs to be discovered.
- It categorizes facts into:
  1. **Facts given in the task** – Explicit information available.
  2. **Facts to look up** – Missing information requiring external sources.
  3. **Facts to derive** – Logical conclusions or calculations based on existing facts.

- The **update_facts_pre_messages** and **update_facts_post_messages** ensure that facts are continuously revised based on new discoveries during the problem-solving process.

#### **2. High-Level Planning**
- The **initial_plan** section instructs how to create a structured, high-level plan that breaks down the task into individual steps.
- It emphasizes:
  - Using available tools efficiently.
  - Avoiding unnecessary steps.
  - Ensuring completeness without detailing low-level operations.
  - Including an `<end_plan>` marker to signal plan completion.

- The **update_plan_pre_messages** and **update_plan_post_messages** ensure that plans are updated as progress is made, incorporating new facts and adjusting strategies accordingly.

#### **3. Collaboration and Tool Utilization**
- The framework allows for calling external tools and delegating tasks to human team members.
- It provides a structured way to integrate available resources dynamically into the problem-solving workflow.

### Example

Here’s a concrete example using this framework. Suppose the task is:

**Task:** *"Develop a chatbot that answers customer inquiries about an insurance policy."*

---

#### **1. Initial Facts Analysis**
**(Generated from `initial_facts`)**
```
#### 1. Facts given in the task
- The chatbot is for answering customer inquiries.
- The domain is insurance policies.

#### 2. Facts to look up
- What types of insurance policies are covered?
- What are the common customer inquiries?
- Are there any legal compliance requirements for chatbot responses?
- What existing datasets or knowledge bases can we use for training?

#### 3. Facts to derive
- The chatbot's architecture (e.g., retrieval-based vs. generative).
- Key intents and entities required for natural language understanding (NLU).
- Integration points with backend insurance systems.
```

---

#### **2. Initial Plan**
**(Generated from `initial_plan`)**
```
Step 1: Gather insurance policy details from the company's documentation.
Step 2: Research common customer inquiries from past support logs or FAQs.
Step 3: Identify legal constraints and compliance requirements for automated responses.
Step 4: Design a chatbot architecture that aligns with the task requirements.
Step 5: Choose an appropriate NLP model or chatbot framework.
Step 6: Develop an intent classification system and entity recognition.
Step 7: Train the chatbot using insurance-specific datasets.
Step 8: Implement API integrations with backend systems for real-time data access.
Step 9: Conduct testing with sample queries and refine responses.
Step 10: Deploy the chatbot and monitor for improvements.
<end_plan>
```

---

#### **3. Updating Facts and Plan During Execution**
After gathering more information, we refine the facts and update the plan.

**Updated Facts (`update_facts_post_messages`)**
```
#### 1. Facts given in the task
- The chatbot answers customer inquiries about insurance policies.

#### 2. Facts that we have learned
- The insurance policies cover health, auto, and home insurance.
- Common inquiries include policy coverage, claims process, and premium calculations.
- The chatbot must comply with GDPR regulations for customer data protection.

#### 3. Facts still to look up
- Exact API specifications for backend integration.
- Performance benchmarks for different NLP models.

#### 4. Facts still to derive
- Best approach to handle multi-turn conversations in the chatbot.
- Optimization strategies for response accuracy.
```

**Updated Plan (`update_plan_post_messages`)**
```
Step 1: Finalize data sources for chatbot training (FAQs, support logs, insurance docs).
Step 2: Develop a compliance-aware response generation mechanism.
Step 3: Implement NLP model with fine-tuned insurance-specific data.
Step 4: Establish API connections with policy databases.
Step 5: Deploy a prototype and collect user feedback for iterative improvement.
Step 6: Enhance chatbot performance based on real-world interactions.
<end_plan>
```

### **Key Takeaways**
1. **Structured problem-solving** – The task is broken into clear steps.
2. **Fact-based planning** – Ensures all required information is gathered before execution.
3. **Continuous iteration** – Updates facts and plans based on new discoveries.
4. **Practical use of tools and collaboration** – Identifies where to use tools, APIs, or team members.