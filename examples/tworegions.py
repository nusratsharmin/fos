import sys
import numpy as np
from fos import *

from PySide.QtGui import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Window()

    mytransform = IdentityTransform()
    mytransform.set_translation( x = 5 )
    mytransform.set_scale( 1.5, 1, 1 )
    mytransform.rotate( 45, 1.0, 0, 0 )

    region = Region( regionname = "Main", transform = mytransform, resolution = ("mm", "mm", "mm"),
                     extent_min = np.array( [-5.0, -5, -5] ), extent_max = np.array( [5, 5, 5] )  )

    region.add_actor( Axes( name = "3 axes", linewidth = 5.0) )
    w.add_region ( region )

    mytransform = IdentityTransform()
    mytransform.set_translation( x = -40 )

    region2 = Region( regionname = "Main2", transform = mytransform, resolution = ("mm", "mm", "mm"),
                      extent_min = np.array( [-5.0, -5, -5] ), extent_max = np.array( [5, 5, 5] )  )

    region2.add_actor( Axes( name = "3 axes", linewidth = 2.0) )
    w.add_region( region2 )

    w.refocus_camera()

    sys.exit(app.exec_())
