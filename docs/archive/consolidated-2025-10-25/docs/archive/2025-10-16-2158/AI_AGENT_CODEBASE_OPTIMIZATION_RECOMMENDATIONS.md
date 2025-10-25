# AI Agent Codebase Optimization: Recommendations

This document provides a set of actionable recommendations for making the Te Kete Ako codebase more friendly for AI agent collaboration. The recommendations are based on an analysis of the existing codebase and external research into best practices for AI-friendly code.

## 1. Executive Summary

The Te Kete Ako codebase has a strong architectural foundation and good documentation. However, several key areas need improvement to facilitate effective collaboration with AI agents. The most critical issues are the presence of large, monolithic functions, a lack of automated tests, and tight coupling between components.

The following recommendations are prioritized by impact and feasibility:

1.  **Refactor Monolithic Functions:** Break down large functions into smaller, single-responsibility functions.
2.  **Introduce a Comprehensive Testing Suite:** Implement unit and integration tests for all core components.
3.  **Decouple Components with a Message Queue:** Use a message queue to communicate between the different parts of the "brain".
4.  **Adopt a More Structured Prompt Management Strategy:** Move away from large, monolithic prompt strings to a more structured approach.
5.  **Implement a "Dry Run" Mode for Destructive Operations:** Add a "dry run" mode to scripts that modify the database.

## 2. Detailed Recommendations

### 2.1. Refactor Monolithic Functions

**Problem:** The core logic in `kaitiaki-memory.ts` and `kaitiaki-cerebellum.ts` is contained in large, monolithic functions (`processArtifact` and `ingestDocument`). These functions are difficult for AI agents to understand, modify, and test.

**Recommendation:** Refactor these functions into smaller, single-responsibility functions that are composed into a pipeline.

**Example (`kaitiaki-cerebellum.ts`):**

The `ingestDocument` function could be refactored into a series of functions:

```typescript
function extractContent(filePath: string): Promise<string> { ... }
function chunkContent(content: string): string[] { ... }
async function processChunk(chunk: string): Promise<ExtractedData> { ... }
async function storeResults(results: ExtractedData[]): Promise<void> { ... }

async function ingestDocument(filePath: string): Promise<void> {
  const content = await extractContent(filePath);
  const chunks = chunkContent(content);
  const results = await Promise.all(chunks.map(processChunk));
  await storeResults(results);
}
```

**Benefits:**

*   **Improved Readability:** Smaller functions are easier to understand.
*   **Improved Testability:** Each function can be tested in isolation.
*   **Improved Modifiability:** AI agents can modify individual functions with less risk of breaking the entire system.

### 2.2. Introduce a Comprehensive Testing Suite

**Problem:** The codebase has no automated tests. This makes it very risky for AI agents to make changes, as there is no way to verify that the changes have not introduced regressions.

**Recommendation:** Introduce a testing framework (e.g., Jest, Vitest) and write unit and integration tests for all core components.

**Testing Priorities:**

1.  **Unit tests for pure functions:** Start by writing unit tests for pure functions like `chunkTextIntelligently` and `extractKeywords`.
2.  **Unit tests for content extraction:** Write unit tests for the functions that extract content from different file types.
3.  **Integration tests for the ingestion pipeline:** Write integration tests that test the entire ingestion pipeline, from reading a file to storing the results in the database.

**Benefits:**

*   **Increased Confidence:** A comprehensive test suite provides a safety net that allows AI agents to make changes with more confidence.
*   **Improved Code Quality:** Writing tests often leads to better-designed code.
*   **Executable Documentation:** Tests can serve as a form of executable documentation.

### 2.3. Decouple Components with a Message Queue

**Problem:** The "cerebellum" and "cortex" components are tightly coupled via a direct HTTP call. This makes the system less resilient to failures and harder to test.

**Recommendation:** Use a message queue (e.g., RabbitMQ, AWS SQS) to communicate between the components.

**Workflow:**

1.  The "cerebellum" reads a document and chunks it.
2.  For each chunk, it publishes a message to a "chunks-to-process" queue.
3.  The "cortex" subscribes to this queue, processes the chunks, and publishes the results to a "results" queue.
4.  The "cerebellum" subscribes to the "results" queue and stores the results in the database.

**Benefits:**

*   **Improved Resilience:** If the "cortex" is down, the messages will remain in the queue and will be processed when it comes back up.
*   **Improved Scalability:** You can run multiple instances of the "cortex" to process chunks in parallel.
*   **Improved Testability:** The components can be tested in isolation by mocking the message queue.

### 2.4. Adopt a More Structured Prompt Management Strategy

**Problem:** The `buildExtractionPrompt` function in `kaitiaki-cortex.ts` contains a large, monolithic string that is difficult for an AI to modify.

**Recommendation:** Use a more structured approach to manage prompts. This could involve:

*   **Template Engine:** Use a template engine like Handlebars or EJS to build the prompt from a template.
*   **Prompt as Code:** Define the prompt as a JavaScript object that is then serialized to JSON.
*   **Prompt Management Library:** Use a library like `langchain` to manage prompts.

**Benefits:**

*   **Improved Modifiability:** A structured approach makes it easier for an AI to add, remove, or modify parts of the prompt.
*   **Improved Readability:** Separating the prompt from the code makes the code easier to read.
*   **Improved Reusability:** Prompts can be reused across different parts of the application.

### 2.5. Implement a "Dry Run" Mode for Destructive Operations

**Problem:** The `kaitiaki-memory.ts` script directly modifies the database. This makes it risky for an AI to run, as a bug could potentially corrupt the database.

**Recommendation:** Implement a "dry run" mode that prints the actions that would be taken without actually performing them.

**Implementation:**

Add a command-line flag (e.g., `--dry-run`) to the script. If the flag is present, the script should print the SQL statements that it would execute instead of actually executing them.

**Benefits:**

*   **Increased Safety:** A "dry run" mode allows an AI to test its changes without risking the integrity of the database.
*   **Improved Debugging:** The output of the "dry run" mode can be used to debug issues with the script.
