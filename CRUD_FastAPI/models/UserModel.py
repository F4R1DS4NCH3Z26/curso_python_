# from sqlalchemy import Table, Column, SQ
# from sqlalchemy.sql.sqltypes import Integer, String
# from config.db import engine



# user_model = Table(
#             "user", meta,
#             Column("user_id", Integer, primary_key=True),
#             Column("fullname", String(255)),
#             Column("username", String(255)),
#             Column("password", String(255)),
#             Column("active", Integer, default=1)
#             )

# meta.create_all(engine)