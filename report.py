from fpdf import FPDF
def reportes(a,b):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_title(title=f"Reporte de {b}")
    pdf.set_author(author="Ing. Jonathan Sanmartin")
    pdf.set_subject(subject="Proyecto de Tratamiento de datos")
    pdf.add_page()
    pdf.set_font('Arial', '', 5)
    pdf.text(x=190, y=2, txt="Jonathan Sanmartin")
    pdf.set_font('Arial', 'B', 18)
    pdf.set_text_color(60, 99, 234)
    pdf.text(x=15,y=10, txt=f"REPORTE DEL PRODUCTO \"{b}\"")
    f = 15
    nu = 1
    hoja=1
    for documentos in a.find({}):
        try:
            hoja += 1
            print("articulo--> ", hoja)
            print("Nombre", documentos["Nom_pro"])
            print("Estado:", documentos["Est_pro"])
            print("Precio:", documentos["Pre_pro"])
            print("*************************************************")
            pdf.set_font('Arial', 'B', 12)
            pdf.set_text_color(159, 35, 60)
            pdf.text(x=17, y=f + 8, txt="Artículo:")
            pdf.text(x=17, y=f + 13, txt="Estado :")
            pdf.text(x=17, y=f + 18, txt="Precio  :")
            pdf.set_font('Arial', '', 8)
            pdf.set_text_color(0, 0, 0)
            pdf.text(x=10, y=f + 12, txt=str(nu))
            pdf.text(x=38, y=f + 8, txt=documentos["Nom_pro"].encode('latin-1', 'replace').decode('latin-1'))
            pdf.text(x=38, y=f + 13, txt=documentos["Est_pro"])
            pdf.text(x=38, y=f + 18, txt=documentos["Pre_pro"])
            pdf.line(10, f + 2, 200, f + 2)
            f += 18
            nu += 1
            if (hoja == 15):
                pdf.add_page()
                hoja = 0
                f = 15
        except Exception as e:
            print("Falla del Sistema", e)
            print("eeeeeeeeeeeerroooooooooooooorrrrrrrrrrrrrrrrrrr")
    #print("Total de datos cargados: ",a.count_documents({}))
    pdf.output(f"Reportes/REPORTE_{b}_JS.pdf")
    pdf.output(f"Reportes/general.pdf")