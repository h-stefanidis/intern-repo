# Reflection Answers on E2E Testing

## 1. What is the difference between E2E, unit, and integration testing?

- **Unit Testing:**
  - Tests individual components or functions in isolation.
  - Fast, focused on a single piece of code.
  - Helps catch bugs early in the development process.
- **Integration Testing:**
  - Verifies the interaction between multiple components or modules.
  - Ensures that combined parts work together as expected.
  - Can involve external dependencies (e.g., databases, APIs).
- **End-to-End (E2E) Testing:**
  - Simulates real user scenarios by testing the entire application workflow from start to finish.
  - Validates that all layers of the system (UI, backend, integrations) work together correctly.
  - Generally slower and more complex, but provides higher confidence that the system functions as intended in a production-like environment.

## 2. What are the key benefits of E2E tests in a real-world application?

- **Comprehensive Coverage:**  
  E2E tests ensure that all parts of the application—from the UI to backend services—work together, catching integration issues that unit and integration tests might miss.
- **User-Centric Validation:**  
  They simulate real user interactions and workflows, confirming that the application meets business requirements and user expectations.
- **Regression Prevention:**  
  Automated E2E tests can be run regularly (e.g., in CI/CD pipelines) to quickly detect if new changes break existing functionality.
- **Confidence in Production:**  
  By mimicking real-world usage, E2E tests provide assurance that the system will behave correctly in live environments.

## 3. How does automated testing help Focus Bear reduce regression bugs?

- **Frequent and Consistent Testing:**  
  Automated tests run on every code change or pull request, ensuring that any regressions are caught early before they reach production.
- **Faster Feedback Loops:**  
  Developers receive immediate notifications about failing tests, allowing them to address issues promptly.
- **Complete Workflow Verification:**  
  E2E tests simulate entire user journeys, catching issues that occur only when multiple components interact.
- **Reduced Manual Effort:**  
  Automation minimises the need for repetitive manual testing, freeing up time for developers to focus on new features and improvements.

## 4. What are some challenges of writing and maintaining E2E tests?

- **Complexity and Fragility:**  
  Because they interact with the full application stack, E2E tests can be fragile—small changes in the UI or backend may break them.
- **Slower Execution Times:**  
  E2E tests often take longer to run than unit tests, which can slow down the development feedback loop.
- **High Maintenance Overhead:**  
  Frequent changes in the application (especially in the UI) require regular updates to the tests to keep them reliable.
- **Environment Dependencies:**  
  E2E tests need a stable, production-like environment; variability in test environments (network issues, service availability) can lead to flaky tests.
- **Resource Intensity:**  
  Running a comprehensive suite of E2E tests can be resource-intensive, which might necessitate additional infrastructure for parallel test execution and faster feedback.
