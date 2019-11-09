from Minecraft_GUI_Dependancies import *
from mine import *

def mcConnect( ):
	try:
		GV.mc = Minecraft( )
		for button in btn:
			button.configure( state = NORMAL )
	except Exception as e:
		if DEBUG:
			print e
		tkMessageBox.showerror( "Error", "Unable to Connect to Minecraft" )
		for button in btn:
			button.configure( state = DISABLED )

def SetPos1( ):
	try:
		x1.set( GV.mc.player.getTilePos( ).x )
		y1.set( GV.mc.player.getTilePos( ).y )
		z1.set( GV.mc.player.getTilePos( ).z )
	except Exception as e:
		if DEBUG:
			print e
		tkMessageBox.showerror( "Error", "Unable to Connect to Minecraft !" )
		for button in btn:
			button.configure( state = DISABLED )

def SetPos11( ):
	pass

def SetPos2( ):
	try:
		x2.set( GV.mc.player.getTilePos( ).x )
		y2.set( GV.mc.player.getTilePos( ).y )
		z2.set( GV.mc.player.getTilePos( ).z )
	except Exception as e:
		if DEBUG:
			print e
		tkMessageBox.showerror( "Error", "Unable to Connect to Minecraft !" )
		for button in btn:
			button.configure( state = DISABLED )

def SetPos21( ):
	pass

def Connection( main ):
	msg = Message( main, 'Connection' )
	msg.place( x = 5, y = -9 )

	btn0 = Button( main, 'Connect' )
	btn0.pack( side = TOP, fill = X, pady = 12, padx = 5 )
	btn0.configure( command = mcConnect )
	btn0.configure( state = NORMAL )

	frame = Frame( main )
	frame.pack( side = BOTTOM, fill = X )

	txt1 = Message( frame, 'Set Position 1 by' )
	txt1.pack( side = TOP )

	btn01 = Button( frame, 'Player Position' )
	btn01.pack( side = TOP, fill = X, pady = 7, padx = 7 )
	btn01.configure( command = SetPos1 )

	btn11 = Button( frame, 'Last Sword Hit' )
	btn11.pack( side = TOP, fill = X, padx = 7 )
	btn11.configure( command = SetPos11 )

	pos1 = Frame( frame )
	pos1.pack( side = TOP, pady = 7, padx = 7 )

	textx1 = Message( pos1, 'x' )
	textx1.pack( side = LEFT )

	xval1 = Entry( pos1 )
	xval1.pack( side = LEFT )
	xval1.configure( textvariable = x1 )
	xval1.configure( width = 4 )

	texty1 = Message( pos1, 'y' )
	texty1.pack( side = LEFT )

	yval1 = Entry( pos1 )
	yval1.pack( side = LEFT )
	yval1.configure( textvariable = y1 )
	yval1.configure( width = 4 )

	textz1 = Message( pos1, 'z' )
	textz1.pack( side = LEFT )

	zval1 = Entry( pos1 )
	zval1.pack( side = LEFT )
	zval1.configure( textvariable = z1 )
	zval1.configure( width = 4 )

	txt2 = Message( frame, 'Set Position 2 by' )
	txt2.pack( side = TOP )

	btn02 = Button( frame, 'Player Position' )
	btn02.pack( side = TOP, fill = X, pady = 7, padx = 7 )
	btn02.configure( command = SetPos2 )

	btn21 = Button( frame, 'Last Sword Hit' )
	btn21.pack( side = TOP, fill = X, padx = 7 )
	btn21.configure( command = SetPos21 )

	pos2 = Frame( frame )
	pos2.pack( side = TOP, pady = 7 )

	textx2 = Message( pos2, 'x' )
	textx2.pack( side = LEFT )

	xval2 = Entry( pos2 )
	xval2.pack( side = LEFT )
	xval2.configure( textvariable = x2 )
	xval2.configure( width = 4 )

	texty2 = Message( pos2, 'y' )
	texty2.pack( side = LEFT )

	yval2 = Entry( pos2 )
	yval2.pack( side = LEFT )
	yval2.configure( textvariable = y2 )
	yval2.configure( width = 4 )

	textz2 = Message( pos2, 'z' )
	textz2.pack( side = LEFT )

	zval2 = Entry( pos2 )
	zval2.pack( side = LEFT )
	zval2.configure( textvariable = z2 )
	zval2.configure( width = 4 )

	btn.append( btn01 )
	btn.append( btn02 )
	btn.append( btn11 )
	btn.append( btn21 )