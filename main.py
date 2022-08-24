# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import psycopg2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    conn = psycopg2.connect(database="Crawler", user="postgres", password="DeepseaBus@1992", host="localhost",
                            port="5432")
    cur1 = conn.cursor()
    sql = '''
    SELECT id, "PriceDate", "Type", "Price", "IsActive", "CreateDate"
	FROM public."OilPrice";
    '''

    cur1.execute(sql)
    data = cur1.fetchall()
    print(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
