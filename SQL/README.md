# 🗄️ Database Engineering & SQL

![Microsoft SQL Server](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

Welcome to the Database Engine Room! This directory contains my daily scripts, queries, and architectural practice. 

**Note on Cross-Compatibility:** While my current focus and environment utilize **Microsoft SQL Server (SSMS)**, the core SQL logic, execution orders, 

and foundational syntaxes I am mastering here are highly transferable and allow me to confidently handle **MySQL** and **PostgreSQL** databases as well.

---

### 🏆 Current Arsenal (Mastered Concepts)

Here is a breakdown of the core SQL mechanics I am currently utilizing in this workspace:

🔹 **The SQL Engine (Order of Execution)** 

Understanding that how we *write* SQL is different from how the machine *reads* it. 

*(e.g., The engine processes `FROM` and `WHERE` before it ever looks at `SELECT`!).*

🔹 **DDL (Data Definition Language)** 

Architecting the actual database structures.

↳ `CREATE`, `ALTER`, `DROP`, and `TRUNCATE` tables and schemas.

🔹 **DML (Data Manipulation Language)** 

Controlling the data that lives inside the structures.

↳ `INSERT` (adding records), `UPDATE` (modifying existing data), and `DELETE` (removing rows).

🔹 **Precision Filtering** Using the `WHERE` clause to surgically extract specific data sets using logical operators:

↳ **Comparisons:** `=`, `<`, `>`, `<=`, `>=`

↳ **Ranges & Lists:** `BETWEEN`, `IN`

↳ **Pattern Matching:** `LIKE` (using `%` and `_` wildcards)

↳ **Logical Chaining:** `AND`, `OR`, `NOT`

---

### 📖 The Roadmap (Coming Soon...)

As I progress through my SQL journey, these files will be updated with advanced data engineering concepts:

🚀 **Relational Data:** Primary Keys, Foreign Keys, and Database Normalization.

🚀 **Data Blending:** `INNER JOIN`, `LEFT/RIGHT JOIN`, `FULL OUTER JOIN`, and `UNION`.

🚀 **Aggregations:** Summarizing data using `GROUP BY`, `HAVING`, and math functions (`SUM()`, `COUNT()`, `AVG()`).

🚀 **Advanced Logic:** `CASE` statements for conditional outputs.

🚀 **Pro-Level Queries:** Subqueries, CTEs (Common Table Expressions), and Window Functions.

> *"Data is just noise until you know how to query it."* 📊