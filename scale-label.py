# This user-defined function is called by OVITO to let it draw arbitrary graphics on top of the viewport.
def render(args):
    
    # This demo code prints the current animation frame into the upper left corner of the viewport.
    text1 = "Frame {}".format(args.frame)
    args.painter.drawText(10, 10 + args.painter.fontMetrics().ascent(), text1)
    
    # Also print the current number of particles into the lower left corner of the viewport.
    pipeline = args.scene.selected_pipeline
    if pipeline:
        data = pipeline.compute()
        num_particles = data.particles.count
        text2 = "{} particles".format(num_particles)
        args.painter.drawText(10, args.painter.window().height() - 10, text2)
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Parameters:
bar_length = 10   # Simulation units (e.g. Angstroms)
bar_color = QColor(0,0,0)
label_text = "{} nm".format(bar_length/10)
label_color = QColor(255,255,255)

# This function is called by OVITO on every viewport update.
def render(args):
    if args.is_perspective: 
        raise Exception("This overlay only works with non-perspective viewports.")
        
    # Compute length of bar in screen space
    screen_length = args.project_size((0,0,0), bar_length)

    # Define geometry of bar in screen space
    height = 0.07 * args.painter.window().height()
    margin = 0.02 * args.painter.window().height()
    rect = QRectF(margin, margin, screen_length, height)

    # Render bar rectangle
    args.painter.fillRect(rect, bar_color)

    # Render text label
    font = args.painter.font()
    font.setPixelSize(height)
    args.painter.setFont(font)
    args.painter.setPen(QPen(label_color))
    args.painter.drawText(rect, Qt.AlignCenter, label_text)
