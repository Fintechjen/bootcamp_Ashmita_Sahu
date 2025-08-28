# Finance A/B Testing Project

## Project Scoping
The problem we aim to address is whether a new digital financial education module leads to higher savings behavior compared to the existing module. Many users of the app struggle to consistently save money, and the company wants to test whether redesigned educational content improves engagement and financial outcomes. The **primary stakeholder** is the product team responsible for improving user engagement and retention, while the **end users** are the app’s customers who benefit from more effective financial tools and nudges.

To answer this question, we will run an **A/B test** where one group of users receives the old module (control) and another group receives the redesigned module (treatment). We will use **linear regression** to estimate the treatment effect on savings behavior while controlling for user demographics and baseline financial activity. The answer we seek is **predictive and causal**—we want to quantify whether the new module causally increases savings and by how much. A useful output will be a statistical estimate of the treatment effect (e.g., increase in average savings per user), along with confidence intervals, so that the product team can make an informed decision about whether to roll out the new module broadly.

---

## Goals → Lifecycle → Deliverables

- **Goals**
  - Measure whether the new module increases user savings.
  - Provide product team with actionable evidence for rollout decision.

- **Lifecycle**
  1. Define experiment and recruit users.  
  2. Collect A/B testing data.  
  3. Clean and preprocess data (stored in `/data/`).  
  4. Analyze using linear regression in Jupyter notebooks (`/notebooks/`).  
  5. Develop reusable analysis functions in `/src/`.  
  6. Summarize results and insights in `/docs/`.

- **Deliverables**
  - Clean dataset ready for modeling.  
  - Jupyter notebooks with regression analysis.  
  - Python functions/modules for re-use.  
  - Final report with causal inference results.  
