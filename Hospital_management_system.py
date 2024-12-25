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

        self.Nameoftablet = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.Nooftablet = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.Expdate = StringVar()
        self.Dailydose = StringVar()
        self.Sideffects = StringVar()
        self.Furtherinfo = StringVar()
        self.Storage = StringVar()
        self.Bloodpressure = StringVar()
        self.Medication = StringVar()
        self.Patientid = StringVar()
        self.Nhsno = StringVar()
        self.Patientname = StringVar()
        self.DOB = StringVar()
        self.Patientaddress = StringVar()

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
        comNameTablet = ttk.Combobox(Dataframeleft,font=("arial",12,"bold"),state='readonly',width=33,textvariable=self.Nameoftablet)
        comNameTablet["values"] = ("Nice","Ammarell","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan","Dolo-650","Dolo-325")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref = Label(Dataframeleft,text="Reference no:",font=("arial",12,"bold"),padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(Dataframeleft,font=("arial",12,"bold"),width=35,textvariable=self.Ref)
        txtref.grid(row=1,column=1)

        lblDose = Label(Dataframeleft,text="Dose:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(Dataframeleft,font=("arial",12,"bold"),width=35,textvariable=self.Dose)
        txtDose.grid(row=2,column=1)

        lblNoOfTablets = Label(Dataframeleft,text="No of Tablets:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets = Entry(Dataframeleft,font=("arial",12,"bold"),width=35,textvariable=self.Nooftablet)
        txtNoOfTablets.grid(row=3,column=1)

        lblLot = Label(Dataframeleft,text="Lot:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(Dataframeleft,font=("arial",12,"bold"),width=35,textvariable=self.Lot)
        txtLot.grid(row=4,column=1)

        lblIssueDate = Label(Dataframeleft, text="Issue Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Issuedate)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(Dataframeleft, text="Exp Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Expdate)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(Dataframeleft, text="Daily Dose:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Dailydose)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffects = Label(Dataframeleft, text="Side Effects:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSideEffects.grid(row=8, column=0, sticky=W)
        txtSideEffects = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Sideffects)
        txtSideEffects.grid(row=8, column=1)

        lblFurtherInfo = Label(Dataframeleft, text="Further Info:", font=("arial", 12, "bold"), padx=2)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Furtherinfo)
        txtFurtherInfo.grid(row=0, column=3)

        lblBloodPressure = Label(Dataframeleft, text="Blood Pressure:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Bloodpressure)
        txtBloodPressure.grid(row=1, column=3)

        lblStorageAdvice = Label(Dataframeleft, text="Storage Advice:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblStorageAdvice.grid(row=2, column=2, sticky=W)
        txtStorageAdvice = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Storage)
        txtStorageAdvice.grid(row=2, column=3)

        lblMedication = Label(Dataframeleft, text="Medication:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMedication.grid(row=3, column=2, sticky=W)
        txtMedication = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Medication)
        txtMedication.grid(row=3, column=3)

        lblPatientId = Label(Dataframeleft, text="Patient Id:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Patientid)
        txtPatientId.grid(row=4, column=3)

        lblNHSNumber = Label(Dataframeleft, text="NHS Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNHSNumber.grid(row=5, column=2, sticky=W)
        txtNHSNumber = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Nhsno)
        txtNHSNumber.grid(row=5, column=3)

        lblPatientName = Label(Dataframeleft, text="Patient Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Patientname)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(Dataframeleft, text="Date Of Birth:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.DOB)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(Dataframeleft, text="Patient Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(Dataframeleft, font=("arial", 12, "bold"), width=35,textvariable=self.Patientaddress)
        txtPatientAddress.grid(row=8, column=3)

        # ===================================== Dataframeright ===========================================================

        self.txtPrescription = Text(Dataframeright,font=("arial",12,"bold"),width=50,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        # ======================================= Buttons ================================================================

        btnPrescription = Button(Buttonframe, command=self.iPrescription,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe,command=self.iprescriptionData,text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, command=self.update_data,text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, command=self.iDelete_data,text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, command=self.iClear_data,text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, command=self.iExit,text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
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
        self.Hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ============================================ Functionality Daclaration ========================================

    def iprescriptionData(self):
        if self.Nameoftablet.get()=="" or self.Ref.get()=="":
            messagebox.showerror("Error","All fields are required")

        else:
            connection = mysql.connector.connect(
                host="localhost",  # Replace with your host if needed
                user="root",  # Replace with your MySQL username
                password="26871234",  # Replace with your MySQL password
                database="emp"  # Replace with your database name
            )
            cursor = connection.cursor()
            values = (self.Nameoftablet.get(), self.Ref.get(), self.Dose.get(), self.Nooftablet.get(), self.Lot.get(), self.Issuedate.get(),
                      self.Expdate.get(), self.Dailydose.get(), self.Storage.get(), self.Nhsno.get(), self.Patientname.get(), self.DOB.get(),
                      self.Patientaddress.get())
            cursor.execute("insert into hospital values(%s ,%s, %s ,%s, %s ,%s, %s ,%s, %s ,%s, %s ,%s, %s)",values)
            connection.commit()
            self.fetch_data()
            connection.close()

            messagebox.showinfo("Success","Record has been inserted")

    def update_data(self):
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your host if needed
            user="root",  # Replace with your MySQL username
            password="26871234",  # Replace with your MySQL password
            database="emp"  # Replace with your database name
        )
        cursor = connection.cursor()
        values = (self.Nameoftablet.get(), self.Dose.get(), self.Nooftablet.get(), self.Lot.get(),self.Issuedate.get(),self.Expdate.get(),
                  self.Dailydose.get(), self.Storage.get(), self.Nhsno.get(),self.Patientname.get(), self.DOB.get(),
                  self.Patientaddress.get(), self.Ref.get())
        cursor.execute("update hospital set Nameoftablet=%s, Dose=%s, Nooftablets=%s, Lot=%s, Issuedate=%s, Expdate=%s, Dailydose=%s, Storage=%s, Nhsnumber=%s, Patientname=%s, DOB=%s, Patientaddress=%s where Refno=%s",values)
        connection.commit()
        messagebox.showinfo("Success","Record has been updated Successfully")
        connection.close()


    def fetch_data(self):
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your host if needed
            user="root",  # Replace with your MySQL username
            password="26871234",  # Replace with your MySQL password
            database="emp"  # Replace with your database name
        )
        cursor = connection.cursor()
        cursor.execute("select * from hospital")
        rows = cursor.fetchall()
        if len(rows)!=0:
            self.Hospital_table.delete(*self.Hospital_table.get_children())
            for i in rows:
                self.Hospital_table.insert("",END,values=i)
            connection.commit()
        connection.close()

    def get_cursor(self,event=""):
        cursor_row = self.Hospital_table.focus()
        content = self.Hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablet.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.Nooftablet.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.Expdate.set(row[6])
        self.Dailydose.set(row[7])
        self.Storage.set(row[8])
        self.Nhsno.set(row[9])
        self.Patientname.set(row[10])
        self.DOB.set(row[11])
        self.Patientaddress.set(row[12])

    def iPrescription(self):
        self.txtPrescription.insert(END,"name of tablet:\t\t\t" + self.Nameoftablet.get() + "\n")
        self.txtPrescription.insert(END, "Reference no:\t\t\t" + self.Ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "No of tablet:\t\t\t" + self.Nooftablet.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Exp date:\t\t\t" + self.Expdate.get() + "\n")
        self.txtPrescription.insert(END, "Side effects:\t\t\t" + self.Sideffects.get() + "\n")
        self.txtPrescription.insert(END, "Further Info:\t\t\t" + self.Furtherinfo.get() + "\n")
        self.txtPrescription.insert(END, "Storage Advice:\t\t\t" + self.Storage.get() + "\n")
        self.txtPrescription.insert(END, "Blood pressure:\t\t\t" + self.Bloodpressure.get() + "\n")
        self.txtPrescription.insert(END, "Patient Id:\t\t\t" + self.Patientid.get() + "\n")
        self.txtPrescription.insert(END, "Nhs number:\t\t\t" + self.Nhsno.get() + "\n")
        self.txtPrescription.insert(END, "Patient name:\t\t\t" + self.Patientname.get() + "\n")
        self.txtPrescription.insert(END, "Date Of Birth:\t\t\t" + self.DOB.get() + "\n")
        self.txtPrescription.insert(END, "Patient address:\t\t\t" + self.Patientaddress.get() + "\n")

    def iDelete_data(self):
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your host if needed
            user="root",  # Replace with your MySQL username
            password="26871234",  # Replace with your MySQL password
            database="emp"  # Replace with your database name
        )
        cursor = connection.cursor()
        query = "delete from hospital where Refno=%s"
        values = (self.Ref.get(),)
        cursor.execute(query,values)

        connection.commit()
        connection.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted Successfully")

    def iClear_data(self):
        self.Nameoftablet.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.Nooftablet.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.Dailydose.set("")
        self.Sideffects.set("")
        self.Furtherinfo.set("")
        self.Storage.set("")
        self.Bloodpressure.set("")
        self.Patientid.set("")
        self.Nhsno.set("")
        self.Patientname.set("")
        self.DOB.set("")
        self.Patientaddress.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System","Confirm to Exit")
        if iExit>0:
            root.destroy()
            return


root=Tk()
ob=Hospital(root)
root.mainloop()
