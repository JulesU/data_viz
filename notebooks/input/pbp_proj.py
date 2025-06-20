# import additional xlwing packages

from xlwings import Workbook, Range

# define my function

def summarize_sales():
    """
    Retrieve the pizza type and date ranges from the Excel sheet
    """
    # Make a connection to the calling Excel file
    wb = Workbook.caller()

    # Connect to sqlite db
    filename= 'pizza2.db'
    #pathlib.Path(mydir) / myfile
    #from pathlib import Path
    os = 'C:/Users/jurbano/data_viz/notebooks/input'
    db_file = Path.cwd().joinpath(os).joinpath(filename)
    engine = create_engine(r"sqlite:///{}".format(db_file))

    # Retrieve the fund and account numbers along with dates - check cells correspond to correct location of entry
    #fund = Range('B3').value
    type = Range('D3').value
    start_date = Range('F3').value
    end_date = Range('H3').value

    # Output the data with default values to confirm my code is working
    #Range('A4').value = fund
    Range('A5').value = type
    Range('A6').value = start_date
    Range('A7').value = end_date

    # If retrieving a number from the excel sheet as an int
    # id = Range('B2').options(numbers=int).value
    # Get our pizza type - maybe make this a drop down in the future??
    type = Range('B2').value

    # Get our dates - in real life would need to do some error checking to ensure
    # the correct format
    start_date = Range('D2').value
    end_date = Range('F2').value

    # Clear existing data
    Range('A5:F100').clear_contents()

    # Create SQL query
    sql = 'SELECT * from pizzaplace2 WHERE type="{}" AND date BETWEEN "{}" AND "{}"'.format(type, start_date, end_date)

    # Read query directly into a dataframe
    sales_data = pd.read_sql(sql, engine)

    # Analyze the data however we want
    summary = sales_data.groupby(["type"])["price"].sum()
    total_sales = sales_data["price"].sum()

    # Output the results
    if summary.empty:
        Range('A5').value = "No Data for pizza type {}".format(type)
    else:
        Range('A5').options(index=True).value = summary
        Range('E5').value = "Total Sales"
        Range('F5').value = total_sales