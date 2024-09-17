import customtkinter as ctk
import tkinter as tk
from tkinter import *
from call_linear_function import LinearRegression

ctk.set_appearance_mode("Light") 
ctk.set_default_color_theme("blue") 

appWidth, appHeight = 600, 1500

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1, uniform="fred")
        self.grid_columnconfigure(1, weight=1, uniform="fred")
        self.grid_columnconfigure(2, weight=1, uniform="fred")
        self.grid_columnconfigure(3, weight=1, uniform="fred")
        furnishvalues=["Chưa có nội thất","Nội thất cơ bản","Nội Thất đầy đủ"]
        furnish_var=tk.StringVar(self,"Chưa có nội thất")
        area_var=tk.StringVar(self,"0")
        bed_var=tk.StringVar(self, "0")
        bath_var=tk.StringVar(self,"0")
        wm_var=tk.StringVar(self,"0")
        hw_var=tk.StringVar(self,"0")
        ac_var=tk.StringVar(self,"0")
        pk_var=tk.StringVar(self,"0")
        se_var=tk.StringVar(self,"0")
        cen_var=tk.StringVar(self,"0")
        reg=LinearRegression
        def submit():
                area=float(area_var.get())
                bed =int(bed_var.get())
                bath=int(bath_var.get())
                wm=int(wm_var.get())
                hw=int(hw_var.get())
                ac=int(ac_var.get())
                pk=int(pk_var.get())
                se=int(se_var.get())
                dtcen=float(cen_var.get())
                furnish=furnish_var.get()
                fn=furnishvalues.index(furnish)
                price=reg.predict(area, bed, bath, wm, dtcen, hw, ac, pk, se,fn)
                
                print("Floor area: ", area)
                print("Number of Bedroom: ", bed)
                print("Number of Bathroom: ", bath)
                print("Washing machine: ", wm)
                print("Furnishment level: ", fn)
                print("Hot water: ", hw)
                print("AC: ", ac)
                print("Parking: ", pk)
                print("Security: ", se)
                print("Predicted price: ", price)
                
                # Output
                self.outputlabel = ctk.CTkLabel(self, text="Giá Trọ Dự Đoán")
                self.outputlabel.grid(row=12, column=1, padx=20, pady=15, sticky="ew")
                self.price = ctk.CTkLabel(self, text=f'{price:,}'+' Đồng')
                self.price.grid(row=12, column=2, padx=20, pady=15, sticky="ew")
                
# App title
        self.title("Ứng Dụng Dự Đoán Giá Nhà Trọ")
        self.geometry(f"{appWidth}x{appHeight}")
        
# Title Label
        self.label = ctk.CTkLabel(self, text="DỰ ĐOÁN GIÁ TRỌ", font=ctk.CTkFont(size=30, weight="bold"))
        self.label.grid(row=0,column=0, columnspan=4, padx=50, pady=30,sticky='ew')

# area
        self.areaLabel = ctk.CTkLabel(self,text="Diện Tích Sàn (m\u00b2)")
        self.areaLabel.grid(row=1, column=0, padx=20, pady=15, sticky="ew")
        self.areaEntry = ctk.CTkEntry(self, placeholder_text="60 (m^2)",textvariable = area_var)
        self.areaEntry.grid(row=1, column=1, columnspan=2, padx=20, pady=15, sticky="ew")

# Bedroom Label
        self.BedroomLabel = ctk.CTkLabel(self, text="Số Phòng Ngủ")
        self.BedroomLabel.grid(row=2, column=0, padx=20, pady=15, sticky="ew")
        self.BedroomMenu = ctk.CTkOptionMenu(self,values=["1","2","3"], variable=bed_var)
        self.BedroomMenu.grid(row=2, column=1, padx=20, pady=15, columnspan=2, sticky="ew")
        
# Bathroom Label
        self.BathroomLabel = ctk.CTkLabel(self, text="Số Phòng Tắm")
        self.BathroomLabel.grid(row=3, column=0, padx=20, pady=15, 
                                sticky="ew")
        self.BathroomMenu = ctk.CTkOptionMenu(self,values=["0","1","2","3"], 
                                              variable=bath_var)
        self.BathroomMenu.grid(row=3, column=1, padx=20, pady=15, 
                               columnspan=2, sticky="ew")
# Furnishing Label
        self.FurnishLabel = ctk.CTkLabel(self, text="Nội Thất")
        self.FurnishLabel.grid(row=4, column=0, padx=20, pady=15, 
                               sticky="ew")
        self.FurnishMenu = ctk.CTkOptionMenu(self,values=furnishvalues, 
                                             variable=furnish_var)
        self.FurnishMenu.grid(row=4, column=1, padx=20, pady=15,
                                    columnspan=2, sticky="ew")
        

# Utilities Label
        self.choiceLabel = ctk.CTkLabel(self, text="Tiện Nghi")
        self.choiceLabel.grid(row=5, column=0, padx=20, pady=15, 
                              sticky="ew")

# Utility chekcbox
        #row 5
        self.wmchoice = ctk.CTkCheckBox(self, text="Máy giặt", 
                                        variable=wm_var, onvalue="1", offvalue="0")
        self.wmchoice.grid(row=5, column=1, padx=20, pady=15, 
                           sticky="ew")

        self.hwchoice = ctk.CTkCheckBox(self, text="Nước nóng", 
                                        variable=hw_var, onvalue="1", offvalue="0")							 
        self.hwchoice.grid(row=5, column=2, padx=20, pady=15, 
                           sticky="ew")
        
        #row 6
        self.acchoice = ctk.CTkCheckBox(self, text="Điều hoà", 
                                        variable=ac_var, onvalue="1", offvalue="0")
        self.acchoice.grid(row=6, column=1, padx=20, pady=15, 
                           sticky="ew")

        self.pkchoice = ctk.CTkCheckBox(self, text="Bãi giữ xe", 
                                        variable=pk_var, onvalue="1", offvalue="0")							 
        self.pkchoice.grid(row=6, column=2, padx=20, pady=15, 
                           sticky="ew")
        
        #row 7
        self.sechoice = ctk.CTkCheckBox(self, text="Bảo vệ", 
                                        variable=se_var, onvalue="1", offvalue="0")
        self.sechoice.grid(row=7, column=1, padx=20, pady=15, 
                           sticky="ew")
# Utilities Label
        self.choiceLabel = ctk.CTkLabel(self, text="Khoản cách (km)")
        self.choiceLabel.grid(row=8, column=0, padx=20, pady=15, 
                              sticky="ew")
# Distance Entry
        #row 8
        self.areaLabel = ctk.CTkLabel(self,text="Khu trung tâm")
        self.areaLabel.grid(row=8, column=1, padx=20, pady=15, sticky="ew")
        self.areaEntry = ctk.CTkEntry(self, placeholder_text="2 (km)",textvariable = cen_var)
        self.areaEntry.grid(row=8, column=2, columnspan=1, padx=20, pady=15, sticky="ew")
        
# Generate Button
        self.generateResultsButton = ctk.CTkButton(self, text="Generate Results", command = submit)s
        self.generateResultsButton.grid(row=11, column=1, columnspan=2,
                                        padx=20, pady=15, sticky="ew")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
