import logging
import logs
from sqlalchemy import text

def execute_procedure(engine, procedure_name):
    try:
        print("\n" + "=" * 80)
        print(f"STARTING PROCEDURE EXECUTION: {procedure_name}")
        print("=" * 80)

        logging.info("=" * 80)
        logging.info(f"STARTING PROCEDURE EXECUTION: {procedure_name}")
        logging.info("=" * 80)

        with engine.begin() as conn:
            print(f"[EXECUTING] EXEC {procedure_name}")
            logging.info(f"[EXECUTING] EXEC {procedure_name}")

            conn.execute(text(f"EXEC {procedure_name}"))

        print(f"[SUCCESS] Procedure '{procedure_name}' executed successfully.\n")
        logging.info(f"[SUCCESS] Procedure '{procedure_name}' executed successfully.")

    except Exception as e:
        print(f"[FAILED] Procedure '{procedure_name}' execution failed.")
        print(f"[ERROR DETAILS] {e}\n")

        logging.exception(f"[FAILED] Procedure '{procedure_name}' execution failed. Error: {e}")