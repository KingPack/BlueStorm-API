import sqlite3

from pharmacies.pharmacies.models.core import PatientsModel



DATABASE_LOCAL = "/home/hendrek/Documents/github/kingpack/api/pharmacies/pharmacies/ext/backend_test.db"
connect_db = sqlite3.connect(DATABASE_LOCAL)

cur = connect_db.cursor()


query_patients = cur.execute("SELECT UUID, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH FROM PATIENTS;")


patients = query_patients.fetchall()

for patient in patients:
    print(patient)

    # insert_patients = PatientsModel(
    #                     UUID=patient[0],
    #                     FIRST_NAME=patient[1],
    #                     LAST_NAME=patient[2],
    #                     DATE_OF_BIRTH=patient[3]
    #                     )

    # print(insert_patients)