CREATE TABLE Companies (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    created_at TIMESTAMP
);

CREATE TABLE Warehouses (
    id INT PRIMARY KEY,
    company_id INT,
    name VARCHAR(255),
    location VARCHAR(255),
    FOREIGN KEY (company_id) REFERENCES Companies(id)
);

CREATE TABLE Products (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    sku VARCHAR(100) UNIQUE,
    price DECIMAL(10,2),
    product_type VARCHAR(100)
);

CREATE TABLE Inventory (
    id INT PRIMARY KEY,
    product_id INT,
    warehouse_id INT,
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES Products(id),
    FOREIGN KEY (warehouse_id) REFERENCES Warehouses(id)
);

CREATE TABLE Suppliers (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    contact_email VARCHAR(255)
);

CREATE TABLE Product_Suppliers (
    product_id INT,
    supplier_id INT,
    FOREIGN KEY (product_id) REFERENCES Products(id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(id)
);

CREATE TABLE Inventory_Logs (
    id INT PRIMARY KEY,
    product_id INT,
    warehouse_id INT,
    change INT,
    timestamp TIMESTAMP
);

CREATE TABLE Bundles (
    bundle_id INT,
    product_id INT,
    quantity INT
);