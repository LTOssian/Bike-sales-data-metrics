CREATE TYPE age_group AS ENUM ('Youth (<25)', 'Young Adults (25-34)', 'Adults (35-64)', 'Seniors (65+)');
CREATE TYPE customer_gender AS ENUM ('M', 'F');
CREATE TYPE product_category AS ENUM ('Accessories', 'Bikes');


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
    Sub_Category VARCHAR(100),
    Product VARCHAR(100),
    Order_Quantity INT,
    Unit_Cost DECIMAL(10, 2),
    Unit_Price DECIMAL(10, 2),
    Profit DECIMAL(10, 2),
    Cost DECIMAL(10, 2),
    Revenue DECIMAL(10, 2)
);
