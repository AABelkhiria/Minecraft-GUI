from Minecraft_GUI_Dependancies import *
from mine import *

combotext = StringVar( )
secBlock = []

def BrowseFolder( combo ):
	path = filedialog.askdirectory( )
	combolist = []
	for ( paths, names, filenames ) in walk( path ):
		for filename in filenames:
			if filename.endswith( '.blk' ):
				combolist.append( filename )
	combo['values'] = combolist

	if len(combolist) == 1:
		combo.set(combolist[0])
	else:
		combo.set('')


def Refresh( combo ):
	combolist = []
	for ( paths, names, filenames ) in walk( getcwd( ) ):
		for filename in filenames:
			if filename.endswith( '.blk' ):
				combolist.append( filename )
	combo['values'] = combolist

	if len(combolist) == 1:
		combo.set(combolist[0])
	else:
		combo.set('')

def ProcessSetBlock( mc, x, y, z, ID, data, f1, f3 ):
	global secBlock
	if mc.getBlock( x, y, z ) != 7:
		if ID == 64:
			if data != 8:
				if mc.getBlock( x, y + 1, z ) != 7:
					mc.setBlock( x, y, z, block.Block( ID, data ) )
					mc.setBlock( x, y + 1, z, block.Block( ID, 8 ) )
			else:
				pass

		elif ID == 50:
			Torch = SecBlock( x, y, z, ID, data )
			secBlock.append( Torch )

		elif ID == 7:
			pass

		else:
			mc.setBlock( x, y, z, block.Block( ID, data ) )

def SetSecondary( mc ):
	global secBlock
	for blk in secBlock:
		mc.setBlock( blk.x, blk.y, blk.z, block.Block( blk.ID, blk.Data ) )
	secBlock = []

def ImportButton( ):
	mc = Minecraft( )
	name = combotext.get( )
	x1, y1, z1 = mc.player.getTilePos( )
	y, z = 0, 0

	try:
		with open( name, 'r' )  as file:
			lines = file.readlines( )

			f1, f2, f3 = 0, 0, 0
			if messagebox.askyesno( "Import Blocks", "Are you sure you want to import " + name + "?" ):
				for line in lines:
					if "f" in line:
						f1 = int( line.split( " " )[1] )
						f2 = int( line.split( " " )[2] )
						f3 = int( line.split( " " )[3] )
					elif "*" in line:
						y = y + 1
						z = 0
					else:
						for x in range( len( line.split( " " ) ) - 1 ):
							copyBlock = line.split( " " )[x]
							ID = int( copyBlock.split( ',' )[0] )
							Data = int( copyBlock.split( ',' )[1] )
							ProcessSetBlock( mc, x1 + x, y1 + y, z1 + z, ID, Data, f1, f3 )
						z = z + 1
				SetSecondary( mc )
	except Exception as e:
		print e

def ImportFrame( frame ):
	browse = Frame( frame )
	browse.pack( side = LEFT, expand = True )

	buttons = Frame( browse )
	buttons.pack( )

	msg = Message( frame, 'Import' )
	msg.place( x = 5, y = -9 )

	btn1 = Button( buttons, 'Refresh' )
	btn1.pack( padx = 10, side = LEFT )
	btn1.configure( width = 10 )
	btn1.configure( command = lambda: Refresh( combo ) )

	btn2 = Button ( buttons,'Browse Folder' )
	btn2.pack( padx = 5, pady = 5, side = LEFT )
	btn2.configure( width = 16 )
	btn2.configure( command = lambda: BrowseFolder( combo ) )

	combo = Combobox( browse )
	combo.pack( padx = 10, pady = 5 )
	combo.configure( width = 37 )
	combo.configure( textvariable = combotext )
	combo.configure( takefocus = "" )
	combo.configure( state= "readonly" )	
	Refresh( combo )

	btn3, btn4 = Righty( frame )
	btn3.configure( command = ImportButton )
	btn4.configure( command = lambda: PreviewImport( combotext.get( ) ) )