import sqlite3

def get_results_from_db():
    conn = sqlite3.connect('running_data.db')
    c = conn.cursor()
    c.execute("SELECT result FROM running_data")
    results = c.fetchall()
    conn.close()
    return results

# 결과 출력
results = get_results_from_db()
for result in results:
    print(result[0])