What are loops ??
- Loops are used to Control the flow of code.
- Repeat a block of code over and over until a condition is met.
- we have 2 main types of loops
      - For loop 
      - While Loop

## Loop Comparison: For vs. While

| Loop Criteria | for loop | while loop |
| :--- | :--- | :--- |
| **Loop Criteria** | Loops over a fixed sequence | Loops while a condition is True |
| **Condition flexibility** | • Predefined condition.<br>• Asks always if the sequence is completed.<br>• Cannot change the condition (no flexibility). | • Totally flexible.<br>• We can add our own conditions. |
| **When to use** | • If Number of Iterations are known.<br>• To loop through the data / Processing Data like through <br>tables, columns, rows to clean up the data. | • If Nr. of Iterations are unknown.<br>• Waiting for the External event or trigger.<br>• We use when we build retries in the login, connecting to database or API's. |
| **Advantages** | • Simple<br>• Clear<br>• Safe | • Advanced<br>• Flexible<br>• Adds dynamic to our logic |
| **Disadvantages** | • Limited: always need to Pre-define the number of iterations. | • More complex.<br>• Have high risk of turning out to be infinite loop if handled loosely. |
| **Think of it as** | **Song’s Playlist:** We know how many songs are already present in the playlist. | **Waiting for the Reply:** Keep checking until the condition is met. |