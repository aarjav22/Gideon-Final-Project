from db_connection import *
api='gideon_v2.0_259634'

test = dataLink(api)
test.uploadDht(23)
print(test.fetchMotor())
