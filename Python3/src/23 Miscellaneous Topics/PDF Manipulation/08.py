from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, TableStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER,TA_LEFT, TA_JUSTIFY
from reportlab.platypus import Table
#from reportlab.lib.pagesizes import cm
#from compras.settings import EMPRESA
PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()

Title = "Hello world"
pageinfo = "platypus example"
def myFirstPage(canvas, doc):
    canvas.saveState()
    go2(canvas);
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch,"First Page / %s" % pageinfo)
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch,"Page %d %s" % (doc.page, pageinfo))
    hello(canvas)
    canvas.restoreState()

def go2(canvas):
    p = ParagraphStyle('parrafos', 
                           alignment = TA_CENTER,
                           fontSize = 8,
                           fontName="Times-Roman")        
    data = [
            [ Paragraph("Question",p) ],  
            [ Paragraph("Response",p) ],  
            [ Paragraph("Virtual Coach",p) ]
           ]
#    t = Table(data, colWidths=[1 * inch], rowHeights=0.5 * inch)
    def getTable(d):
        t = Table(d, colWidths=[1 * inch], rowHeights=0.5 * inch)
        t.setStyle(TableStyle(
                [
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('BACKGROUND', (0, 0), (-1, -1), colors.green),
                    ('FONTSIZE', (0, 0), (-1, -1), 8),
                    ('ALIGN',(0,0),(-1,-1),'LEFT'),
                    ('VALIGN',(0,0),(-1,-1),'TOP'),
                ]
            ))
#         t.wrapOn(canvas, 0, 0)
#         t.drawOn(canvas, 100, PAGE_HEIGHT*0) 
        return t
    
    getTable(data)
    
def go():
    doc = SimpleDocTemplate("phello2.pdf")
    Story = [Spacer(1,2*inch)]
    style = styles["Normal"]
    for i in range(100):
        bogustext = ("Paragraph number %s. " % i) *20
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))
    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)


def hello(c):
    from reportlab.lib.units import inch
    # move the origin up and to the left
    c.translate(inch,inch)
    # define a large font
    c.setFont("Helvetica", 14)
    # choose some colors
    c.setStrokeColorRGB(0.2,0.5,0.3)
    c.setFillColorRGB(1,0,1)
    # draw some lines
    c.line(0,0,0,1.7*inch)
    c.line(0,0,1*inch,0)
    # draw a rectangle
    c.rect(0.2*inch,0.2*inch,1*inch,1.5*inch, fill=1)
    # make text go straight up
    c.rotate(45)
    # change color
    c.setFillColorRGB(0,0,0.77)
    # say hello (note after rotate the y coord needs to be negative!)
    c.drawString(0.3*inch, -inch, "Hello World")
    
if __name__ == "__main__":
    go()
    