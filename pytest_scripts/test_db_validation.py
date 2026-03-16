import oracledb

def test_record_count():

    conn = oracledb.connect(
        user="hr",
        password="hr",
        dsn="localhost:1521/orclpdb"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM table1_data")
    source_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM table2_data")
    target_count = cursor.fetchone()[0]

    conn.close()
    ##Just adding for ci validation

    assert source_count == target_count