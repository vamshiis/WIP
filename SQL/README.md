```markdown
# 🗄️ SQL Server & Database Engineering

Welcome to the Database Engine Room! This directory contains my daily scripts, queries, and architectural practice using **Microsoft SQL Server (SSMS)**. 

My current focus is mastering how data is stored, manipulated, and precisely filtered before moving into complex relational models.

---

### 🏆 Current Arsenal (Mastered Concepts)

Here is a breakdown of the core SQL mechanics I am currently utilizing in this workspace:

* **The SQL Engine (Order of Execution):** Understanding that how we *write* SQL is different from how the machine *reads* it. 
  *(e.g., The engine processes `FROM` and `WHERE` before it ever looks at `SELECT`!).*
* **DDL (Data Definition Language):** Architecting the actual database structures.
  * `CREATE`, `ALTER`, `DROP`, and `TRUNCATE` tables and schemas.
* **DML (Data Manipulation Language):** Controlling the data that lives inside the structures.
  * `INSERT` (adding records), `UPDATE` (modifying existing data), and `DELETE` (removing rows).
* **Precision Filtering:** Using the `WHERE` clause to surgically extract specific data sets using logical operators:
  * **Comparisons:** `=`, `<`, `>`, `<=`, `>=`
  * **Ranges & Lists:** `BETWEEN`, `IN`
  * **Pattern Matching:** `LIKE` (using `%` and `_` wildcards)
  * **Logical Chaining:** `AND`, `OR`, `NOT`

---

### 🗺️ The Roadmap (Coming Soon...)

As I progress through my SQL journey, these files will be updated with advanced data engineering concepts:

* [ ] **Relational Data:** Primary Keys, Foreign Keys, and Database Normalization.
* [ ] **Data Blending:** `INNER JOIN`, `LEFT/RIGHT JOIN`, `FULL OUTER JOIN`, and `UNION`.
* [ ] **Aggregations:** Summarizing data using `GROUP BY`, `HAVING`, and math functions (`SUM()`, `COUNT()`, `AVG()`).
* [ ] **Advanced Logic:** `CASE` statements for conditional outputs.
* [ ] **Pro-Level Queries:** Subqueries, CTEs (Common Table Expressions), and Window Functions.

> *"Data is just noise until you know how to query it."* 🚀

```