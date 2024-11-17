import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculator")
        self.calc_exp = [
            ["%","CE","C","\u232b"],
            ["1/x","x\u00b2","\u221Ax\u0305","\u00F7"],
            ["7","8","9","x"],
            ["4","5","6","-"],
            ["1","2","3","+"],
            [" ","0",".","="]
        ]
        self.center_window()
        self.top_panel()
        self.calculation_screen()
        self.center_panels()
        

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 2
        self.geometry(f"+{x}+{y}")
        self.maxsize(width=380,height=480)
        self.minsize(width=380,height=480)
        

    def top_panel(self):
        panel = tk.Frame(self,highlightbackground="white", highlightthickness=2)
        panel.pack(fill="both")
        label = tk.Label(panel,text="Calculator",fg="purple",font= ('Helvetica  30 bold italic'))
        label.pack(fill="both")

    def calculation_screen(self):
        self.expression=tk.StringVar(value=0)
        self.expression_c=tk.StringVar(value=0)
        panel = tk.Frame(self, highlightbackground="purple",height=10, highlightthickness=5,bg="#CB93F7")
        panel.pack(fill="both",padx=10,pady=10)

        self.expression_label = tk.Label(panel,fg="purple",font= ('Helvetica 15 bold italic'), anchor="e",bg="#CB93F7")
        self.expression_label.config(textvariable=self.expression)
        self.expression_label.pack(fill="both",padx=(5))

        self.expression_label_c = tk.Label(panel,fg="purple",font= ('Helvetica 22 bold italic'), anchor="e",bg="#CB93F7")
        self.expression_label_c.config(textvariable=self.expression_c)
        self.expression_label_c.pack(fill='both',padx=(5))

    def center_panels(self):
        back=BackEnd()
        self.center_panel=tk.Frame(self,highlightbackground="white", highlightthickness=2)
        self.center_panel.pack(fill="both",padx=10,pady=10,expand=True)
        
        for row in range(6):
            for col in range(4):
                self.CalcButton = tk.Button(self.center_panel, text=str(self.calc_exp[row][col]),height=2,width=8,bg="purple",fg="white",font= ('Helvetica 12 bold italic'))
                self.CalcButton.config(command=lambda i=str(str(row+1)+str(col+1)):back.write_expression(i))
                self.CalcButton.grid(row=row, column=col, padx=0, pady=0,sticky="news")


