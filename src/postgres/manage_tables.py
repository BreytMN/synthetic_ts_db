def create_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS timeseries (
            id SERIAL PRIMARY KEY, 
            timestamp TIMESTAMP, 
            value FLOAT, 
            data_group VARCHAR(255), 
            data_subgroup VARCHAR(255)
        );
    """)
    conn.commit()
