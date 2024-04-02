import maya.cmds as cmds
import maya.OpenMaya as om

class DisplayColorOverride(object):
    '''
    Class for modifying the drawing overrides of selected objects.
    No UI code is contained in this class
    '''

    MAX_OVERRIDE_COLOR = 32

    @classmethod
    def override_color(cls, color_index):
        if (color_index >= cls.MAX_OVERRIDE_COLOR or color_index < 0):
            om.MGlobal.displayError("Color index out-of-range (must be between 0-31)")
            return False
        shapes = cls.shape_nodes()
        if not shapes:
            om.MGlobal.displayError("No shapes nodes selected")
            return False




    @classmethod
    def shape_nodes(cls):
        selection = cmds.ls(selection=True)
        if not selection:
            return None
        
        shapes = []
        for node in selection:
            shapes.extend(cmds.listRelatives(node,shapes=True))

        return shapes
    pass

class DisplayColorOverrideUi(object):
    '''
    Creates a GUI that can be used to override the drawing color 
    of selected objects.
    '''
    pass


#Get the list of the shapes of the selected objects


#Enable drawing overrides

#Change the drawing override color