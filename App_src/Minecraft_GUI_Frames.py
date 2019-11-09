from Minecraft_GUI_Widgets	import VPackPart, HPackPart
from Minecraft_GUI_Import	import ImportFrame
from Minecraft_GUI_Export	import ExportFrame
from Minecraft_GUI_Circle	import CircleFrame
from Minecraft_GUI_DrawCube	import DrawCubic
from Minecraft_GUI_Clone	import Duplicate
from Minecraft_GUI_Connect	import Connection
from Minecraft_GUI_Block	import BlockIData

def DrawFrames( root ):
	cfgPanel = HPackPart( root )
	funPanel = HPackPart( root )

	Connection(	VPackPart( cfgPanel ) )
	BlockIData( VPackPart( cfgPanel ) )

	ImportFrame(	VPackPart( funPanel ) )
	CircleFrame(	VPackPart( funPanel ) )
	DrawCubic(		VPackPart( funPanel ) )
	Duplicate(		VPackPart( funPanel ) )
	ExportFrame(	VPackPart( funPanel ) )