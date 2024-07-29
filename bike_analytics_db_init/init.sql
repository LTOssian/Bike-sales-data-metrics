CREATE TYPE age_group AS ENUM ('Youth (<25)', 'Young Adults (25-34)', 'Adults (35-64)', 'Seniors (65+)');
CREATE TYPE customer_gender AS ENUM ('M', 'F');
CREATE TYPE product_category AS ENUM ('Accessories', 'Bikes', 'Clothing');
CREATE TYPE sub_category AS ENUM (
    'Tires and Tubes',
    'Bottles and Cages',
    'Road Bikes',
    'Helmets',
    'Mountain Bikes',
    'Jerseys',
    'Caps',
    'Fenders',
    'Touring Bikes',
    'Gloves',
    'Cleaners',
    'Shorts',
    'Hydration Packs',
    'Socks',
    'Vests',
    'Bike Racks',
    'Bike Stands'
);

CREATE TABLE sales_data (
    Date DATE,
    Day INT,
    Month INT,
    Year INT,
    Customer_Age INT,
    Age_Group age_group,
    Customer_Gender customer_gender,
    Country VARCHAR(50),
    State VARCHAR(50),
    Product_Category product_category,
    Sub_Category sub_category,
    Product VARCHAR(100),
    Order_Quantity INT,
    Unit_Cost DECIMAL(10, 2),
    Unit_Price DECIMAL(10, 2),
    Profit DECIMAL(10, 2),
    Cost DECIMAL(10, 2),
    Revenue DECIMAL(10, 2)
);

-- Question 1: Revenu par catégories
CREATE TABLE category_revenue (
    category_name product_category PRIMARY KEY,
    total_revenue NUMERIC
);

-- Question 2: Revenu par sous-catégories
CREATE TABLE subcategory_revenue (
    subcategory_name sub_category PRIMARY KEY,
    total_revenue NUMERIC
);

-- Question 3: Top des produits
CREATE TABLE top_products (
    product_name VARCHAR(255) PRIMARY KEY,
    total_revenue NUMERIC
);

-- Question 4: Top des produits en France
CREATE TABLE top_products_france (
    product_name VARCHAR(255) PRIMARY KEY,
    total_revenue NUMERIC
);

-- Question 5: Ventes par tranches d'âge
CREATE TABLE age_group_purchases (
    age_group age_group PRIMARY KEY,
    total_purchases INTEGER
);