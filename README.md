# Bynry Backend Engineering Intern Case Study
**Candidate:** Sujal Papalkar  

---

## 📌 Overview
This repository contains my solutions to the Bynry Backend Engineering Intern Case Study.

The case study evaluates:
- Code debugging and best practices
- Database design and scalability
- API development and business logic handling

---

## 🧩 Solution Breakdown

### 🔹 Part 1: Code Review & Debugging
- Identified issues like lack of validation, no transaction handling, and SKU duplication risks
- Implemented fixes ensuring:
  - Data consistency
  - Atomic transactions
  - Proper error handling

---

### 🔹 Part 2: Database Design
- Designed normalized schema supporting:
  - Multi-warehouse inventory
  - Supplier relationships
  - Inventory tracking logs
- Added constraints and indexing for scalability

---

### 🔹 Part 3: Low Stock Alert API
- Implemented API to:
  - Detect low inventory
  - Handle multiple warehouses
  - Include supplier details
- Considered edge cases and performance concerns

---

## ⚙️ Tech Stack
- Python (Flask)
- SQL (Relational Database Design)

---

## 🧠 Key Highlights
- Focus on **scalability and real-world constraints**
- Ensured **data integrity using transactions**
- Designed with **future extensibility in mind**

---

## ⚠️ Assumptions
- Fixed low-stock threshold
- Sales data availability assumed
- One primary supplier per product

---

## 🚀 Conclusion
This solution focuses on building a **robust, scalable, and production-ready backend system**, while handling incomplete requirements through logical assumptions.


## 📄 Case Study Document
Google Doc Link: https://docs.google.com/document/d/13UBsr6t-58GdVWz9c9LBxTbWziQ5CF7L60gFA997AW4/edit?usp=sharing