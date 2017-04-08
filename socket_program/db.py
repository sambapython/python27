

import psycopg2


def connect():
	con = psycopg2.connect(host="localhost",port=5432,database="db1",user="postgres",
					  password="root")
	cur = con.cursor()
	return con,cur



def browse(cust_id):
	con,cur = connect()
	cur.execute("select * from customer where id={0}".format(cust_id))
	data = cur.fetchall()
	return data
def main():
	pass
if __name__ == "__main__":
	main()

#print browse(200)