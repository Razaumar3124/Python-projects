from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root                          #here windows name will be generating
        self.root.title("Hospital Management System")       #here we will be giving the title
        self.root.geometry("1520x800+0+0")                       #0+0 are given for the windows x axis and y axis

        lbl_title = Label(self.root,bd=20,relief="ridge",text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold")) #here the title or the header is created and css is also provided
        lbl_title.pack(side=TOP,fill="x")           #here we are aligning the title

        # **************************************** Dataframe *******************************************

        Dataframe = Frame(self.root,bd=20,relief="ridge")
        Dataframe.place(x=0,y=130,width=1536,height=400)

        Dataframeleft = LabelFrame(Dataframe,bd=10,relief="ridge",padx=20,
                                            font=("arial",12,"bold"),text="Patient Information")    #here we are create frame inside another frame which is Patient Information box
        Dataframeleft.place(x=5,y=5,width=980,height=350)       #here we are placing the Patient Information box

        Dataframeright = LabelFrame(Dataframe,bd=10,relief="ridge",padx=20,
                                        font=("arial",12,"bold"),text="Prescription")       #here we are create frame inside another frame which is Prescription box
        Dataframeright.place(x=990,y=5,width=500,height=350)        #here we are placing the Prescription box

        # *********************************************** Buttons frame ***********************************************************

        Buttonframe = Frame(self.root,bd=20,relief="ridge")
        Buttonframe.place(x=0,y=530,width=1536,height=70)

        # *********************************************** Details frame ***********************************************************

        Deatilsframe = Frame(self.root,bd=20,relief="ridge")
        Deatilsframe.place(x=0,y=600,width=1536,height=190)

        # ============================================== Dataframeleft =============================================================

        lblNameTablet = Label(Dataframeleft,text="Names of Tablet:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        self.comNameTablet = ttk.Combobox(Dataframeleft,font=("arial",12,"bold"),state='readonly',width=33)
        self.comNameTablet["values"] = ("Nice","Ammarell","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan","Dolo-650","Dolo-325")
        self.comNameTablet.current(0)
        self.comNameTablet.grid(row=0,column=1)

        lblref = Label(Dataframeleft,text="Reference no:",font=("arial",12,"bold"),padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        self.txtref = Entry(Dataframeleft,font=("arial",12,"bold"),width=35)
        self.txtref.grid(row=1,column=1)

        lblDose = Label(Dataframeleft,text="Dose:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        self.txtDose = Entry(Dataframeleft,font=("arial",12,"bold"),width=35)
        self.txtDose.grid(row=2,column=1)

        lblNoOfTablets = Label(Dataframeleft,text="No of Tablets:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        self.txtNoOfTablets = Entry(Dataframeleft,font=("arial",12,"bold"),width=35)
        self.txtNoOfTablets.grid(row=3,column=1)

        lblLot = Label(Dataframeleft,text="Lot:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        self.txtLot = Entry(Dataframeleft,font=("arial",12,"bold"),width=35)
        self.txtLot.grid(row=4,column=1)

        lblIssueDate = Label(Dataframeleft, text="Issue Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        self.txtIssueDate = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        self.txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(Dataframeleft, text="Exp Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        self.txtExpDate = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        self.txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(Dataframeleft, text="Daily Dose:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        self.txtDailyDose = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        self.txtDailyDose.grid(row=7, column=1)

        lblSideEffects = Label(Dataframeleft, text="Side Effects:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSideEffects.grid(row=8, column=0, sticky=W)
        txtSideEffects = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        txtSideEffects.grid(row=8, column=1)

        lblFurtherInfo = Label(Dataframeleft, text="Further Info:", font=("arial", 12, "bold"), padx=2)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        txtFurtherInfo.grid(row=0, column=3)

        lblBloodPressure = Label(Dataframeleft, text="Blood Pressure:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorageAdvice = Label(Dataframeleft, text="Storage Advice:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblStorageAdvice.grid(row=2, column=2, sticky=W)
        self.txtStorageAdvice = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        self.txtStorageAdvice.grid(row=2, column=3)

        lblMedication = Label(Dataframeleft, text="Medication:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMedication.grid(row=3, column=2, sticky=W)
        txtMedication = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        txtMedication.grid(row=3, column=3)

        lblPatientId = Label(Dataframeleft, text="Patient Id:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        txtPatientId.grid(row=4, column=3)

        lblNHSNumber = Label(Dataframeleft, text="NHS Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNHSNumber.grid(row=5, column=2, sticky=W)
        self.txtNHSNumber = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        self.txtNHSNumber.grid(row=5, column=3)

        lblPatientName = Label(Dataframeleft, text="Patient Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        self.txtPatientName = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        self.txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(Dataframeleft, text="Date Of Birth:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        self.txtDateOfBirth = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        self.txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(Dataframeleft, text="Patient Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        self.txtPatientAddress = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35)
        self.txtPatientAddress.grid(row=8, column=3)

        # ===================================== Dataframeright ===========================================================

        self.txtPrescription = Text(Dataframeright,font=("arial",12,"bold"),width=50,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        # ======================================= Buttons ================================================================

        btnPrescription = Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe,command=self.store_details,text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnExit.grid(row=0, column=5)

        # ============================================ Table =======================================================
        # ================================= Scrollbar ==============================================================

        scrollbar_x = Scrollbar(Deatilsframe,orient=HORIZONTAL)
        scrollbar_y = Scrollbar(Deatilsframe, orient=VERTICAL)
        self.Hospital_table = ttk.Treeview(Deatilsframe,columns=("NameOfTablet","Ref","Dose","NoOfTablets","Lot","IssueDate","ExpDate",
                                                                 "DailyDose","Storage","NHSNumber","Pname","DOB","Address"),xscrollcommand=scrollbar_x.set,yscrollcommand=scrollbar_y)
        scrollbar_x.pack(side=BOTTOM,fill=X)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        scrollbar_x = Scrollbar(command=self.Hospital_table.xview)
        scrollbar_y = Scrollbar(command=self.Hospital_table.yview)

        self.Hospital_table.heading("NameOfTablet",text="Name Of Tablets")
        self.Hospital_table.heading("Ref", text="Reference")
        self.Hospital_table.heading("Dose", text="Dose")
        self.Hospital_table.heading("NoOfTablets", text="No Of Tablets")
        self.Hospital_table.heading("Lot", text="Lot")
        self.Hospital_table.heading("IssueDate", text="Issue Date")
        self.Hospital_table.heading("ExpDate", text="Expire Date")
        self.Hospital_table.heading("DailyDose", text="Daily Dose")
        self.Hospital_table.heading("Storage", text="Storage")
        self.Hospital_table.heading("NHSNumber", text="NHS Number")
        self.Hospital_table.heading("Pname", text="Patient Name")
        self.Hospital_table.heading("DOB", text="Date Of Birth")
        self.Hospital_table.heading("Address", text="Address")

        self.Hospital_table["show"]="headings"

        self.Hospital_table.pack(fill=BOTH,expand=1)

        self.Hospital_table.column("NameOfTablet",width=100)
        self.Hospital_table.column("Ref", width=100)
        self.Hospital_table.column("Dose", width=100)
        self.Hospital_table.column("NoOfTablets", width=100)
        self.Hospital_table.column("Lot", width=100)
        self.Hospital_table.column("IssueDate", width=100)
        self.Hospital_table.column("ExpDate", width=100)
        self.Hospital_table.column("DailyDose", width=100)
        self.Hospital_table.column("Storage", width=100)
        self.Hospital_table.column("NHSNumber", width=100)
        self.Hospital_table.column("Pname", width=100)
        self.Hospital_table.column("DOB", width=100)
        self.Hospital_table.column("Address", width=100)

        self.Hospital_table.pack(fill=BOTH,expand=1)
        self.fetch_data()


    # ================================== Functionality Declaration ================================================

    def store_details(self):
        nameoftablet = self.comNameTablet.get()
        Ref = self.txtref.get()
        Dose = self.txtDose.get()
        Nooftablets = self.txtNoOfTablets.get()
        Lot = self.txtLot.get()
        Issuedate = self.txtIssueDate.get()
        Expdate = self.txtExpDate.get()
        Dailydose = self.txtDailyDose.get()
        Storage = self.txtStorageAdvice.get()
        Nhsno = self.txtNHSNumber.get()
        Pname = self.txtPatientName.get()
        DOB = self.txtDateOfBirth.get()
        Address = self.txtPatientAddress.get()

        if nameoftablet and Ref and Dose and Nooftablets and Lot and Issuedate and Expdate and Dailydose and Storage and Nhsno and Pname and DOB and Address:
            try:
                # Connect to MySQL database
                connection = mysql.connector.connect(
                    host="localhost",  # Replace with your host if needed
                    user="root",  # Replace with your MySQL username
                    password="26871234",  # Replace with your MySQL password
                    database="emp"  # Replace with your database name
                )
                cursor = connection.cursor()

                # Insert data into the details table
                query = "INSERT INTO hospital(Nameoftablet,Refno,Dose,Nooftablets,Lot,Issuedate,Expdate,Dailydose,Storage,Nhsnumber,Patientname,DOB,Patientaddress) VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s, %s)"
                values = (nameoftablet,Ref,Dose,Nooftablets,Lot,Issuedate,Expdate,Dailydose,Storage,Nhsno,Pname,DOB,Address)
                cursor.execute(query, values)
                connection.commit()
                self.fetch_data()

                # Show success message
                messagebox.showinfo("Success", "Details stored successfully!")

                # Clear the fields
                self.comNameTablet.delete(0, END)
                self.txtref.delete(0, END)
                self.txtDose.delete(0, END)
                self.txtNoOfTablets.delete(0, END)
                self.txtLot.delete(0, END)
                self.txtIssueDate.delete(0, END)
                self.txtExpDate.delete(0, END)
                self.txtDailyDose.delete(0, END)
                self.txtStorageAdvice.delete(0, END)
                self.txtNHSNumber.delete(0, END)
                self.txtPatientName.delete(0, END)
                self.txtDateOfBirth.delete(0, END)
                self.txtPatientAddress.delete(0, END)


            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}")

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        else:
            messagebox.showwarning("Warning", "All fields are required!")
    def fetch_data(self):
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your host if needed
            user="root",  # Replace with your MySQL username
            password="26871234",  # Replace with your MySQL password
            database="emp"  # Replace with your database name
        )
        cursor = connection.cursor()
        query = "select * from hospital"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows)!=0:
            self.Hospital_table.delete(*self.Hospital_table.get_children())
            for i in rows:
                self.Hospital_table.insert("",END,values=i)
            connection.commit()
        connection.close()

    def get_cursor(self):
        cursor_row = self.Hospital_table.focus()
        content = self.Hospital_table.item(cursor_row)
        row = content["values"]







root=Tk()
ob=Hospital(root)
root.mainloop()