class BackEnd():
    def __init__(self) -> None:
        self.result_p = False
        pass

    def write_expression(self,n):
        self.match_exp = ["+","-","\u00F7","*"]
        if n=="11": #  % Percentage Sign
            if app.expression.get() == "0":
                app.expression_c.set("0")
                pass
            else:
                exp=app.expression_c.get()
                res= eval(exp+"/100")
                result=eval(app.expression.get()+"("+exp+"/100)")
                if self.result_p == True:
                    app.expression.set(app.expression.get()+str(res))
                else:
                    #app.expression.set("1/("+ app.expression_c.get()+")")
                    pass
                app.expression_c.set(result)
            pass
            self.result_p=True
            pass 

        elif n=="12": # CE Sign
            app.expression_c.set("0")
            pass

        elif n=="13": # C Sign
            app.expression.set("0")
            app.expression_c.set("0")
            pass

        elif n=="14": # <- BackSpace Sign
            if app.expression_c.get()=="0":
                pass
            else:
                exp=app.expression_c.get()
                exp=exp[:-1]
                if len(exp)==0:
                    app.expression_c.set("0")
                else:
                    app.expression_c.set(exp)
            pass

        elif n=="21": # 1/x Sign
            if app.expression.get()=="0":
                if app.expression_c.get() == "0":
                    app.expression_c.set("Cannot Divide By Zero")
                else:
                    exp=app.expression_c.get()
                    result=eval("1/"+exp)
                    app.expression_c.set(result)
                    app.expression.set("1/("+ exp+")")   
            else:
                exp=app.expression_c.get()
                result=eval("1/"+exp)
                if self.result_p == True:
                    app.expression.set("1/("+ app.expression.get()+")")
                else:
                    app.expression.set("1/("+ app.expression_c.get()+")")
                app.expression_c.set(result)
                pass
            self.result_p=True
            pass

        elif n=="22": # x^2 Sign  #" x\u00b2
            if app.expression.get()=="0":
                exp=app.expression_c.get()
                result=eval(exp+"**2")
                app.expression_c.set(result)
                app.expression.set("sqr("+ exp+")")   
            else:
                exp=app.expression_c.get()
                result=eval(exp+"**2")
                if self.result_p == True:
                    app.expression.set("sqr("+ app.expression.get()+")")
                else:
                    app.expression.set("sqr("+ app.expression_c.get()+")")
                app.expression_c.set(result)
                pass
            self.result_p=True
            pass

        elif n=="23": # Squareroot Sign \u221Ax\u0305
            if app.expression.get()=="0":
                exp=app.expression_c.get()
                result=eval(exp+"**.5")
                app.expression_c.set(result)
                app.expression.set("\u221A("+ exp+")")   
            else:
                exp=app.expression_c.get()
                result=eval(exp+"**.5")
                if self.result_p == True:
                    app.expression.set("\u221A("+ app.expression.get()+")")
                else:
                    app.expression.set("\u221A("+ app.expression_c.get()+")")
                app.expression_c.set(result)
                pass
            self.result_p=True
            pass

        elif n=="24": # / Divide Sign \u00F7
            if app.expression.get() == "0":
                app.expression.set(app.expression_c.get()+"\u00F7")
                self.result_p=True

            elif any(x in app.expression.get()[-1] for x in self.match_exp)  and app.expression.get()[-2] ==")":
                app.expression.set(app.expression.get()[:-1]+"\u00F7")

            elif app.expression.get()[-1] ==")":
                app.expression.set(app.expression.get()+"\u00F7")

            elif app.expression.get()[-1] =="=":
                app.expression.set(app.expression_c.get()+"\u00F7")
                
            else:
                exp=app.expression.get().replace("\u00F7","/")
                result = str(eval(exp+app.expression_c.get()))
                app.expression_c.set(result)
                app.expression.set(result+"\u00F7")
            self.result_p=True
            pass

        elif n=="31": # 7 Sign
            if app.expression_c.get() == "0":
                app.expression_c.set("7")
            else:
                if self.result_p==False:
                    app.expression_c.set(app.expression_c.get()+"7")
                else:
                    app.expression_c.set("7")
                    self.result_p=False
            pass

        elif n=="32": # 8 Sign
            if app.expression_c.get() == "0":
                app.expression_c.set("8")
            else:
                if self.result_p==False:
                    app.expression_c.set(app.expression_c.get()+"8")
                else:
                    app.expression_c.set("8")
                    self.result_p=False
            pass

        elif n=="33": # 9 Sign
            if app.expression_c.get() == "0":
                app.expression_c.set("9")
            else:
                if self.result_p==False:
                    app.expression_c.set(app.expression_c.get()+"9")
                else:
                    app.expression_c.set("9")
                    self.result_p=False
            pass

        elif n=="34": # X Multiply Sign
            if app.expression.get() == "0":
                app.expression.set(app.expression_c.get()+"*")
                self.result_p=True

            elif any(x in app.expression.get()[-1] for x in self.match_exp)  and app.expression.get()[-2] ==")":
                app.expression.set(app.expression.get()[:-1]+"*")

            elif app.expression.get()[-1] ==")":
                app.expression.set(app.expression.get()+"*")

            elif app.expression.get()[-1] =="=":
                app.expression.set(app.expression_c.get()+"*")
                pass
            else:
                exp=app.expression.get().replace("\u00F7","/")
                result = str(eval(exp+app.expression_c.get()))
                app.expression_c.set(result)
                app.expression.set(result+"*")
                self.result_p=True

            self.result_p=True    
            pass

        elif n=="41": # 4 Sign
            if app.expression_c.get() == "0":
                app.expression_c.set("4")
            else:
                if self.result_p==False:
                    app.expression_c.set(app.expression_c.get()+"4")
                else:
                    app.expression_c.set("4")
                    self.result_p=False
            pass

        elif n=="42": # 5 Sign
            if app.expression_c.get() == "0":
                app.expression_c.set("5")
            else:
                if self.result_p==False:
                    app.expression_c.set(app.expression_c.get()+"5")
                else:
                    app.expression_c.set("5")
                    self.result_p=False
            pass

        elif n=="43": # 6 Sign
            if app.expression_c.get() == "0":
                app.expression_c.set("6")
            else:
                if self.result_p==False:
                    app.expression_c.set(app.expression_c.get()+"6")
                else:
                    app.expression_c.set("6")
                    self.result_p=False
            pass

        elif n=="44": # - Subtract Sign
            if app.expression.get() == "0":
                app.expression.set(app.expression_c.get()+"-")
                self.result_p=True

            elif any(x in app.expression.get()[-1] for x in self.match_exp)  and app.expression.get()[-2] ==")":
                app.expression.set(app.expression.get()[:-1]+"-")

            elif app.expression.get()[-1] ==")":
                app.expression.set(app.expression.get()+"-")

            elif app.expression.get()[-1] =="=":
                app.expression.set(app.expression_c.get()+"-")
                pass
            else:
                exp=app.expression.get().replace("\u00F7","/")
                result = str(eval(exp+app.expression_c.get()))
                app.expression_c.set(result)
                app.expression.set(result+"-")
                self.result_p=True
            
            self.result_p=True
            pass

        elif n=="51": # 1 Sign
            if app.expression_c.get() == "0":
                app.expression_c.set("1")
            else:
                if self.result_p==False:
                    app.expression_c.set(app.expression_c.get()+"1")
                else:
                    app.expression_c.set("1")
                    self.result_p=False
            pass

        elif n=="52": # 2 Sign
            if app.expression_c.get() == "0":
                app.expression_c.set("2")
            else:
                if self.result_p==False:
                    app.expression_c.set(app.expression_c.get()+"2")
                else:
                    app.expression_c.set("2")
                    self.result_p=False
            pass

        elif n=="53": # 3 Sign
            if app.expression_c.get() == "0":
                app.expression_c.set("3")
            else:
                if self.result_p==False:
                    app.expression_c.set(app.expression_c.get()+"3")
                else:
                    app.expression_c.set("3")
                    self.result_p=False
            pass

        elif n=="54": # + Add Sign
            if app.expression.get() == "0":
                app.expression.set(app.expression_c.get()+"+")
                self.result_p=True

            elif any(x in app.expression.get()[-1] for x in self.match_exp)  and app.expression.get()[-2] ==")":
                app.expression.set(app.expression.get()[:-1]+"+")

            elif app.expression.get()[-1] ==")":
                app.expression.set(app.expression.get()+"+")

            elif app.expression.get()[-1] =="=":
                app.expression.set(app.expression_c.get()+"+")
                pass
            else:
                exp=app.expression.get().replace("\u00F7","/")
                result = str(eval(exp+app.expression_c.get()))
                app.expression_c.set(result)
                app.expression.set(result+"+")
            
            self.result_p=True
            pass

        elif n=="61": # +/- Sign
            pass

        elif n=="62": # 0 Sign
            if app.expression_c.get() == "0":
                app.expression_c.set("0")
            else:
                if self.result_p==False:
                    app.expression_c.set(app.expression_c.get()+"0")
                else:
                    app.expression_c.set("0")
                    self.result_p=False
            pass

        elif n=="63": # . Sign
            app.expression_c.set(app.expression_c.get()+".")
            pass

        elif n=="64": # = Sign   # Squareroot: \u221A  # Square: 
            if app.expression.get() == "0":
                app.expression.set(app.expression_c.get()+"=")
                self.result_p=True
            else:
                exps=app.expression.get()
                exp=exps.replace("\u00F7","/")
                if any(x in exps for x in self.match_exp) and "\u221A" in exp:
                    exp=exps.removeprefix("\u221A")
                    exp=exp.removeprefix("(")
                    exp=exp.removeprefix(")")
                    
                elif any(x in exps for x in self.match_exp) and exp[-1]=="=":
                    n1=self.find_pos_of_first_exp(exps)
                    val = exp[:n1]
                    exp=exp.removeprefix(val)
                    exp=exp.removesuffix("=")
                    exp=app.expression_c.get()+exp
                    result = str(eval(exp))
                    exp=exp.replace("/","\u00F7")
                    app.expression.set(exp+"=")
                    app.expression_c.set(result)
                    pass

                elif any(x in exps[-1] for x in self.match_exp):
                    result = str(eval(exp+app.expression_c.get()))
                    app.expression.set(exps+app.expression_c.get()+"=")
                    app.expression_c.set(result)
                
                elif app.expression.get()[-1] == ")":
                    app.expression.set(app.expression.get()+"=")

                elif app.expression.get()[-1] == "=":
                    app.expression.set(app.expression_c.get()+"=")

                elif any(x in exps for x in self.match_exp):
                    app.expression.set(app.expression_c.get()+"=")

                self.result_p=True
                    
            pass
    
    def find_pos_of_first_exp(self,exp=""):
        s=0
        for i in self.match_exp:
            if s<exp.find(i):
                s=exp.find(i) 
        return s






if __name__ == "__main__":
    app = App()
    app.mainloop()