from tkinter import *
from tkinter import messagebox
import os
import random


class Bill_App:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1350x710+0+0")
        self.root.title("Billing software")
        bg_color = "#badc57"
        Label(
            self.root,
            text="Billing software",
            font=("times new roman", 30, "bold"),
            pady=2,
            bg=bg_color,
            bd=12,
            fg="Black",
            relief=RIDGE,
        ).pack(fill=X)
        # ===========medical==========
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.newsprin = IntVar()
        self.thermal_gun = IntVar()
        # ============grocery==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        # =============coldDrinks=============================
        self.sprite = IntVar()
        self.limka = IntVar()
        self.mazza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_duo = IntVar()
        # ==============Total product price================
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
        # ===============Tax================================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
        # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text='Customer Name:',bg=bg_color, font=('times new roman', 15, 'bold' ))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_text = Entry(F1, width=15,font='arial 15', textvariable=self.c_name,  relief=GROOVE, bd=7)
        cname_text.grid(row=0, column=1, padx=10, pady=5 )

        cphn_lbl = Label(F1,text='Customer Phone:', bg=bg_color,font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, textvariable=self.c_phone, font='arial 15', width=15, relief=GROOVE, bd=7 )
        cphn_txt.grid(row=0, column=3,padx=10, pady=5)

        c_bill_lbl = Label(F1, text='Bill Number :', bg=bg_color, font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_text = Entry(F1, width=15, bd=7, textvariable=self.search_bill, font='arial 15', relief=GROOVE)
        c_bill_text.grid(row=0, column=5, padx=25, pady=5)

        bil_btn = Button(F1, text='Search', command=self.find_bill, width=10, bd=7,font=('arial', 12, 'bold'), relief=GROOVE )
        bil_btn.grid(row=0, column=6, padx=10, pady=5)

        #===============custom frome====================
        container_frame = Frame(self.root)
        container_frame.place(x=0, y=170, relwidth=1, height=380)
        container_frame.grid_columnconfigure((0,1,2,3), weight=1, uniform='equal')
        container_frame.grid_rowconfigure(0, weight=1)

        #===============medical============
        F2 = LabelFrame(container_frame, text='Medical Purpose', font=('times new roman',15, 'bold'), bg=bg_color, bd=10, fg='Black', width=200)
        F2.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        F2.grid_columnconfigure(1, weight=1)

        sanitizer_lbl = Label(F2, text='Sanitizer', bg=bg_color, font=('times new roman', 16, 'bold'), fg='Black')
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
        sanitizer_txt = Entry(F2, width=10, bd=5, relief=GROOVE, textvariable=self.sanitizer, font=('times new roman', 16, 'bold'))
        sanitizer_txt.grid(row=0, column=1, padx=20 ,sticky='e')

        mask_lbl = Label(F2, text='Mask', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='nw')
        mask_txt = Entry(F2, width=10, bd=5, relief=GROOVE, textvariable=self.mask, font=('times new roman', 16, 'bold'))
        mask_txt.grid(row=1, column=1, sticky='e', padx=20)

        hand_gloves_lbl = Label(F2, text='Hand Gloves', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='nw')
        hand_gloves_txt = Entry(F2, width=10, bd=5, relief=GROOVE, textvariable=self.hand_gloves, font=('times new roman', 16, 'bold'))
        hand_gloves_txt.grid(row=2, column=1, sticky='e', padx=20)

        dettol_lbl = Label(F2, text='Dettol', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        dettol_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='nw')
        dettol_txt = Entry(F2, width=10, bd=5, relief=GROOVE, textvariable=self.dettol, font=('times new roman', 16, 'bold'))
        dettol_txt.grid(row=3, column=1, sticky='e', padx=20)

        newsprin_lbl = Label(F2, text='Newsprin', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        newsprin_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='nw')
        newsprin_txt = Entry(F2, width=10, bd=5, relief=GROOVE, textvariable=self.newsprin, font=('times new roman', 16, 'bold'))
        newsprin_txt.grid(row=4, column=1, sticky='e', padx=20)

        thermal_gun_lbl = Label(F2, text='Thermal Gun', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        thermal_gun_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='nw')
        thermal_gun_txt = Entry(F2, width=10, bd=5, relief=GROOVE, textvariable=self.thermal_gun, font=('times new roman', 16, 'bold'))
        thermal_gun_txt.grid(row=5, column=1, sticky='e', padx=20)

        #==============grocery=============
        F3 = LabelFrame(container_frame, text='Grocery Items', font=('times new roman',15, 'bold'), bg=bg_color, bd=10, fg='Black', width=200)
        F3.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        F3.grid_columnconfigure(1, weight=1)

        rice_lbl = Label(F3, text='Rice', bg=bg_color, font=('times new roman', 16, 'bold'), fg='Black')
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
        rice_txt = Entry(F3, width=10, bd=5, relief=GROOVE, textvariable=self.rice, font=('times new roman', 16, 'bold'))
        rice_txt.grid(row=0, column=1, padx=20 ,sticky='e')

        food_oil_lbl = Label(F3, text='Food Oil', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='nw')
        food_oil_txt = Entry(F3, width=10, bd=5, relief=GROOVE, textvariable=self.food_oil, font=('times new roman', 16, 'bold'))
        food_oil_txt.grid(row=1, column=1, sticky='e', padx=20)

        wheat_lbl = Label(F3, text='Wheat', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='nw')
        wheat_txt = Entry(F3, width=10, bd=5, relief=GROOVE, textvariable=self.wheat, font=('times new roman', 16, 'bold'))
        wheat_txt.grid(row=2, column=1, sticky='e', padx=20)

        daal_lbl = Label(F3, text='Daal', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        daal_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='nw')
        daal_txt = Entry(F3, width=10, bd=5, relief=GROOVE, textvariable=self.daal, font=('times new roman', 16, 'bold'))
        daal_txt.grid(row=3, column=1, sticky='e', padx=20)

        flour_lbl = Label(F3, text='Flour', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        flour_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='nw')
        flour_txt = Entry(F3, width=10, bd=5, relief=GROOVE, textvariable=self.flour, font=('times new roman', 16, 'bold'))
        flour_txt.grid(row=4, column=1, sticky='e', padx=20)

        maggi_lbl = Label(F3, text='Maggi', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        maggi_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='nw')
        maggi_txt = Entry(F3, width=10, bd=5, relief=GROOVE, textvariable=self.maggi, font=('times new roman', 16, 'bold'))
        maggi_txt.grid(row=5, column=1, sticky='e', padx=20)

        #=========cold drinks=================

        F4 = LabelFrame(container_frame, text='Medical Purpose', font=('times new roman',15, 'bold'), bg=bg_color, bd=10, fg='Black', width=200)
        F4.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
        F4.grid_columnconfigure(1, weight=1)

        sprite_lbl = Label(F4, text='Sprite', bg=bg_color, font=('times new roman', 16, 'bold'), fg='Black')
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
        sprite_txt = Entry(F4, width=10, bd=5, relief=GROOVE, textvariable=self.sprite, font=('times new roman', 16, 'bold'))
        sprite_txt.grid(row=0, column=1, padx=20 ,sticky='e')

        limka_lbl = Label(F4, text='Limka', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        limka_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='nw')
        limka_txt = Entry(F4, width=10, bd=5, relief=GROOVE, textvariable=self.limka, font=('times new roman', 16, 'bold'))
        limka_txt.grid(row=1, column=1, sticky='e', padx=20)

        mazza_lbl = Label(F4, text='Mazza', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        mazza_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='nw')
        mazza_txt = Entry(F4, width=10, bd=5, relief=GROOVE, textvariable=self.mazza, font=('times new roman', 16, 'bold'))
        mazza_txt.grid(row=2, column=1, sticky='e', padx=20)

        coke_lbl = Label(F4, text='Coke', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='nw')
        coke_txt = Entry(F4, width=10, bd=5, relief=GROOVE, textvariable=self.coke, font=('times new roman', 16, 'bold'))
        coke_txt.grid(row=3, column=1, sticky='e', padx=20)

        fanta_lbl = Label(F4, text='Fanta', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        fanta_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='nw')
        fanta_txt = Entry(F4, width=10, bd=5, relief=GROOVE, textvariable=self.fanta, font=('times new roman', 16, 'bold'))
        fanta_txt.grid(row=4, column=1, sticky='e', padx=20)

        mountain_duo_lbl = Label(F4, text='Mountain Duo', bg=bg_color, fg='Black', font=('times new roman', 16, 'bold'))
        mountain_duo_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='nw')
        mountain_duo_txt = Entry(F4, width=10, bd=5, relief=GROOVE, textvariable=self.mountain_duo, font=('times new roman', 16, 'bold'))
        mountain_duo_txt.grid(row=5, column=1, sticky='e', padx=20)

        # =================BillArea======================
        F5 = Frame(container_frame, bd=5, relief=GROOVE)
        F5.grid(row=0, column=3, padx=10, pady=10, sticky='nsew')

        bill_title = Label(F5, text='Bill Area', bd=7, relief=GROOVE, font=('arial', 15, 'bold'))
        bill_title.pack(fill=X)
        
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        self.txtarea.configure(tabs=('60',))  # Customize tab width
        self.txtarea.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txtarea.yview)

        # =======================BillFrame=============
        F6 = LabelFrame(self.root, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, bg=bg_color, fg='black')
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text='Total Medical Price', font=('times new roman', 14, 'bold'), bg=bg_color, fg='black')
        m1_lbl.grid(row=0, column=0, padx=17, pady=1, sticky='W')
        m1_txt = Entry(F6, textvariable=self.medical_price, font=('arial', 10, 'bold'), bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=15, pady=1)

        m2_lbl = Label(F6, text='Total Grocery Price', font=('times new roman', 14, 'bold'), bg=bg_color, fg='black')
        m2_lbl.grid(row=1, column=0, padx=17, pady=1, sticky='W')
        m2_txt = Entry(F6, textvariable=self.grocery_price, font=('arial', 10, 'bold'), bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=15, pady=1)

        m3_lbl = Label(F6, text='Total Cold Drinks Price', font=('times new roman', 14, 'bold'), bg=bg_color, fg='black')
        m3_lbl.grid(row=2, column=0, padx=17, pady=1, sticky='W')
        m3_txt = Entry(F6, textvariable=self.cold_drinks_price, font=('arial', 10, 'bold'), bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=15, pady=1)

        m4_lbl = Label(F6, text='Medical Tax', font=('times new roman', 14, 'bold'), bg=bg_color, fg='black')
        m4_lbl.grid(row=0, column=2, padx=17, pady=1, sticky='W')
        m4_txt = Entry(F6, textvariable=self.medical_tax, font=('arial', 10, 'bold'), bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=15, pady=1)

        m5_lbl = Label(F6, text='Grocery Tax', font=('times new roman', 14, 'bold'), bg=bg_color, fg='black')
        m5_lbl.grid(row=1, column=2, padx=17, pady=1, sticky='W')
        m5_txt = Entry(F6, textvariable=self.grocery_tax, font=('arial', 10, 'bold'), bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=15, pady=1)

        m6_lbl = Label(F6, text='Cold Drinks Tax', font=('times new roman', 14, 'bold'), bg=bg_color, fg='black')
        m6_lbl.grid(row=2, column=2, padx=17, pady=1, sticky='W')
        m6_txt = Entry(F6, textvariable=self.cold_drinks_tax, font=('arial', 10, 'bold'), bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=15, pady=1)

        # =======================ButtonFrame=============
        F7 = Frame(F6, bd=7, relief=GROOVE, bg='white')
        F7.place(height=102, width=548, x=780)

        total_btn = Button(F7, text='Total', fg='white',  bg='#535C68', bd=2, command=self.total, font=('arial', 13, 'bold'), width=11, height=3)
        total_btn.grid(row=0, column=0, padx=6, pady=7)

        generate_bill_btn = Button(F7, text='Generate Bill', fg='white',  bg='#535C68', bd=2, command=self.bill_area, font=('arial', 13, 'bold'), width=11, height=3)
        generate_bill_btn.grid(row=0, column=1, padx=6, pady=7)

        clear_btn = Button(F7, text='Clear', fg='white',  bg='#535C68', bd=2, command=self.clear_data, font=('arial', 13, 'bold'), width=11, height=3)
        clear_btn.grid(row=0, column=2, padx=6, pady=7)

        exit_btn = Button(F7, text='Exit', fg='white',  bg='#535C68', bd=2, command=self.exit_app, font=('arial', 13, 'bold'), width=11, height=3)
        exit_btn.grid(row=0, column=3, padx=6, pady=7)

    def total(self):
        self.m_s_p = self.sanitizer.get()*2
        self.m_m_p = self.mask.get()*5
        self.m_h_g_p = self.hand_gloves.get()*12
        self.m_d_p = self.dettol.get()*30
        self.m_n_p = self.newsprin.get()*5
        self.m_t_g_p = self.thermal_gun.get()*15
        self.total_medical_price = float(self.m_m_p+self.m_h_g_p+self.m_d_p+self.m_n_p+self.m_t_g_p+self.m_s_p)

        self.medical_price.set(f"Rs. {str(self.total_medical_price)}")
        self.c_tax = round((self.total_medical_price * 0.05), 2)
        self.medical_tax.set(f"Rs. {str(self.c_tax)}")

        self.g_r_p = self.rice.get()*10 
        self.g_f_o_p = self.food_oil.get()*10
        self.g_w_p = self.wheat.get()*10
        self.g_d_p = self.daal.get()*6
        self.g_f_p = self.flour.get()*8
        self.g_m_p = self.maggi.get()*5
        self.total_grocery_price = float(self.g_d_p + self.g_f_o_p + self.g_f_p + self.g_m_p + self.g_r_p + self.g_w_p)

        self.grocery_price.set(f"Rs. {str(self.total_grocery_price)}")
        self.g_tax = round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax.set(f"Rs. {str(self.g_tax)}")

        self.c_d_s_p = self.sprite.get()*10
        self.c_d_l_p = self.limka.get()*10
        self.c_d_m_p = self.mazza.get()*10
        self.c_d_c_p = self.coke.get()*10
        self.c_d_f_p = self.fanta.get()*10
        self.c_m_d = self.mountain_duo.get()*10
        self.total_cold_drinks_price = float(self.c_d_s_p+self.c_d_l_p+self.c_d_m_p+self.c_d_c_p+self.c_d_f_p+self.c_m_d)

        self.cold_drinks_price.set(f"Rs. {str(self.total_cold_drinks_price)}")
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set(f"Rs. {str(self.c_d_tax)}")

        self.total_bill = float(self.total_medical_price+self.total_grocery_price+self.total_cold_drinks_price+self.c_tax+self.g_tax+self.c_d_tax)
    
    #==============welcome-bill==============================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, '\tWelcome Webcode Retail')
        self.txtarea.insert(END, f"\nBill number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n=================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

    #======================billArea=========================
    def bill_area(self):
        
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill() 

        # ============medical===========================
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\nSanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
        if self.mask.get() != 0:
            self.txtarea.insert(END, f"\nMask\t\t{self.mask.get()}\t\t{self.m_m_p}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(END, f"\nHand gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
        if self.dettol.get() != 0:
            self.txtarea.insert(END, f"\nDettol\t\t{self.dettol.get()}\t\t{self.m_d_p}")
        if self.newsprin.get() != 0:
            self.txtarea.insert(END, f"\nNewsprin\t\t{self.newsprin.get()}\t\t{self.m_n_p}")
        if self.thermal_gun.get() != 0:
            self.txtarea.insert(END, f"\nThermal gun\t\t{self.thermal_gun.get()}\t\t{self.m_t_g_p}")

        # ==============Grocery============================
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\nFood oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
        if self.daal.get() != 0:
            self.txtarea.insert(END, f"\nDaal\t\t{self.daal.get()}\t\t{self.g_d_p}")
        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\nFlour\t\t{self.flour.get()}\t\t{self.g_f_p}")
        if self.maggi.get() != 0:
            self.txtarea.insert(END, f"\nMaggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")

        #================ColdDrinks==========================
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\nSprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
        if self.limka.get() != 0:
            self.txtarea.insert(END, f"\nLimka\t\t{self.limka.get()}\t\t{self.c_d_l_p}")
        if self.mazza.get() != 0:
            self.txtarea.insert(END, f"\nMazza\t\t{self.mazza.get()}\t\t{self.c_d_m_p}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\nCoke\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
        if self.fanta.get() != 0:
            self.txtarea.insert(END, f"\nFanta\t\t{self.fanta.get()}\t\t{self.c_d_f_p}")
        if self.mountain_duo.get() != 0:
            self.txtarea.insert(END, f"\nMountain Duo\t\t{self.mountain_duo.get()}\t\t{self.c_m_d}")
        
        self.txtarea.insert(END, f"\n------------------------------------")

        # ===============taxes==============================
        if self.medical_tax.get() != 'Rs. 0.0':
            self.txtarea.insert(END, f"\nMedical tax\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != 'Rs. 0.0':
            self.txtarea.insert(END, f"\nMedical tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != 'Rs. 0.0':
            self.txtarea.insert(END, f"\nMedical tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\nTotal Bill:\t\t\t{self.total_bill}")
        self.save_bill()

    #=========savebill============================
    def save_bill(self):
        op = messagebox.askyesno('Save bill', 'Do you want to save the bill')
        if op > 0:
            path = f"bills/{str(self.bill_no.get())}.txt"
            content = self.txtarea.get('1.0', END)
            with open(path, 'w') as dest:
                dest.write(content)
            messagebox.showinfo('Saved', f"Bill no {str(self.bill_no.get())} successfully saved")
        else:
            return
        
    # ===================find_bill================================
    def find_bill(self):
        present = 'no'
        for i in os.listdir('bills/'):
            if i.split('.')[0] == self.search_bill.get():
                self.txtarea.delete('1.0', END)
                with open(f"bills/{i}", 'r') as f1:
                    for d in f1:
                        self.txtarea.insert(END, d)
                present = 'yes'
                break
        if present == 'no':
            messagebox.showinfo('Error', 'Invalid bill no')
    def clear_data(self):
        op = messagebox.askyesno('Clear', 'Do you really want to clear')
        if op > 0:
        #================medical======================
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.dettol.set(0)
            self.newsprin.set(0)
            self.thermal_gun.set(0)
        # ============grocery=========================
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.flour.set(0)
            self.maggi.set(0)
        # =============coldDrinks======================
            self.sprite.set(0)
            self.limka.set(0)
            self.mazza.set(0)
            self.coke.set(0)
            self.fanta.set(0)
            self.mountain_duo.set(0)
        #==============total price===============
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()
    def exit_app(self):
        op = messagebox.askyesno('Exit', 'Do you really want to Exit')
        
        if op > 0:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Bill_App(root)
    root.mainloop()
