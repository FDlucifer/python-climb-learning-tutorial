import os
import win32com.client as win32

excel = win32.Dispatch("Excel.Application")
excel.Visible = True

workbook = excel.Workbooks.Add()
workbook.SaveAs(os.path.join(os.getcwd(), "myfile.xlsx"))

sheet1 = workbook.Worksheets("Sheet1")
sheet1.name = "Todo List"
sheet1.Range("A:D").ColumnWidth = 30

cells = sheet1.Cells

cells(1, "A").Value = "Task"
cells(1, "A").Font.Bold = True
cells(1, "B").Value = "Description"
cells(1, "B").Font.Bold = True
cells(1, "C").Value = "Done"
cells(1, "C").Font.Bold = True
cells(1, "D").Value = "Time Needed"
cells(1, "D").Font.Bold = True

cells(2, "A").Value = "Dinner"
cells(2, "B").Value = "Cook Dinner"
cells(2, "C").Value = ""
cells(2, "D").Value = "40"

cells(3, "A").Value = "Clean Room"
cells(3, "B").Value = "Clean my room"
cells(3, "C").Value = "X"
cells(3, "D").Value = "20"

cells(4, "A").Value = "Workout"
cells(4, "B").Value = "go to the gym"
cells(4, "C").Value = ""
cells(4, "D").Value = "120"

cells(5, "D").Value = "=SUM(D2:D4)"

ch = sheet1.Shapes.AddChart().Select()

excel.ActiveChart.SetSourceData(Source=sheet1.Range("D2:D4"), PlotBy=2)
excel.ActiveChart.ChartType = 63

workbook.SaveAs(os.path.join(os.getcwd(), "myfile.xlsx"))

