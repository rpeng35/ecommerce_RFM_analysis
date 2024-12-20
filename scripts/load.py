import mysql.connector
import pandas as pd

# MySQL connection details
db_config = {
    'user': 'root',
    'password': 'rP_0934019769',
    'host': 'localhost',
    'database': 'ecommerce_rfm'
}

# Function to create tables
def create_tables(cursor):
    rfm_table_query = """
    CREATE TABLE IF NOT EXISTS rfm_data (
        customer_id VARCHAR(50),
        Recency INT,
        Frequency INT,
        Monetary FLOAT,
        recency_score INT,
        frequency_score INT,
        monetary_score INT,
        rfm_score INT,
        segment VARCHAR(20)
    );
    """
    combined_table_query = """
    CREATE TABLE IF NOT EXISTS combined (
        order_id VARCHAR(50),
        order_item_id VARCHAR(50),
        product_id VARCHAR(50),
        seller_id VARCHAR(50),
        shipping_limit_date DATETIME,
        price FLOAT,
        freight_value FLOAT,
        customer_id VARCHAR(50),
        order_purchase_timestamp DATETIME
    );
    """
    cursor.execute(rfm_table_query)
    cursor.execute(combined_table_query)
    print("Tables created successfully.")

# Function to insert data from pandas dataframe to MySQL table
def insert_data_from_dataframe(cursor, table_name, dataframe):
    for i, row in dataframe.iterrows():
        columns = ', '.join(dataframe.columns)
        values_placeholder = ', '.join(['%s'] * len(row))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_placeholder})"
        cursor.execute(insert_query, tuple(row))
    conn.commit()
    print(f"Data inserted into {table_name} successfully.")

# Main script
try:
    # Establish connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create tables
    create_tables(cursor)

    # Load data from CSVs
    rfm_data = pd.read_csv('./scripts/rfm_metrics.csv')
    combined_data = pd.read_csv('./scripts/combined_cleaned.csv')

    # Insert data into MySQL tables
    insert_data_from_dataframe(cursor, 'rfm_data', rfm_data)
    insert_data_from_dataframe(cursor, 'combined', combined_data)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    conn.close()

