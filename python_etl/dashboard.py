import pandas as pd
import logging

def generate_dashboard(engine):
    try:
        print("=" * 80)
        print("GENERATING EXCEL DASHBOARD")
        print("=" * 80)

        logging.info("=" * 80)
        logging.info("GENERATING EXCEL DASHBOARD")
        logging.info("=" * 80)

        query = """
            SELECT
                YEAR(COALESCE(order_date, '2009-01-01')) AS sales_year,
                SUM(sales_amount) AS total_sales,
                SUM(quantity) AS total_quantity,
                COUNT(DISTINCT order_number) AS total_orders
            FROM gold.fact_sales
            GROUP BY YEAR(COALESCE(order_date, '2009-01-01'))
            ORDER BY sales_year
        """

        output_file = r"C:\Project_2\data_warehouse_project\etl_dashboard.xlsx"

        # Read SQL result into DataFrame
        df = pd.read_sql(query, engine)

        print(f"[LOAD] Creating Excel dashboard file: {output_file}")
        logging.info(f"[LOAD] Creating Excel dashboard file: {output_file}")

        with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:

            # Write data to Excel
            df.to_excel(
                excel_writer=writer,
                sheet_name="report",
                index=False,
                startcol=1
            )

            print("[SUCCESS] Dashboard data written to sheet: report")
            logging.info("[SUCCESS] Dashboard data written to sheet: report")

            # Access workbook and worksheet
            workbook = writer.book
            worksheet = writer.sheets["report"]

            print("[INFO] Workbook and worksheet objects created successfully.")
            logging.info("[INFO] Workbook and worksheet objects created successfully.")

            # Find number of rows
            max_row = len(df)

            # ==================================================
            # Chart 1: Total Sales by Year
            # ==================================================
            print("[CHART] Creating Chart 1: Total Sales by Year ...")
            logging.info("[CHART] Creating Chart 1: Total Sales by Year ...")

            chart_sales = workbook.add_chart({"type": "column"})

            chart_sales.add_series({
                "name": "Total Sales",
                "categories": ["report", 1, 1, max_row, 1],  # sales_year in column B
                "values":     ["report", 1, 2, max_row, 2],  # total_sales in column C
            })

            chart_sales.set_title({"name": "Sales by Year"})
            chart_sales.set_x_axis({"name": "Sales Year"})
            chart_sales.set_y_axis({"name": "Total Sales"})

            worksheet.insert_chart("G2", chart_sales)

            print("[SUCCESS] Chart 1 created successfully")
            logging.info("[SUCCESS] Chart 1 created successfully")

            # ==================================================
            # Chart 2: Total Orders by Year
            # ==================================================
            print("[CHART] Creating Chart 2: Total Orders by Year ...")
            logging.info("[CHART] Creating Chart 2: Total Orders by Year ...")

            chart_orders = workbook.add_chart({"type": "line"})

            chart_orders.add_series({
                "name": "Total Orders",
                "categories": ["report", 1, 1, max_row, 1],  # sales_year in column B
                "values":     ["report", 1, 4, max_row, 4]   # total_orders in column E
            })

            chart_orders.set_title({"name": "Orders Trend"})
            chart_orders.set_x_axis({"name": "Sales Year"})
            chart_orders.set_y_axis({"name": "Total Orders"})

            worksheet.insert_chart("B18", chart_orders)

            print("[SUCCESS] Chart 2 created successfully")
            logging.info("[SUCCESS] Chart 2 created successfully")

            # ==================================================
            # Chart 3: Total Quantity by Year
            # ==================================================
            print("[CHART] Creating Chart 3: Total Quantity by Year ...")
            logging.info("[CHART] Creating Chart 3: Total Quantity by Year ...")

            chart_quantity = workbook.add_chart({"type": "column"})

            chart_quantity.add_series({
                "name": "Total Quantity",
                "categories": ["report", 1, 1, max_row, 1],  # sales_year in column B
                "values":     ["report", 1, 3, max_row, 3],  # total_quantity in column D
            })

            chart_quantity.set_title({"name": "Total Quantity by Year"})
            chart_quantity.set_x_axis({"name": "Sales Year"})
            chart_quantity.set_y_axis({"name": "Total Quantity"})

            worksheet.insert_chart("J18", chart_quantity)

            print("[SUCCESS] Chart 3 created successfully")
            logging.info("[SUCCESS] Chart 3 created successfully")

        print(f"[SUCCESS] Excel dashboard generated successfully: {output_file}")
        logging.info(f"[SUCCESS] Excel dashboard generated successfully: {output_file}")

        print("=" * 80)
        print("DASHBOARD GENERATION COMPLETED")
        print("=" * 80)

        logging.info("=" * 80)
        logging.info("DASHBOARD GENERATION COMPLETED")
        logging.info("=" * 80)

    except Exception as e:
        print(f"[ERROR] Failed to generate Excel dashboard: {e}")
        logging.exception(f"[ERROR] Failed to generate Excel dashboard: {e}")